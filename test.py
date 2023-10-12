import pytest
from main import data

@pytest.fixture()
def test_val():
	return data("Sider",25,"India")

def name_printer(test_val):
	assert test_val.name=="Sider"

def age_printer(test_val):
	assert test_val.age==25
