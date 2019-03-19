import configparser
import os

def read_conf():
    conf_path = os.path.abspath('.') #+ '/config/config.ini'
    print(conf_path)
    cf = configparser.ConfigParser()
    cf.read('E:\PycharmProjects\cre_api_test\config\config.ini')
    secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，
    print(secs)
    options = cf.options("web_url")  # 获取某个section名为Mysql-Database所对应的键
    print(options)
    items = cf.items("web_url")  # 获取section名为Mysql-Database所对应的全部键值对
    print(items)
    host = cf.get("web_url", "cas_url")  # 获取[Mysql-Database]中host对应的值
    print(host)
    return cf



if __name__ == '__main__':
    read_conf()
