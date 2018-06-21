import types
import functools

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        new_args=2*args[0]
        return func(new_args, **kwargs)
    return inner


def initialize_settings(arg):
    print(arg)
    return('Hello')

print(once(initialize_settings)(2))
print(initialize_settings(2))(2))
