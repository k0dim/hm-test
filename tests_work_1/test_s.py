import pytest
from main_work_1 import get_doc_shelf

PARAMETRS = [
    ('2207 876234'),
    ('11-2'),
    ('10006')
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

@pytest.mark.parametrize("num_doc", PARAMETRS)
def test_get_doc_shelf(num_doc):
    assert get_doc_shelf(num_doc) in directories.keys()