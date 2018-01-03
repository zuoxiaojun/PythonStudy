# Author ='zuoxi'
#date =2018/1/3
counter = 0
while counter <3:
    _username = "zxj"
    _passwd  = "1234567"
    username = input("username :")
    passwd = input("passwad :")
    if username == _username and passwd ==_passwd:
        print("welcome %s login ! " %_username)
        break
    else:
        print("Invalid username or passwad!")
    counter += 1
    if counter ==3:
        keep_going_choice = input("还想玩么？【y/n】")
        if keep_going_choice == "y":
            counter =0
else:
    print("三次都错了，还试个毛线")
