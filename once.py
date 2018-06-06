import functools

def once(func):

    @functools.wraps(func)
    def inner(*args, **kwargs):
        if deco == True:
            return func(*args, **kwargs)
        if not inner.called:
            inner.called = True
            return func(*args, **kwargs)
    inner.called = False
    return inner

@once
def initialize_settings(txt):
    print("Settings initialized")
    return(txt)

print(initialize_settings())
