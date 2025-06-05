
import pytest
from employee import Employee

@pytest.fixture
def setUp():
    setUp = Employee('Petr', 'Petrov', 80000)
    return setUp

def test_give_default_raise(setUp): 
    setUp.give_raise()
    assert setUp.salary_year == 85000

def test_give_custom_raise(setUp):
    setUp.give_raise(8000)
    assert setUp.salary_year == 88000

