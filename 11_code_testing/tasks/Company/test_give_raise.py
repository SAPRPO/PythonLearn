
from employee import Employee

#no fixture
def test_give_default_raise():
    t_emp = Employee('Petr', 'Petrov', 80000)
    t_emp.give_raise()
    assert t_emp.salary_year == 85000

def test_give_custom_raise():
    t_emp = Employee('Petr', 'Petrov', 80000)
    t_emp.give_raise(8000)
    assert t_emp.salary_year == 88000

