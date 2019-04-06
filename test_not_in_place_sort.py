import pytest
from random import randint as rand

class TestNotInPlaceSort(object):
    def test_empty_arr(self, sort_function):
        arr = []
        assert sorted(arr) == sort_function(arr)

    def test_len_1(self, sort_function):
        arr = [1]
        assert sorted(arr) == sort_function(arr)

    def test_len_2(self, sort_function):
        arr = [2,1]
        assert sorted(arr) == sort_function(arr)

    def test_len_3(self, sort_function):
        arr = [1,3,2]
        assert sorted(arr) == sort_function(arr)
    
    def test_len_10(self, sort_function):
        arr = [rand(0,100) for n in range(10)]
        assert sorted(arr) == sort_function(arr)