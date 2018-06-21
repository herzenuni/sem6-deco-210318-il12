import functools

def once(func):
    result = 0;
    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal result
        print(inner.called, inner.deco)
        if not inner.called and not inner.deco:
          result = func(*args, **kwargs)
          inner.called = True
          return(func(*args, **kwargs))
        else:
          return(result)
    inner.called = False  
    inner.deco = False
    return inner

@once
def initialize_setting(txt):
  print("Settings initialized")
  return(txt)

print(initialize_setting(11))
print(initialize_setting(12))
