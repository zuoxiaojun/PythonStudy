#由于dict也是一个集合，所以，遍历dict和遍历list类似，都可以通过 for 循环实现。
#直接使用for循环可以遍历 dict 的 key：

d ={
    'Adam':78,
    'Lisa':89,
    'Bart':90
}
for key in d:
   print(key +':',d[key])

