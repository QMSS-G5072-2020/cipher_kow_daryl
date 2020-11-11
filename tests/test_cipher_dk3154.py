from cipher_dk3154 import __version__
from cipher_dk3154 import cipher_dk3154

def test_version():
    assert __version__ == '0.1.0'

def test_cipher_symbols():
    assert cipher_dk3154.cipher('72', 1, encrypt=True) == '72', "Should be 72"