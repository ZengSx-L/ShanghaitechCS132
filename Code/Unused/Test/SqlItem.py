import MySQLdb
import gc
import globalData as gl

class MySQL_Item:
  def __init__(self):
    self.db = MySQLdb.connect(host=gl.get_value("HOST"), user=gl.get_value("USER"), password=gl.get_value("PASSWORD"), db=gl.get_value("BD"))
    self.cur = self.db.cursor()
    self.create_table()
  def create_table(self):
    create ="""CREATE TABLE IF NOT EXISTS item_data(
                id SMALLINT UNSIGNED NOT NULL auto_increment,
                item_name VARCHAR(20) NOT NULL,
                price DECIMAL(8,2) UNSIGNED NOT NULL,
                seller_id SMALLINT UNSIGNED NOT NULL,
                stock SMALLINT UNSIGNED NOT NULL,
                intro VARCHAR(100) NOT NULL,
                img_name VARCHAR(20) NOT NULL,
                tag SMALLINT UNSIGNED NOT NULL,
                primary key (id)
            ) ENGINE = InnoDB;            
            """
    self.cur.exec(create)
  def close_connect(self):
    self.db.close()
    gc.collect()
  def query_insert(self, data):
    insert = "INSERT INTO item_data (item_name,seller_id,price,stock,intro, img_name,tag) VALUES (%s ,%d, %f, %d, %s, %s, %d);"
    self.cur.execute(insert, data)
    self.db.commit()

  def query_select_all(self):
    select_all = "SELECT * FROM item_data;"
    self.cur.execute(select_all)
    data = self.cur.fetchall()
    return data

  def query_select_tag(self,data):
    select_all = "SELECT * FROM item_data WHERE tag = %s;"
    self.cur.execute(select_all)
    data = self.cur.fetchall()
    return data

  def query_select_name(self,data):
    select_all = "SELECT * FROM item_data WHERE tag_1 = %s;"
    self.cur.execute(select_all)
    data = self.cur.fetchall()
    return data



