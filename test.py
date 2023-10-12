import pytest
from main import Person

@pytest.fixture()
def test_val():
	return Person("Sider",25,"India")

def test_name_printer(test_val):
	assert test_val.name=="Sider"

def test_age_printer(test_val):
	assert test_val.age==25
