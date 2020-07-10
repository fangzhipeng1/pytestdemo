# coding : utf-8
'''
1.os模块：os模块在python中包含普遍的操作系统功能，下面列出了一些在os模块中比较有用的部分。

os.sep可以取代操作系统特定的路径分隔符。windows下为 “\\”

os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。

os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。

os.getenv()获取一个环境变量，如果没有返回none

os.putenv(key, value)设置一个环境变量值

os.listdir(path)返回指定目录下的所有文件和目录名。

os.remove(path)函数用来删除一个文件。

os.system(command)函数用来运行shell命令。

os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。

os.curdir:返回当前目录（'.')
os.chdir(dirname):改变工作目录到dirname

========================================================================================

os.path常用方法：

os.getcwd() 获取当前工作目录，即当前python脚本工作的目录路径

os.chdir("dirname")  改变当前脚本工作目录；相当于shell下cd

os.curdir  返回当前目录: ('.')

os.pardir  获取当前目录的父目录字符串名：('..')

os.makedirs('dirname1/dirname2')    可生成多层递归目录

os.removedirs('dirname1')    若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推

os.mkdir('dirname')    生成单级目录；相当于shell中mkdir dirname

os.rmdir('dirname')    删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname

os.listdir('dirname')    列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

os.remove()  删除一个文件

os.rename("oldname","newname")  重命名文件/目录

os.stat('path/filename')  获取文件/目录信息

os.sep    输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"

os.linesep    输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"

os.pathsep    输出用于分割文件路径的字符串 win下为;,Linux下为:

os.name    输出字符串指示当前使用平台。win->'nt'; Linux->'posix'

os.system("bash command")  运行shell命令，直接显示

os.environ  获取系统环境变量

os.path.abspath(path)  返回path规范化的绝对路径

os.path.split(path)  将path分割成目录和文件名二元组返回

os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素

os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素

os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False

os.path.isabs(path)  如果path是绝对路径，返回True

os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False

os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False

os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略

os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间

os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间

os.path.getsize(path) 返回path的大小

os.path.normpath(os.path.join(os.path.abspath(__file__),'..','..','..'))表示返回当前文件的上上上层目录
'''
from datetime import datetime
import os
import configparser
import yaml
pwd = os.path.abspath('../case/set')  # 获取当前目录绝对路径

print('   Size  Last Modified Name')
print('------------------------------')

# for f in os.listdir(pwd):
#     # print(f)
#     fsize = os.path.getsize(f)
#     mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     flag = '/' if os.path.isdir(f) else''
#     print('%10d %s %s%s' % (fsize, mtime, f, flag))
#
# cwd = os.getcwd() # 获取当前目录完整路径
# print(cwd)

b = os.listdir(os.getcwd())  # 返回指定目录下的所有文件和目录名(包括隐藏文件)
#print(b)
def get_file_path():
    d = list()
    for i in b:
        c = os.path.join(os.getcwd(),i)
        d.append(c)
    return d

file_path = get_file_path()
# q = r"D:\pytestdemo\case\set\test.txt"
# print(file_path.index(q))
# print(file_path)

# os.rename("oldname","newname") 更改文件名称
# os.rename("test.txt","test2.txt")


'''
读取config 目录下config.ini 配置文件



file = r'..\case\config\config.ini'
con = configparser.ConfigParser()
con.read(file, encoding='utf-8')
sections = con.sections()
items = con.items('user')
items = dict(items)
print(items['username'])
'''
# 获得配置文件的方法
# 需要传入2个参数，第一个是ini 文件section的名称，第二个是内容的key值
def get_conf_value(sectionname,key):
    try:
        file = r'../case/config/config.ini'
        con =configparser.ConfigParser()    # 创建配置文件对象
        con.read(file, encoding='utf-8')    # 读取配置文件
        sections = con.sections()           # 获取所有section
        # items = con.items(sectionname)      # 获取指定的section 名称的内容
        # items = dict(items)                 # 转成字典
        # return items[key]                   # 取值
        value = con.get(sectionname, key)   # 取值
        return value
    except Exception as e:
        print(e)

con = configparser.ConfigParser()
con.read(r'../case/config/config.ini', encoding= 'utf-8')
sections = con.sections()
value2 = con.get('user', 'username')
print(value2)


def get_yaml_value():
    file = r'../case/config/config.yaml'
    with open(file, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)
if __name__ == '__main__':
    value = get_conf_value('user', 'password')
    value3 = get_yaml_value()
    print(value3['my']["name"])             # 获得某个值
    for i in value3:
        print(i)
    assert value3['my']["name"] == 'fangzhipeng1'


# http://nodeca.github.io/js-yaml/
# a=os.environ.get()
# def get_config():
#     for key in a:
#         print(key + ':' + a[key])

