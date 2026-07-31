import pytest
 
from app.employee_service import EmployeeServcie
 
service=EmployeeServcie()
 
def test_calculate_annual_salary():
    result=service.calculate_annual_salary(50_000)
    assert result==600_000
 
def test_calcualte_bonus():
    result=service.calculate_bonus(50_000,10)
    assert result==5_000
 
def test_invalid_salary():
    with pytest.raises(ValueError,match="monthly salary must be greater than 0"):
        service.calculate_annual_salary(-10_1000)
 
@pytest.mark.parametrize(
    "employee_id,expected_result",
    [
        (101,True),
        (1,True),
        (0,False),
        (-10,False),
        ("EMP101",False),
    ],
)
 
def test_validate_employee(employee_id,expected_result):
    assert  service.validate_employee(employee_id)==expected_result
 