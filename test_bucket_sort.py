import pytest
from test_not_in_place_sort import TestNotInPlaceSort
from bucket_sort import bucket_sort

@pytest.fixture
def sort_function():
    return bucket_sort
TestNotInPlaceSort()