# coding = utf-8

from datetime import datetime

with open("test.txt","w") as f:
    f.write("今天是")
    f.write(datetime.now().strftime('%y-%m-%d'))

with open("test.txt",'r') as f:
    s = f.read()
    print('oepn for read...')

with open("test.txt",'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)