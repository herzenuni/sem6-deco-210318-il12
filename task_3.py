import functools
import pytest

def once(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        new_args=2*args[0]
        return func(new_args, **kwargs)
    return inner


def initialize_settings(arg):
    return(arg)


class TestInit:
    def test_init(self):
        assert(once(initialize_settings)(2)==4)

    def test_second_init(self):
        assert(initialize_settings(2)==2)
