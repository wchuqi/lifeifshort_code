import os
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')


def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')

test_iterator()

test_generator()

# initing iterator memory used: 6.6796875 MB
# after iterator initiated memory used: 3448.6953125 MB
# 4999999950000000
# after sum called memory used: 3877.38671875 MB
# initing generator memory used: 6.72265625 MB
# after generator initiated memory used: 6.72265625 MB
# 4999999950000000
# after sum called memory used: 6.7265625 MB

