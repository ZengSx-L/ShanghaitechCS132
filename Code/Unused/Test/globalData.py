def _init():
    """ 初始化 """

    global _global_dict
    _global_dict = {}
#HOST, USER, PASSWORD, BD = "localhost", "testusr", "test123", "TESTDB"
    set_value("HOST","localhost")
    set_value("USER","testusr")
    set_value("PASSWORD","test123")
    set_value("BD","TESTDB")


def set_value(key,value):
    """ 定义一个全局变量 """

    _global_dict[key] = value


def get_value(key,defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """

    try:
        return _global_dict[key]
    except KeyError:  # 查找字典的key不存在的时候触发
        return defValue