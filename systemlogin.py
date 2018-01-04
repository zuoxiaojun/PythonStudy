# Author ='zuoxi'
#date =2018/1/4
counter = 0
while counter<3 :
    _username = "zxj"
    _passwd = "1234567"

    username = input("username : ")
    passwd   = input("password: ")
    if username ==_username and passwd ==_passwd:
        print ("login successful,welcome %s" %_username)
    else:
        print("Invalid username or passwd")
    counter += 1
    if counter == 3:
        keep_going_chonce=input("play again? [y/n]:")
        if keep_going_chonce=="y":
            counter = 0
else:
    print("bye bye")