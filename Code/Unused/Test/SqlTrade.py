import MySQLdb
import gc
import globalData as gl

class MySQL_Item:
  def __init__(self):
    self.db = MySQLdb.connect(host=gl.get_value("HOST"), user=gl.get_value("USER"), password=gl.get_value("PASSWORD"), db=gl.get_value("BD"))
    self.cur = self.db.cursor()
    #create_table()
  def create_table(self):
    create ="""CREATE TABLE IF NOT EXISTS trade_data(
                id SMALLINT UNSIGNED NOT NULL auto_increment,
                item_id SMALLINT UNSIGNED NOT NULL,
                amount SMALLINT UNSIGNED NOT NULL,
                status TINYINT UNSIGNED NOT NULL,
                primary key (id)
            ) ENGINE = InnoDB;            
            """
    self.cur.exec(create)
  def close_connect(self):
    self.db.close()
    gc.collect()
  def query_insert(self, data):
    insert = "INSERT INTO trade_data (item_id, amount, status) VALUES (%s ,%s, %s);"
    self.cur.execute(insert, data)
    self.db.commit()

  def query_select_all(self):
    select_all = "SELECT * FROM user_data;"
    self.cur.execute(select_all)
    data = self.cur.fetchall()
    return data



