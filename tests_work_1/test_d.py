import pytest
from main_work_1 import delete_doc

PARAMETRS = [
    ("2207 876234", True),
    ("11-2", True)
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

@pytest.mark.parametrize("num_doc, bool_result", PARAMETRS)
def test_delete_doc(num_doc, bool_result):
    result = delete_doc(num_doc)
    assert bool_result in result