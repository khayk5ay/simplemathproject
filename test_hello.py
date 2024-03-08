import hello
from hello import add, subtract, multiply, divide, square
import unittest

def test_add():
    assert(add(2,3)==5)

def test_subtract():
    assert(subtract(6,4)==2)

def test_multiply():
    assert(multiply(3,4)==12)

def test_divide():
    assert(divide(6,2)==3)

def test_square():
    assert(square(2)==4)