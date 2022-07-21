import pytest
from caesar_cipher.cipher import encrypt,decrypt,crack

# @pytest.mark.skip("TODO")
def test_encrypt_shift_1():
    actual = encrypt("apple", 1)
    expected = "bqqmf"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_encrypt_shift_10():
    actual = encrypt("apple", 10)
    expected = "kzzvo"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_encrypt_shift_20():
    actual = encrypt("apple", 20)
    expected = "ujjfy"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_uppercase():
    actual = encrypt("BANANA", 10)
    expected = "LKXKXK"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_with_whitespace():
    actual = encrypt("apples and bananas", 1)
    expected = "bqqmft boe cbobobt"
    assert actual == expected

