import pymysql
from sshtunnel import SSHTunnelForwarder
import os


class DbConnect():
    def __init__(self):
        self.tunnel = SSHTunnelForwarder(
                ('hk-test.showcard.vip', 22),  # 跳板机的ip、端口号
                ssh_username = "ubuntu",  # 跳板机的用户名
                ssh_pkey = os.path.join(os.path.dirname(os.path.realpath(__file__)), "hk-king-test.pem"),  # 密钥路径
                ssh_private_key_password = "123456",  # 跳板机的密码
                remote_bind_address=("hk-test.showcard.vip", 3306))
        self.tunnel.start()
        self.conn = pymysql.connect(host="127.0.0.1",  # host必须为127.0.0.1，代表本机(堡垒机)
                                   port=self.tunnel.local_bind_port,
                                   user="jiebin",  # 数据库的用户名
                                   passwd="123456",  # 数据库的密码
                                   db="ShopBack")  # 数据库名

        self.cursor = self.conn.cursor()

    def select(self, sql):
        '''查询语句'''
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


    def execute(self, sql):
        '''删除、修改、新增语句'''
        try:
            self.cursor.execute(sql) # 执行sql语句
            self.conn.commit() # 提交修改
        except:
            self.conn.rollback() # 发生错误时回滚


    def close(self):
        self.cursor.close()
        self.conn.close()

def delete_wish_list(user_id, product_id):
    '''数据库删除心愿单'''
    sql = "delete from wish_list where user_id = %s and product_id = %s" % (user_id, product_id)
    db = DbConnect()
    db.execute(sql)
    db.close()

def delete_card_apply(name, phone):
    '''数据库删除申请卡'''
    sql = "delete from vip_card_apply where name = %s and phone = %s" % (name, phone)
    db = DbConnect()
    db.execute(sql)
    db.close()

if __name__ == '__main__':
    db = DbConnect()
    result = db.select("select * from user where user_id = '8888'")
    print(result)
    delete_wish_list(user_id=10203, product_id=500001)