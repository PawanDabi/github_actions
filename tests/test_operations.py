from src.math_operations import add,sub

def test_add():
    assert add(5,6) == 11
    assert add(7,2) == 9
    assert add(10,20) == 30

def test_sub():
    assert sub(5,6) == -1
    assert sub(7,5) == 2
    assert sub(10,10) == 0