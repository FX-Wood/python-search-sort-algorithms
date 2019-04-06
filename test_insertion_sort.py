import pytest
from insertion_sort import insertion_sort
from test_in_place_sort import TestInPlaceSort

@pytest.fixture
def sort_function():
    return insertion_sort

TestInPlaceSort()