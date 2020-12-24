from time import sleep
import pytest
import shopping_basket.primes as sb
def test_always_passes():
    print("Running PyTest ...")
    sleep(3)
    assert True
    print("Test Completed")


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1,2,3,4])) == [4,3,2,1]
"""
def test_some_primes():
    assert 37 in {
        num
        for num in range(1,50)
        if num !=1 and not any ([num % div == 0 for div in range (2, num)])
    }
"""


# Arrange tests as 
def test_basic():
    # Arrange
    # Act
    # Assert
    pass


def test_prime_low_number():
    assert sb.is_prime(1) == False

def test_prime_prime_number():
    assert sb.is_prime(29)

def test_prime_composite_number():
    assert sb.is_prime(15) == False

def test_sum_of_primes_empty_list():
    assert sb.sum_of_primes([]) == 0

def test_sum_of_primes_mixed_list():
    assert sb.sum_of_primes([11,15,17,18,20,100]) == 28

