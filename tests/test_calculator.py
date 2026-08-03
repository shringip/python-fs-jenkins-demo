import pytest
 
from app.calculator import add,substract,multiply,divison
 
@pytest.mark.smoke
def test_add():
    assert add(1,20)==21
 
def test_subtract():
    assert substract(20,10)==10
 
def test_multiply():
    assert multiply(4,4)==16

@pytest.mark.regression
def test_division():
    assert divison(20,5)==4

@pytest.mark.regression
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divison(10,0)
 
 