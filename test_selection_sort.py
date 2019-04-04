import pytest
from random import shuffle
from random import randint as rand

from selection_sort import selection_sort

class TestSelectionSort(object):
    def test_on_len_0(self):
        assert selection_sort([]) == []
    
    def test_on_len_1(self):
        assert selection_sort([1]) == [1]
    
    def test_on_len_10(self):
        arr = [rand(0,100) for n in range(10)]
        assert selection_sort == arr.sort()
