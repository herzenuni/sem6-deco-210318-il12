import hashlib
import functools

@functools.singledispatch
def hash(arg):
    type_name = type(arg).__name__
    assert False, "Unsupported object type : " + type_name

@hash.register(str)
def _(arg):
    sha = hashlib.sha1(bytes(arg,'utf-8')).hexdigest()
    return sha


@hash.register(list)
def _(arg):
    result = type(arg)()
    for i in arg:
        result.append(hashlib.sha1(bytes(i,'utf-8')).hexdigest())
    return result

@hash.register(tuple)
def _(arg):
    result = []
    for i in arg:
        result.append(hashlib.sha1(bytes(i,'utf-8')).hexdigest())
    return tuple(result)

@hash.register(set)
def _(arg):
    result = type(arg)()
    for i in arg:
        result.add(hashlib.sha1(bytes(i,'utf-8')).hexdigest())
    return result


@hash.register(dict)
def _(arg):
    keys = arg.keys()
    values = []
    for i in arg.values():
        values.append(hashlib.sha1(bytes(i,'utf-8')).hexdigest())
    result = dict.fromkeys(keys,None)
    result.update(zip(keys,values))
    return result


class TestInit:

    def test_hash(self):
        assert(hash({'Hello','world'})=={'f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0', '7c211433f02071597741e6ff5a8ea34789abbf43'})

    def test_hash_str(self):
        assert(hash('Hello')=='f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0')

