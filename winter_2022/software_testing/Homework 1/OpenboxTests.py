import pytest
from main import *

#Tests each of the 4 invalid cases in validity method
@pytest.mark.parametrize("input", [
    ("Not of type 'list'"),
    ([None]),
    (["q", "r", 42]),
    ([])
])
def test_invalid_branches(input):
    dummy_element = 0
    with pytest.raises((TypeError, Exception)):
        assert binary_search(input, dummy_element)

#Tests valid method, element > mid branch, element < mid branch, and found branch
def test_with_element_present():
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    element  = 8
    assert binary_search(input, element) is 0

#Tests element not found branch
def test_without_element_present():
    input = ["Your Princess", "is in", "another", "castle"]
    element  = "Mama Mia!"
    assert binary_search(input, element) is 1