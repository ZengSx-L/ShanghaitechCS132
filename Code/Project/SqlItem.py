import MySQLdb
import gc
import globalData as gl

class MySQL_Item:
    def __init__(self):
        self.db = MySQLdb.connect(host=gl.get_value("HOST"), user=gl.get_value("USER"),
        password=gl.get_value("PASSWORD"), db=gl.get_value("BD")
        ,charset='utf8')
        self.cur = self.db.cursor()
        self.create_table()
        self.create_comment_table()
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
    def query_insert(self, data):
        insert = """INSERT INTO item_data (item_name,seller_id,price,stock,intro, img_name,tag)
        VALUES ('%s',%d, %.2f, %d,'%s','%s', %d);"""%(data[0],data[1],data[2],data[3],data[4],data[5],data[6])
        #print(insert)
        self.cur.execute(insert)
        self.db.commit()

    def query_select_all(self):
        select_all = "SELECT * FROM item_data;"
        self.cur.execute(select_all)
        data = self.cur.fetchall()
        return data

    def query_select_page(self,index):
        start = index * 4
        end = start + 4
        '''
        seller = gl.get_value("user_id")
        if gl.get_value("admin") == 1:
            select_all = "SELECT * FROM item_data LIMIT %d,%d;"%(start,end)
        else:
            select_all = "SELECT * FROM item_data WHERE seller_id <> %d LIMIT %d,%d;"%(seller,start,end)
        '''
        select_all = "SELECT * FROM item_data LIMIT %d,%d;"%(start,end)
        self.cur.execute(select_all)
        data = self.cur.fetchall()
        return data

    def query_select_tag(self,tag,index):
        start = index * 4
        end = start + 4
        '''
        seller = gl.get_value("user_id")
        if gl.get_value("admin") == 1:
            select_all = "SELECT * FROM item_data WHERE tag = %d LIMIT %d,%d;"%(tag,start,end)
        else:
            select_all = "SELECT * FROM item_data WHERE tag = %d AND seller_id <> %d LIMIT %d,%d;"%(tag,seller,start,end)
        '''
        select_all = "SELECT * FROM item_data WHERE tag = %d LIMIT %d,%d;"%(tag,start,end)
        self.cur.execute(select_all)
        data = self.cur.fetchall()
        return data

    def query_search_name(self,data,index):
        start = index * 4
        end = start + 4
        name = '%'+data+'%'
        '''
        seller = gl.get_value("user_id")
        if gl.get_value("admin") == 1:
            select_all = "SELECT * FROM item_data WHERE item_name LIKE '%s' LIMIT %d,%d;"%(name,start,end)
        else:
            select_all = "SELECT * FROM item_data WHERE item_name LIKE '%s' AND seller_id <> %d LIMIT %d,%d;"%(name,seller,start,end)
        '''
        select_all = "SELECT * FROM item_data WHERE item_name LIKE '%s' LIMIT %d,%d;"%(name,start,end)
        self.cur.execute(select_all)
        data = self.cur.fetchall()
        return data
  
    def query_all(self,index,tag,data):
        start = index * 4
        end = start + 4
        name = '%'+data+'%'
        '''
        seller = gl.get_value("user_id")
        if gl.get_value("admin") == 1:
            select_all = "SELECT * FROM item_data WHERE tag = %d AND item_name LIKE  '%s' LIMIT %d,%d;"%(tag, name, start, end)
        else:
            select_all = "SELECT * FROM item_data WHERE tag = %d AND item_name LIKE  '%s' AND seller_id <> %d LIMIT %d,%d;"%(tag, name, seller, start, end)
        '''
        select_all = "SELECT * FROM item_data WHERE tag = %d AND item_name LIKE  '%s' LIMIT %d,%d;"%(tag, name, start, end)
        self.cur.execute(select_all)
        data = self.cur.fetchall()
        return data

    def get_item(self,id):
        select_item = "SELECT item_name FROM item_data WHERE id = %d"%id
        self.cur.execute(select_item)
        data = self.cur.fetchall()
        if len(data)>0:
            return data[0][0]
        else:
            return "商品已下架"
    def get_self_item(self,id,index):
        start = index * 4
        end = start + 4
        select_item = "SELECT * FROM item_data WHERE seller_id = %d LIMIT %d,%d"%(id,start,end)
        self.cur.execute(select_item)
        data = self.cur.fetchall()
        return data

    def get_all_item(self,index):
        start = index * 4
        end = start + 4
        select_item = "SELECT * FROM item_data LIMIT %d,%d"%(start,end)
        self.cur.execute(select_item)
        data = self.cur.fetchall()
        return data
    
    def update_item(self,data,curr_item):
        newdata = """UPDATE item_data SET item_name='%s', seller_id=%d, price=%.2f, stock=%d, intro='%s', img_name='%s', tag=%d WHERE id = %d;"""%(data[0],data[1],data[2],data[3],data[4],data[5],data[6],curr_item)
        self.cur.execute(newdata)
        self.db.commit()

    def delete_item(self,curr_item):
        sql = "DELETE FROM item_data WHERE id = %d;"%curr_item
        self.cur.execute(sql)
        self.db.commit()
        
        #self.cur.close()
        #self.db.close()
    
    def create_comment_table(self):
        create ="""CREATE TABLE IF NOT EXISTS comment(
                    item_id SMALLINT UNSIGNED NOT NULL,
                    user_id SMALLINT UNSIGNED NOT NULL,
                    text VARCHAR(100) NOT NULL
                ) ENGINE = InnoDB;            
                """
        self.cur.execute(create)

    def query_comment_insert(self, data):
        insert = """INSERT INTO comment (item_id,user_id,text)
        VALUES (%d ,%d,'%s');"""%(data[0],data[1],data[2])
        self.cur.execute(insert)
        self.db.commit()

    def query_select_comment(self,item):
        select = "SELECT * FROM comment WHERE item_id = %d;"%item
        self.cur.execute(select)
        data = self.cur.fetchall()
        return data