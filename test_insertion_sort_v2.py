import pytest
from test_in_place_sort import TestInPlaceSort
from insertion_sort_v2 import insertion_sort_v2

@pytest.fixture
def sort_function():
    return insertion_sort_v2

TestInPlaceSort()