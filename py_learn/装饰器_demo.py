def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)

        return wrapper

    return my_decorator

@repeat(4)
def greet(message):
    print(message)

greet('hello world')
# 输出：
# wrapper of decorator
# hello world
# wrapper of decorator
# hello world
# wrapper of decorator
# hello world
# wrapper of decorator
# hello world

print(greet.__name__)
# wrapper
help(greet)
# Help on function wrapper in module __main__:
# wrapper(*args, **kwargs)

