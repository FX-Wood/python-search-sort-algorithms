import pytest
from random import shuffle
from random import randint as rand

from selection_sort import selection_sort

class TestSelectionSort(object):
    def test_on_len_0(self):
        assert selection_sort([]) == []
    
    def test_on_len_1(self):
        assert selection_sort([1]) == [1]
    
    def test_on_len_2(self):
        arr = [2,1]
        assert selection_sort(arr) == [1,2]

    def test_on_len_3(self):
        arr = [1,3,2]
        assert selection_sort(arr) == [1,2,3]

    def test_on_len_3_mixed(self):
        arr = [10, 3, 14]
        assert selection_sort(arr) == [3,10,14]

    def test_on_len_10(self):
        arr = [rand(0,100) for n in range(10)]
        sorted_arr = arr.copy()
        sorted_arr.sort()
        assert selection_sort(arr) == sorted_arr

    def test_duplicate_data(self):
        arr = [1,2,1,1,1,1]
        sorted_arr = arr.copy()
        sorted_arr.sort()
        assert selection_sort(arr) == sorted_arr