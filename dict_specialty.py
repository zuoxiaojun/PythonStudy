# 请设计一个dict，可以根据分数来查找名字，已知成绩如下：
# Adam: 95,
# Lisa: 85,
# Bart: 59.

d = {
    95:'Adam',
    85:'Lisa',
    81:'Bart',
    86:'Lrisa'
}
a = input("input score:")
print(d.get(int(a)))   # a 默认应该是str型，故用int函数转换一下
