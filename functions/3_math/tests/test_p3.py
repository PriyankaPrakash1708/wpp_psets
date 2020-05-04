"""
Sum Factors
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p3 import *

@pytest.mark.describe('''it returns limit if the sum of ALL 
    factors never reaches limit''')
def test_sum_factors():
    assert sum_factors(3,8,21) == 18



@pytest.mark.describe('''it returns limit if the sum of ALL 
    factors == limit''')
def test_sum_factors():
    assert sum_factors(3,8,18) == 18



@pytest.mark.describe('''it returns sum of factors until sum 
    reaches limit''')
def test_sum_factors():
    assert sum_factors(3,8,12) == 10



@pytest.mark.describe('''when numbers have NO common factors, 
    it returns sum of factors until sum reaches limit. ''')
def test_sum_factors():
    assert sum_factors(6,12,27) == 16



@pytest.mark.describe('''when numbers DO have common factors, 
    it returns sum of factors until sum reaches limit, without
    double-counting the common factors''')
def test_sum_factors():
    assert sum_factors(6,12,27) == 16



@pytest.mark.describe('''it returns error statement if at least 
    one input is not an int''')
def test_sum_factors():
    assert type(sum_factors(3,'8',18)) == str