# Author ='zuoxi'
#date =2018/1/3

_user = "zuoxiaojun"
_passwd = "abc123"
for i in range(3):
    username = input("Username : ")
    passwd = input("passwd : ")
    if username == _user and passwd ==_passwd :
        print("Welcome %s login......" %_user)
        break   #跳出，中断
    else:
        print("Invalid username or passwd!")
