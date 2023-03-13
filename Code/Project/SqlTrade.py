import MySQLdb
import gc
import globalData as gl

class MySQL_Trade:
  def __init__(self):
    self.db = MySQLdb.connect(host=gl.get_value("HOST"), user=gl.get_value("USER"),
    password=gl.get_value("PASSWORD"), db=gl.get_value("BD")
    ,charset='utf8')
    self.cur = self.db.cursor()
    self.create_table()
    self.create_comment_table()
  def create_table(self):
    create ="""CREATE TABLE IF NOT EXISTS trade_data(
                id SMALLINT UNSIGNED NOT NULL auto_increment,
                item_id SMALLINT UNSIGNED NOT NULL,
                seller_id SMALLINT UNSIGNED NOT NULL,
                buyer_id SMALLINT UNSIGNED NOT NULL,
                amount SMALLINT UNSIGNED NOT NULL,
                price DECIMAL(8,2) UNSIGNED NOT NULL,
                address VARCHAR(50) NOT NULL,
                status TINYINT UNSIGNED DEFAULT 0,
                primary key (id)
            ) ENGINE = InnoDB;            
            """
    self.cur.execute(create)

  def close_connect(self):
    self.db.close()
    gc.collect()
    
  def query_insert(self, data):
    insert = """INSERT INTO trade_data (item_id,seller_id,buyer_id,amount,price,address)
    VALUES (%d ,%d, %d,%d,%.2f,'%s');"""%(data[0],data[1],data[2],data[3],data[4],data[5])
    self.cur.execute(insert)
    self.db.commit()

  def query_select_buyer(self,id):
    select = "SELECT * FROM trade_data WHERE buyer_id = %d;"%id
    self.cur.execute(select)
    data = self.cur.fetchall()
    return data

  def query_select_seller(self,id):
    select = "SELECT * FROM trade_data WHERE seller_id = %d;"%id
    self.cur.execute(select)
    data = self.cur.fetchall()
    return data

  def query_select_all(self):
    select = "SELECT * FROM trade_data ;"
    self.cur.execute(select)
    data = self.cur.fetchall()
    return data

  def get_balance(self,user):
    select = "SELECT balance FROM user_data WHERE id = %d;"%user
    self.cur.execute(select)
    balance = self.cur.fetchall()
    return balance[0][0]
  
  def set_balance(self,user,balance):
    update = "UPDATE user_data SET balance = %.2f WHERE id = %d;"%(balance,user)
    self.cur.execute(update)
    self.db.commit()
  
  def get_status(self,id):
    select = "SELECT status FROM trade_data WHERE id = %d;"%id
    self.cur.execute(select)
    balance = self.cur.fetchall()
    return balance[0][0]
  def set_status(self,id,s):
    update = "UPDATE trade_data SET status = %d WHERE id = %d;"%(s,id)
    self.cur.execute(update)
    self.db.commit()
  
  def get_stock(self,id):
    select = "SELECT stock FROM item_data WHERE id = %d;"%id
    self.cur.execute(select)
    stock = self.cur.fetchall()
    return stock[0][0]

  def set_stock(self,id,s):
    update = "UPDATE item_data SET stock = %d WHERE id = %d;"%(s,id)
    self.cur.execute(update)
    self.db.commit()
  
  def query_delete(self,id):
    delete = "DELETE FROM trade_data WHERE id = %d"%id
    self.cur.execute(delete)
    self.db.commit()
  def get_name(self,id):
    select = "SELECT user_name FROM user_data WHERE id = %d;"%id
    self.cur.execute(select)
    name = self.cur.fetchall()
    if len(name)>0:
            return name[0][0]
    else:
            return "未知用户"

  def query_comment_insert(self, data):
        insert = """INSERT INTO comment (item_id,user_id,text)
        VALUES (%d ,%d,'%s');"""%(data[0],data[1],data[2])
        self.cur.execute(insert)
        self.db.commit()


  def create_comment_table(self):
        create ="""CREATE TABLE IF NOT EXISTS comment(
                    item_id SMALLINT UNSIGNED NOT NULL,
                    user_id SMALLINT UNSIGNED NOT NULL,
                    text VARCHAR(100) NOT NULL
                ) ENGINE = InnoDB;            
                """
        self.cur.execute(create)
