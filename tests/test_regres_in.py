import pytest
import pytest as pytest
from api import Reqres
from settings import *
from conftest import *

reg = Reqres()

test_data_test_1 = (
    pytest.param(-255, -255, 404, id="get_list_of_users__param_1"),#'''the system returns the status code 200 which means a bag''
    pytest.param(-255, -1, 404, id="get_list_of_users__param_2"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(-255, 0, 404, id="get_list_of_users__param_3"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(-255, 1, 404, id="get_list_of_users__param_4"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(-255, 255, 404, id="get_list_of_users__param_5"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(-1, -1, 404, id="get_list_of_users__param_6"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(-1, 0, 404, id="get_list_of_users__param_7"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(-1, 1, 404, id="get_list_of_users__param_8"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(-1, 255, 404, id="get_list_of_users__param_9"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(-1, -255, 404, id="get_list_of_users__param_10"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(0, 0, 200, id="get_list_of_users__param_11"),
    pytest.param(0, 1, 200,id="get_list_of_users__param_12"),
    pytest.param(0, 255, 200, id="get_list_of_users__param_13"),
    pytest.param(0, -255, 404, id="get_list_of_users__param_14"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(0, -1, 404, id="get_list_of_users__param_15"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(1, 1, 200, id="get_list_of_users__param_16"),
    pytest.param(1, 255, 200, id="get_list_of_users__param_17"),
    pytest.param(1, -255, 404, id="get_list_of_users__param_18"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(1, -1, 404, id="get_list_of_users__param_19"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(1, 0, 200, id="get_list_of_users__param_20"),
    pytest.param(255, 255, 200, id="get_list_of_users__param_21"),
    pytest.param(255,-255, 404, id="get_list_of_users__param_22"), #'''the system returns the status code 200 which means a bag'''
    pytest.param(255, -1, 404, id="get_list_of_users__param_23"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(255, 0, 200, id="get_list_of_users__param_24"),
    pytest.param(255, 1, 200, id="get_list_of_users__param_25"),
    pytest.param('','' , 404, id="get_list_of_users__param_26"),#'''the system returns the status code 200 which means a bag'''
    pytest.param('', 1, 404, id="get_list_of_users__param_27"),#'''the system returns the status code 200 which means a bag'''
    pytest.param(2, '', 404, id="get_list_of_users__param_28"))#'''the system returns the status code 200 which means a bag'''


@pytest.mark.positive_and_negative_tests
@pytest.mark.parametrize("page, per_page, status_code", test_data_test_1)
def test_get_list_of_users(page, per_page, status_code):
    actual_status, result = reg.get_list_of_users(page=page, per_page=per_page)
    assert actual_status == status_code

test_data_test_1 = (
    pytest.param('api/users?page=2', 200, id="param_1"),
    pytest.param('api/users/2', 200, id="param_2"),
    pytest.param('api/users/23', 404, id="param_3")
)

@pytest.mark.positive_test
def test_get_single_user():
    status, result = reg.get_single_user()
    assert status == 200

@pytest.mark.negative_test
def test_get_single_user_negative():
    status, result = reg.get_single_user_not_found()
    assert status == 404

@pytest.mark.positive_test
def test_get_resource_list():
    page = 2
    per_page = 4
    status, result = reg.fetch_resource_list(page, per_page)
    assert status == 200

@pytest.mark.positive_test
def test_get_single_resource():
   id = 2
   status, result = reg.fetch_single_resource(id)
   assert status == 200


@pytest.mark.positive_test
def test_post_new_user():
    name = "Ivan"
    job = "Driver"
    status, result = reg.create_user(name, job)
    assert status == 201

@pytest.mark.positive_test
def test_put_user(create_user):
    new_status, new_result = reg.put_user(create_user)
    assert new_status == 200

@pytest.mark.positive_test
def test_delete_user(create_user):
    test_user_id = reg.create_user(name = "Elena", job = "Waiter")
    new_status, new_result = reg.delete_user(user_id=test_user_id)
    assert new_status == 204


