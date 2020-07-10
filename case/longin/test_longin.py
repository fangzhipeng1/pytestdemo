# coding = utf-8

import pytest

'''
test
'''
def add(a, b):
    return a+b

def test_add():
    assert add(1, 2) == 4

def test_add2():
    assert add(2, 4) == 5

if __name__ == '__main__':

    pytest.main()