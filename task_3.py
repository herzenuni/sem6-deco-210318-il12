import types
import functools
def copy_func(f):
    g = types.FunctionType(
      f.__code__, 
      f.__globals__, 
      argdefs=f.__defaults__, 
      closure=f.__closure__
    )
    g.__kwdefaults__ = f.__kwdefaults__
    return g

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
