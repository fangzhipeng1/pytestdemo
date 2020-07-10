# coding = utf8

'''
初始化，
'''

import pytest


def setup_module():
    print('整个模块.py开始')


def teardown_module():
    print('整个模块.py结束')


def setup_function():
    print('不在类中的函数前')


def teardown_function():
    print('不在类中的函数后')


def test_w_one():
    print("不在类中的方法1")


def test_w_two():
    print('不在类中的方法2function')


class TestClass:
    def setup_class(self):
        print('类前')

    def teardown_class(self):
        print('类后')

    def setup_method(self):
        print('方法前')

    def teardown_method(self):
        print('方法后')

    def test_one(self):
        x = "this"
        assert "5" in x

    def test_two(self):
        x = "hello"
        assert "hello" == x

    def test_three(self):
        a = "hello"
        b = "hello worold"
        assert a in b


if __name__ == '__main__':
    pytest.main(["-s", "test_set.py"])
