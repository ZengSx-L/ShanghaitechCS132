import MySQLdb
import gc
import globalData as gl


class MySQL_login:
  def __init__(self):
    self.db = MySQLdb.connect(host=gl.get_value("HOST"), user=gl.get_value("USER"),
    password=gl.get_value("PASSWORD"), db=gl.get_value("BD"),charset='utf8')
    self.cur = self.db.cursor()
    self.create_user_table()

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

  def close_connect(self):
    self.db.close()
    gc.collect()
  
  def query_insert(self, data):
    insert = "INSERT INTO user_data (name, user_name, email,telephone, passwd) VALUES (%s ,%s, %s, %s, %s);"
    self.cur.execute(insert, data)
    self.db.commit()

  def query_select_all(self):
    select_all = "SELECT * FROM user_data;"
    self.cur.execute(select_all)
    data = self.cur.fetchall()
    return data

  def query_select_current_user(self, data):
    select_user_data = "SELECT id, name, user_name,admin FROM user_data WHERE telephone IN('%s');" % data
    self.cur.execute(select_user_data)
    data = self.cur.fetchall()
    return data

  def query_check_user(self, data):
    select_user_telephone = "SELECT telephone FROM user_data WHERE telephone = '%s'" % data
    self.cur.execute(select_user_telephone)
    data = self.cur.fetchall()
    if not data:
      return True
    else:
      return False

  def query_select_login_passwd(self, telephone, password):
    select_phone = "SELECT telephone FROM user_data WHERE telephone = '%s';" % telephone
    self.cur.execute(select_phone)
    _telephone = self.cur.fetchall()
    select_passwd = "SELECT passwd FROM user_data WHERE passwd = '%s';" % password
    self.cur.execute(select_passwd)
    _password = self.cur.fetchall()
    try:
      if (str(telephone),) == _telephone[0]:
        if (str(password),) == _password[0]:
          return True
        else:
          return False
      else:
        return False
    except IndexError:
      pass

  def get_user(self,id):
    select_user = "SELECT user_name FROM user_data WHERE id = %d"%id
    self.cur.execute(select_user)
    data = self.cur.fetchall()
    return data