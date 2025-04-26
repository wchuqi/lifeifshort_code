d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
print(d1 == d2 == d3 ==d4)
# True

s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)
# True

d = {'name': 'jason', 'age': 20}
print(d['name'])
# 'jason'

# d['location']
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# KeyError: 'location'

d = {'name': 'jason', 'age': 20}
print(d.get('name'))
# 'jason'
print(d.get('location', 'null'))
# 'null'

# s = {1, 2, 3}
# print(s[0])
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: 'set' object does not support indexing

s = {1, 2, 3}
print(1 in s)
# True
print(10 in s)
# False

d = {'name': 'jason', 'age': 20}
print('name' in d)
# True
print('location' in d)
# False

d = {'name': 'jason', 'age': 20}
d['gender'] = 'male' # 增加元素对'gender': 'male'
d['dob'] = '1999-02-01' # 增加元素对'dob': '1999-02-01'
print(d)
# {'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}
d['dob'] = '1998-01-01' # 更新键'dob'对应的值
d.pop('dob') # 删除键为'dob'的元素对
# '1998-01-01'
print(d)
# {'name': 'jason', 'age': 20, 'gender': 'male'}

s = {1, 2, 3}
s.add(4) # 增加元素 4 到集合
print(s)
# {1, 2, 3, 4}
s.remove(4) # 从集合中删除元素 4
print(s)
# {1, 2, 3}

d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序
print(d_sorted_by_key)
# [('a', 2), ('b', 1), ('c', 10)]
print(d_sorted_by_value)
# [('b', 1), ('a', 2), ('c', 10)]

s = {3, 4, 2, 1}
sorted(s) # 对集合的元素进行升序排序
print(s)
# [1, 2, 3, 4]

