import pytest
from test_not_in_place_sort import TestNotInPlaceSort
from three_bucket_quick_sort import three_bucket_quick_sort

@pytest.fixture
def sort_function():
    return three_bucket_quick_sort

TestNotInPlaceSort()
