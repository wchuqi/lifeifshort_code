'''
问题：给定两个序列，判定第一个是不是第二个的子序列。
（LeetCode 链接如下：https://leetcode.com/problems/is-subsequence/ ）
'''


def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)

# print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
# print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))
########## 输出 ##########
# True
# False

def is_subsequence1(a, b):
    b = iter(b)
    print(b)

    gen = (i for i in a)
    print(gen)

    for i in gen:
        print(i)

    gen = ((i in b) for i in a)
    print(gen)

    for i in gen:
        print("," + str(i))

    for i in gen:
        print(",," + str(i))
    # return all(((i in b) for i in a))
    return all(gen)


print(is_subsequence1([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence1([1, 4, 3], [1, 2, 3, 4, 5]))

########## 输出 ##########
