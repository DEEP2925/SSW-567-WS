import pytest
from HW01 import classify_triangle

def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral"

def test_isosceles_triangle():
    assert classify_triangle(4, 4, 6) == "Isosceles"

def test_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right Triangle"