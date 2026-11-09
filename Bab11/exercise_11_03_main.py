import pytest
from exercise_11_03_function2 import Employee


@pytest.fixture
def employee():
    return Employee('Rizki', 'Faizan', 60000)


def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 65000


def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 70000