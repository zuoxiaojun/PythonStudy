#利用while循环计算100以内奇数的和。
sum = 0
x = 1
while x <= 100:
    sum = sum + x
    x = x + 2
print ('100以内奇数求和为：'+str(sum))