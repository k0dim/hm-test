import pytest
from main_work_3 import check_for_email


PARAMETR_1 = {
    ('konnov-di2015@yandex.ru','1',('ОШИБКИ НЕТ', 'ОШИБКА ЕСТЬ')),
    ('konnov-di2015@yandex.ru','',('ОШИБКИ НЕТ', 'ОШИБКА ЕСТЬ')),
    ('konnov-di2015@yandex.ru','QwdwDWewdw',('ОШИБКИ НЕТ', 'ОШИБКА ЕСТЬ'))
}

PARAMETR_2 = {
    ('111111','111111',('ОШИБКА ЕСТЬ')),
    ('konnov@yandex.ru','ededwdew',('ОШИБКА ЕСТЬ'))
}

@pytest.mark.parametrize("login, passw, response", PARAMETR_1)
def test_check_for_email_1(login, passw, response):
    result = check_for_email(login, passw)
    assert result["Логин"] == response[0] and result["Пароль"] == response[1]

@pytest.mark.parametrize("login, passw, response", PARAMETR_2)
def test_check_for_email_2(login, passw, response):
    result = check_for_email(login, passw)
    assert result["Логин"] == response[0]