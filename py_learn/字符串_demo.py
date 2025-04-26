# 3种写法
name = 'jason'
city = 'beijing'
text = "welcome to jike shijian"

s1 = 'hello'
s2 = "hello"
s3 = """hello"""
print(s1 == s2 == s3)
# True

s = 'a\nb\tc'
print(s)
print(len(s)) # 5

name = 'jason'
print(name[0])
# 'j'
print(name[1:3])
# 'as'

# 遍历字符串
for char in name:
    print(char)

# 把'hello'的第一个字符'h'，改为大写的'H'
s = 'H' + s[1:]
s = s.replace('h', 'H')

# 格式化
print('%s' % 'a')
print("%s %s" % ('a', 'b'))

a = 'a1a'
b = 'b2b'
c = 'Abc'
print('{} {}'.format('a', 'b'))
print('{} {a}'.format('aa', a=a))

print(f'{a}, {c}')
print(F'{a}, {c}')