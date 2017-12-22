#if-elif-else
# #如果按照分数划定结果：
#  90分或以上：excellent
# 80分或以上：good
#  60分或以上：passed
#  60分以下：failed
# 请编写程序根据分数打印结果。

score = int(input('input your score:'))
if score >= 90:
    print('excellent')
elif score >=80:
    print("good")
elif score >= 60:
    print('passed')
else:
    print('failed')
print('End')
