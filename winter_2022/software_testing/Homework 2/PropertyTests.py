from hypothesis import given, assume, settings, HealthCheck, strategies as st
from main import *
import pytest
import numpy as np


auto_gen_list = st.lists(st.integers(min_value = 0, max_value = 100), min_size=1, max_size=30).map(np.array)
index = st.integers(min_value=0, max_value=30)



#Validity tests - Purposfully tests incorrect inputs to test errors
#Testing a value type that is not np.ndarry
@given(test = st.integers(min_value = 0, max_value = 100))
def test_not_a_list(test):
    with pytest.raises((TypeError, Exception)):
        assert validity(test)

#Testing a list of size 0
@given(list = st.lists(st.integers(), min_size=0, max_size=0))
def test_empty_list(list):
    with pytest.raises((TypeError, Exception)):
        assert validity(list)

#Testing a list continaing integers and strings that can't be directly compared
@given(list = st.lists(st.tuples(st.integers(), st.text())))
def test_mixed_list(list):
    with pytest.raises((TypeError, Exception)):
        assert validity(list)

#Testing a list containing None
@given(list = st.lists(st.none()))
def test_list_not_null(list):
    with pytest.raises((TypeError, Exception)):
        assert validity(list)


#Post Conditions - Make sure something correct is returned after running
@given(auto_gen_list)
def test_element_left_of_mid(input):
    element = input[0]
    result = binary_search(input, element)
    assert result == 0
    

@given(auto_gen_list)
def test_element_right_of_mid(input):
    element = input[-1]
    result = binary_search(input, element)
    assert result == 0

@given(auto_gen_list)
def test_element_on_mid(input):
    size = len(input)
    mid = size // 2
    element = input[mid]
    result = binary_search(input, element)
    assert result == 0 

@given(auto_gen_list, index)
@settings(suppress_health_check=(HealthCheck.filter_too_much,))
def test_element_random_index(input, index):
    size = len(input)
    assume(0 < index < size)
    print(index, size)
    element = input[index]
    result = binary_search(input, element)
    assert result == 0 

@given(auto_gen_list)
def test_no_element_right_of_mid(input):
    element = 101
    result = binary_search(input, element)
    assert result == 1

@given(auto_gen_list)
def test_no_element_left_of_mid(input):
    element = -1
    result = binary_search(input, element)
    assert result == 1
    
