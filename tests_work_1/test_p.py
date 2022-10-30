import pytest
from main_work_1 import get_doc_owner_name

PARAMETRS = [
    ('2207 876234'),
    ('11-2'),
    ('10006')
]

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

def get_name(documents):
    list_name = []
    for i in documents:
        list_name.append(i["name"])
    return list_name

@pytest.mark.parametrize("num_doc", PARAMETRS)
def test_get_doc_owner_name(num_doc):
    assert get_doc_owner_name(num_doc) in get_name(documents)