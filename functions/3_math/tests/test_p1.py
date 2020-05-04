"""
Sign of Product
"""

import io
import pytest
from unittest import TestCase
from unittest.mock import patch
from p1 import *


@pytest.mark.describe('it returns positive if 0 of the args are neg')
def test_product_sign():
	assert product_sign(1,2,3) == 'positive'

@pytest.mark.describe('it returns negative 1 of the args is neg')
def test_product_sign():
	assert product_sign(-1,2,3) == 'negative'

@pytest.mark.describe('it returns positive if 2 of the args are neg')
def test_product_sign():
	assert product_sign(-1,2,-3) == 'positive'

@pytest.mark.describe('it returns negative 3 of the args are neg')
def test_product_sign():
	assert product_sign(-1,-2,-3) == 'negative'
