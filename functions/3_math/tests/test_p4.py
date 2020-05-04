"""
Sum Multiples
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p4 import *

@pytest.mark.describe('it returns 0 if num1 > limit')
def test_sum_multiples():
    assert sum_multiples(12,8,10) == 0



@pytest.mark.describe('it returns 0 if num2 > limit')
def test_sum_multiples():
    assert sum_multiples(3,17,12) == 0



@pytest.mark.describe('it returns 0 if both num1 + num2 > limit')
def test_sum_multiples():
    assert sum_multiples(21,9,20) == 0



@pytest.mark.describe('it returns limit if num1 + num2 == limit')
def test_sum_multiples():
    assert sum_multiples(8,5,13) == 13



@pytest.mark.describe('''it returns the sum of each pair of 
    multiples UNTIL just before sum > limit''')
def test_sum_multiples():
    assert sum_multiples(4,8,42) == 36



@pytest.mark.describe('''it returns error statement if at least one
    input is not an int''')
def test_sum_multiples():
    assert type(sum_multiples(3,'8',18)) == str

