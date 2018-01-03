# Author ='zuoxi'
#date =2018/1/3

_user = "zuoxiaojun"
_passwd = "abc123"
username = input("Username : ")
passwd = input("passwd : ")
if username == _user and passwd ==_passwd :
    print("Welcome %s login......" %_user)
else:
    print("Invalid username or passwd!")
    