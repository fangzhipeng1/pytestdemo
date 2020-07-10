# coding = utf8

def test_one():
    assert 1 == 1
    assert 1 != 2
    assert "1" in "1,2,3"
    assert {"username":"fangzhipeng","password":"1234567"} == {"username":"fangzhipeng","password":"12345678"}
    a =34
    assert 20 < a < 45
    assert 1 < 2 == True


def f():
    return 3
def test_two():
    assert f() == 4