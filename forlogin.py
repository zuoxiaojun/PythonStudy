# Author ='zuoxi'
#date =2018/1/3

# for i in range(100):
#     if i< 50 or i > 70:
#         print(i)

_username = "zuoxiaojun"
_passwd  = "1234567"
for i in range (3):
    username = input("username :")
    passwd = input("passwad :")
    if username == _username:
        print("welcome %s login" %_username)
        break
    else:
        print("Invalid username or passwad!")