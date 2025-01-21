import mysql.connector
import os


class ConfigDao:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='configurator',
                                           # Mysql账号的密码保存在环境变量中
                                           password=os.getenv(
                                               "MYSQL_CONFIG_PWD"),
                                           host='127.0.0.1',
                                           database='config_database')

    def get_https_proxy_config(self):
        query_sql = 'select * from config_table where name = "proxy_https"'
        cursor = self.cnx.cursor()
        cursor.execute(query_sql)
        for _, name, content in cursor:
            cursor.close()
            return content
        cursor.close()


def main():
    dao = ConfigDao()
    print(dao.get_https_proxy_config())


if __name__ == '__main__':
    main()
