import datetime
import logging

from PySide2.QtCore import Qt, Slot
from PySide2.QtSql import QSqlDatabase, QSqlQuery, QSqlRecord, QSqlTableModel

table_name = "Conversations"


def createTable():
    if table_name in QSqlDatabase.database().tables():
        return

    query = QSqlQuery()
    if not query.exec_(
            """
            CREATE TABLE IF NOT EXISTS 'Conversations' (
                'author' TEXT NOT NULL,
                'recipient' TEXT NOT NULL,
                'timestamp' TEXT NOT NULL,
                'message' TEXT NOT NULL,
            FOREIGN KEY('author') REFERENCES Contacts ( name ),
            FOREIGN KEY('recipient') REFERENCES Contacts ( name )
            )
            """
    ):
        logging.error("Failed to query database")

    # This adds the first message from the Bot
    # and further development is required to make it interactive.
    query.exec_(
        """
        INSERT INTO Conversations VALUES(
            'machine', 'Me', '2019-01-07T14:36:06', 'Hello!'
        )
        """
    )
    logging.info(query)


class SqlConversationModel(QSqlTableModel):

    def __init__(self, parent=None):
        super(SqlConversationModel, self).__init__(parent)

        createTable()
        self.setTable(table_name)
        self.setSort(2, Qt.DescendingOrder)
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.recipient = ""

        self.select()
        logging.debug("Table was loaded successfully.")

    def get_print_tb(self):
        logging.debug("mohsen is checking")

    def setRecipient(self, recipient):
        if recipient == self.recipient:
            pass

        self.recipient = recipient

        filter_str = (
            "(recipient = '{}' AND author = 'Me') OR " "(recipient = 'Me' AND author='{}')"
        ).format(self.recipient)
        self.setFilter(filter_str)
        self.select()

    def data(self, index, role):
        if role < Qt.UserRole:
            return QSqlTableModel.data(self, index, role)

        sql_record = QSqlRecord()
        sql_record = self.record(index.row())

        return sql_record.value(role - Qt.UserRole)

    def roleNames(self):
        """Converts dict to hash because that's the result expected
        by QSqlTableModel"""
        names = {}
        author = "author".encode()
        recipient = "recipient".encode()
        timestamp = "timestamp".encode()
        message = "message".encode()

        names[hash(Qt.UserRole)] = author
        names[hash(Qt.UserRole + 1)] = recipient
        names[hash(Qt.UserRole + 2)] = timestamp
        names[hash(Qt.UserRole + 3)] = message

        return names
    @Slot(str,str,str)
    def send_message(self, recipient, message, author):
        timestamp = datetime.datetime.now()

        new_record = self.record()
        new_record.setValue("author", author)
        new_record.setValue("recipient", recipient)
        new_record.setValue("timestamp", str(timestamp))
        new_record.setValue("message", message)

        logging.debug('Message: "{}" \n Received by: "{}"'.format(message, recipient))

        if not self.insertRecord(self.rowCount(), new_record):
            logging.error("Failed to send message: {}".format(self.lastError().text()))
            return

        self.submitAll()
        self.select()