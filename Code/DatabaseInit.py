import MySQLdb
import gc

HOST, USER, PASSWORD, BD = "localhost", "testusr", "test123", "TESTDB"

class MySQL:
  def __init__(self):
    self.db = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD, db=BD,charset='utf8')
    self.cur = self.db.cursor()
    self.create_user_table()
    self.create_table()

  def create_user_table(self):
    create ="""CREATE TABLE IF NOT EXISTS user_data (
                id SMALLINT UNSIGNED NOT NULL auto_increment,
                name VARCHAR(20) NOT NULL,
                user_name VARCHAR(20) NOT NULL,
                email VARCHAR(20) NOT NULL,
                telephone VARCHAR(20) NOT NULL,
                passwd VARCHAR(20) NOT NULL,
                balance DECIMAL(8,2) UNSIGNED DEFAULT 200.00,
                admin TINYINT DEFAULT 0,
                primary key (id)
            ) ENGINE = InnoDB;            
            """
    self.cur.execute(create)
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
        self.cur.execute(create)
  def close_connect(self):
    self.db.close()
    gc.collect()
  def admin(self,cmd):
    self.cur.execute(cmd)
    self.db.commit()
  def query_insert(self, data):
    insert = "INSERT INTO user_data (name, user_name, email,telephone, passwd) VALUES (%s ,%s, %s, %s, %s);"
    self.cur.execute(insert, data)
    self.db.commit()

  def query_insert_item(self, data):
        insert = """INSERT INTO item_data (item_name,seller_id,price,stock,intro, img_name,tag)
        VALUES ('%s',%d, %.2f, %d,'%s','%s', %d);"""%(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
        #print(insert)
        self.cur.execute(insert)
        self.db.commit()
  def get_id(self,name):
    select = "SELECT id FROM user_data WHERE name = '%s';"%name
    self.cur.execute(select)
    name = self.cur.fetchall()
    if len(name)>0:
            return name[0][0]
    else:
            return 1
sql = MySQL()
usr1 = ["Alice","Alice","email1","123456","123"]
usr2 = ["Bob","Bob","email2","456789","456"]
admin = "INSERT INTO user_data (name, user_name, email,telephone, passwd,admin) VALUES ('admin' ,'admin', 'admin', '233333','233',1);"

itemname = ["毛巾","剪刀","牙刷","衬衫（深蓝）","T恤（浅灰）","运动裤（墨绿）","乐事薯片","日式小圆饼","喜之郎果冻","休闲长裤（浅灰）"]
img = ["1640660600.jpg","1640660663.jpg","1640660666.jpg","1640660669.jpg","1640660701.jpg","1640660702.jpg",
"1640660703.jpg","1640660752.jpg","1640660764.jpg","1640660769.jpg"]

price = [20.00,10.00,5.00,30.00,35.00,40.00,20.00,25.00,15.00,30.00]
stock = [5,3,10,1,5,3,15,10,20,1]
intro = ["日用毛巾，几乎全新，无污点无异味。","小剪刀，使用时间不到一周，挺好用的。","真·全新牙刷。当时成套买的用不完了，大家想要的收一下吧。","衬衫买大了，175的，基本上没穿过。半价转了吧。","宽松T恤，面料舒适，欲购从速!","潮流运动裤（男），全新半价，中国人不骗中国人",
        "乐事薯片（未拆封）。准备减肥了，含泪转手。","日式小圆饼，原装进口，原价一袋70，好吃的一。","喜之郎果冻，绝对正版。","休闲长裤，无脏污，穿了两次。有点小掉色，问题不大。"]
tag = [2,2,2,1,1,1,0,0,0,1]
sql.query_insert(usr1)
sql.query_insert(usr2)
sql.admin(admin)

id1 = sql.get_id("Alice")
id2 = sql.get_id("Bob")
seller = [id1,id2]*5

for i in range(10):
  data = [itemname[i],seller[i],price[i],stock[i],intro[i],img[i],tag[i]]
  print(data)
  sql.query_insert_item(data)
sql.close_connect()
