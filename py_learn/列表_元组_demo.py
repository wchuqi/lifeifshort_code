l = [1, 2, 'hello', 'world'] # 列表中同时含有 int 和 string 类型的元素
print(l)
# [1, 2, 'hello', 'world']

tup = ('jason', 22) # 元组中同时含有 int 和 string 类型的元素
print(tup)
# ('jason', 22)

l = [1, 2, 3, 4]
l[3] = 40 # 和很多语言类似，python 中索引同样从 0 开始，l[3] 表示访问列表的第四个元素
print(l)
# [1, 2, 3, 40]

tup = (1, 2, 3, 4)
#tup[3] = 40
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment

tup = (1, 2, 3, 4)
new_tup = tup + (5, ) # 创建新的元组 new_tup，并依次填充原元组的值
print(new_tup)
# (1, 2, 3, 4, 5)

l = [1, 2, 3, 4]
l.append(5) # 添加元素 5 到原列表的末尾
print(l)
# [1, 2, 3, 4, 5]

l = [1, 2, 3, 4]
print(l[-1])
# 4

tup = (1, 2, 3, 4)
print(tup[-1])
# 4

l = [1, 2, 3, 4]
print(l[1:3]) # 返回列表中索引从 1 到 2 的子列表
# [2, 3]

tup = (1, 2, 3, 4)
print(tup[1:3]) # 返回元组中索引从 1 到 2 的子元组
# (2, 3)

l = [[1, 2, 3], [4, 5]] # 列表的每一个元素也是一个列表
tup = ((1, 2, 3), (4, 5, 6)) # 元组的每一个元素也是一元组

print(list((1, 2, 3)))
# [1, 2, 3]
print(tuple([1, 2, 3]))
# (1, 2, 3)

# 列表和元组常用的内置函数
l = [3, 2, 3, 7, 8, 1]
print(l.count(3))
# 2
print(l.index(7))
# 3
l.reverse()
print(l)
# [1, 8, 7, 3, 2, 3]
l.sort()
print(l)
# [1, 2, 3, 3, 7, 8]

tup = (3, 2, 3, 7, 8, 1)
print(tup.count(3))
# 2
print(tup.index(7))
# 3
print(list(reversed(tup)))
# [1, 8, 7, 3, 2, 3]
print(sorted(tup))
# [1, 2, 3, 3, 7, 8]

l = [1, 2, 3]
print(l.__sizeof__())
# 104
tup = (1, 2, 3)
print(tup.__sizeof__())
# 48

l = []
print(l.__sizeof__()) # 空列表的存储空间为 40 字节
# 40
l.append(1)
print(l.__sizeof__())
# 72 加入了元素 1 之后，列表为其分配了可以存储 4 个元素的空间 (72 - 40)/8 = 4
l.append(2)
print(l.__sizeof__())
# 72 由于之前分配了空间，所以加入元素 2，列表空间不变
l.append(3)
print(l.__sizeof__())
# 72 同上
l.append(4)
print(l.__sizeof__())
# 72 同上
l.append(5)
print(l.__sizeof__())
# 104 加入元素 5 之后，列表的空间不足，所以又额外分配了可以存储 4 个元素的空间

l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2
print(id(l1))
print(id(l2))
print(id(l3))