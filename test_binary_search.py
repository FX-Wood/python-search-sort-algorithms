import pytest
from binary_search import binary_search

test_case = [2,4,6,8,10,134,234,391]

def test_find_in_list():
    assert binary_search(test_case, 10) == test_case.index(10)

def test_find_not_in_list():
    assert binary_search(test_case, 7) == "go fish"