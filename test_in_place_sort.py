import pytest
from random import randint as rand

class TestInPlaceSort(object):
    def test_empty_arr(self, sort_function):
        arr = []
        sorted_arr = arr.copy()
        sort_function(sorted_arr)
        assert sorted(arr) == sorted_arr

    def test_len_1(self, sort_function):
        arr = [1]
        sorted_arr = arr.copy()
        sort_function(sorted_arr)
        assert sorted(arr) == sorted_arr

    def test_len_2(self, sort_function):
        arr = [2,1]
        sorted_arr = arr.copy()
        sort_function(sorted_arr)
        assert sorted(arr) == sorted_arr

    def test_len_3(self, sort_function):
        arr = [1,3,2]
        sorted_arr = arr.copy()
        sort_function(sorted_arr)
        assert sorted(arr) == sorted_arr
    
    def test_len_10(self, sort_function):
        arr = [rand(0,100) for n in range(10)]
        sorted_arr = arr.copy()
        sort_function(sorted_arr)
        assert sorted(arr) == sorted_arr