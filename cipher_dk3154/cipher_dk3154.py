def cipher(text, shift, encrypt=True):
    """
    Encrypts/decrypts the alphabetical portion of python strings according to a given shift integer value
    
    Parameters
    ----------
    text: str
      A python string that you wish to encrypt/decrypt
    shift: int
      A python integer which determines the value of the shift along the alphabetical order
    encrypt: bool
      A python boolean which determines whether to apply the positive (encrypt) or negative (decrypt) value of shift to the text
        
    Returns
    -------
    str
      The encrypted/decrypted text
     
    Example
    -------
    >>> from cipher_dk3154 import cipher
    >>> text = "dkow72"
    >>> shift = 1
    >>> cipher_dk3154.cipher(text, shift, encrypt=True) 
    'elpx72'
    >>> cipher_dk3154.cipher(cipher_dk3154.cipher(text, shift, encrypt=True), shift, encrypt=False) 
    'dkow72'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text