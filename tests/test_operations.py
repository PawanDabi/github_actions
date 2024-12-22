from src.math_operations import add,sub

def unit_test_add():
    assert add(5,6) == 11
    assert add(7,2) == 10, "check your parameters again"
    assert add(10,20) == 30

def unit_test_sub():
    assert add(5,6) == -1
    assert add(7,5) == 2
    assert add(10,10) == 0