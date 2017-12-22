#十位数循环从1至9，个位数循环从0至9。
for x in range(1,9):
    for y in range(x+1,10):
        print( str(x)+str(y))
