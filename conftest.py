import pytest
from api import Reqres
reg = Reqres()

@pytest.fixture
def create_user():
    status, result = reg.create_user("tets", "job")
    return result["id"]