from logging import exception
import pytest
from main import *

#Testing invalid combinations
@pytest.mark.parametrize("input", [
    (None),
    ([None]),
    (["q", "r", 42]),
    ([]),
    (1),
    ("aaaaaaaaaaa"),
    (4.2),
    ([9, 8, 7, 3, 4444, 66666666, 1312, 5.55])
])
def test_invalid_types(input):
    dummy_element = 0
    with pytest.raises((TypeError, Exception)):
        assert binary_search(input, dummy_element)


#Testing Valid Inputs
#1) Valid array that includes element
@pytest.mark.parametrize("array, element", [
    ([1, 2, 3, 4, 5, 6, 7], 2),
    ([1.2, 3.4, 5.6, 7.8, 9.0, 10.2], 1.2),
    (["a", "b", "c", "d", "e"], "c"),
    (["Array of size 1"], "Array of size 1"),
    (["in", "order", "strings"], "strings"),
    (["strings", "that must be", "sorted", "alphabetically", "!"], "!"),

])
def test_element_present(array, element):
    assert binary_search(array, element) is 0


#2) Valid array that does not includes element
@pytest.mark.parametrize("array, element", [
    ([1, 2, 3, 4, 5, 6, 7], 7.000000001),
    ([1.2, 3.4, 5.6, 7.8, 9.0, 10.2], 1),
    (["a", "b", "c", "d", "e"], "C"),
    (["Array of size 1"], "Array"),
    (["in", "order", "strings"], "out"),
    (["strings", "that must be", "sorted", "alphabetically", "!"], "?"),

])
def test_element_not_present(array, element):
    assert binary_search(array, element) is 1