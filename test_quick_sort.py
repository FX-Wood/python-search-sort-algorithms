import pytest

from quick_sort import partition
from quick_sort import quick_sort
from test_in_place_sort import TestInPlaceSort

@pytest.fixture
def sort_function():
    return quick_sort

TestInPlaceSort()