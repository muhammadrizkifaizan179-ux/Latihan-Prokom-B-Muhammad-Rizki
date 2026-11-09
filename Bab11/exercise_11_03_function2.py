from exercise_11_03_function import Employee


def test_give_default_raise():
    employee = Employee('Rizki', 'Faizan', 60000)
    employee.give_raise()
    assert employee.annual_salary == 65000


def test_give_custom_raise():
    employee = Employee('Rizki', 'Faizan', 60000)
    employee.give_raise(10000)
    assert employee.annual_salary == 70000