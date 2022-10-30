import pytest
from main_work_2 import Yandex, get_token

PARAMETRS_201 = [
    ('Моя папка 1', 201),
    ('Моя папка 2', 201),
    ('Моя папка 3', 201),
    ('Моя папка 4', 201)
]

PARAMETRS_401 = [
    ('Дубль', 201),
    ('Дубль', 409),
    ('Дубль', 409),
    ('Дубль', 409)
]


@pytest.mark.parametrize("name_folder, code_resonse", PARAMETRS_201)
@pytest.fixture()
def resourse_setup(request, name_folder, code_resonse):
    def resourse_teardown():
        ya_test = Yandex(get_token())
        ya_test.delete_folder(name_folder)
    request.addfinalizer(resourse_teardown)

@pytest.mark.parametrize("name_folder, code_resonse", PARAMETRS_201)
def test_201_creat_folder(resourse_setup, name_folder, code_resonse):
    ya_test = Yandex(get_token())
    result = ya_test.creat_folder(name_folder)
    assert result == code_resonse

@pytest.mark.parametrize("name_folder, code_resonse", PARAMETRS_401)
def test_401_creat_folder(resourse_setup, name_folder, code_resonse):
    ya_test = Yandex(get_token())
    result = ya_test.creat_folder(name_folder)
    assert result == code_resonse

