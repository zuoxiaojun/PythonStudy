# Author ='zuoxi'
#date =2018/1/3
name = input("name is : ")
age = input("age is : ")
job = input("job is : ")
salary = input("salary is : ")
if salary.isdigit():#长得像不像数字，比如200D，'200'
    salary = int(salary)
else:
    print("must input digit!")
    exit("must input digit!")

msg = '''
----info of %s-----
name : %s
age  : %s
job  : %s
salary : %f
-----end------
''' % (name, name , age ,job ,salary )
print(msg)

#z字符格式化输出
#占位符  %S  s = string
#       %d  d = diggit  整数
#       %f = float 浮点数

