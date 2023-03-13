import MySQLdb
import gc
import globalData as gl

class MySQL_Message:
  def __init__(self):
    self.db = MySQLdb.connect(host=gl.get_value("HOST"), user=gl.get_value("USER"),
    password=gl.get_value("PASSWORD"), db=gl.get_value("BD")
    ,charset='utf8')
    self.cur = self.db.cursor()
    self.create_table()

  def create_table(self):
    create ="""CREATE TABLE IF NOT EXISTS message(
                sender_id SMALLINT UNSIGNED NOT NULL,
                receiver_id SMALLINT UNSIGNED NOT NULL,
                text VARCHAR(100) NOT NULL
            ) ENGINE = InnoDB;            
            """
    self.cur.execute(create)
  def close_connect(self):
    self.db.close()
    gc.collect()
  def query_insert(self, data):
    insert = """INSERT INTO message (sender_id,receiver_id,text)
    VALUES (%d ,%d,'%s');"""%(data[0],data[1],data[2])
    self.cur.execute(insert)
    self.db.commit()

  def query_select(self,this,other):
    select = "SELECT * FROM message WHERE sender_id = %d AND receiver_id = %d OR sender_id = %d AND receiver_id = %d;"%(this,other,other,this)
    self.cur.execute(select)
    data = self.cur.fetchall()
    return data

  def get_name(self,id):
    select = "SELECT user_name FROM user_data WHERE id = %d;"%id
    self.cur.execute(select)
    name = self.cur.fetchall()
    if len(name)>0:
            return name[0][0]
    else:
            return "未知用户"