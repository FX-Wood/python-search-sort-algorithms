import pytest
from merge_sort import merge_sort
from merge_sort import merge

from test_not_in_place_sort import TestNotInPlaceSort

@pytest.fixture
def sort_function():
    return merge_sort

TestNotInPlaceSort()