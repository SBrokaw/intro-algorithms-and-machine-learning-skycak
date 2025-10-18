# Skycak, J. (2021). Brute Force Search with Linear-Encoding Cryptography. 
# In Introduction to Algorithms and Machine Learning: from Sorting to 
# Strategic Agents. 
# https://justinmath.com/brute-force-search-with-linear-encoding-cryptography/

def encode_msg( msg, a, b ):
    #max() function handles case where m is a ' ' space. ord(' ') == 32
    ordinal_msg = [max(0, ord(m) - 96) for m in msg.lower()] 
    encoded_msg = [o * a + b for o in ordinal_msg]

    print(f'[DEBUG 10] Input:   {msg}')
    print(f'[DEBUG 10] Ordinal: {ordinal_msg}')
    print(f'[DEBUG 10] Encoded: {encoded_msg}')

    return encoded_msg

def decode_msg( msg, a, b ):
    if a == 0 or b == 0: return False
    decoded_msg = [int((m - b) / a) for m in msg]

    legible_check = set(decoded_msg)
    if any( x < 0 or x > 26 or x % 1 != 0 for x in legible_check):
        return False
    else:
        chr_msg = [chr(96 + m) if m > 0 else ' ' for m in decoded_msg]
        
        return ''.join(chr_msg)

    return False


def enigma_decode( secret ):
    possibilities = [[]]
    possibilities = [(i, j, decoded) 
                     for p in possibilities
                     for i in range(101)
                     for j in range(101)
                     if( decoded := decode_msg( secret, i, j ) )]

    print(f'[Enigma Possibilities] (a, b, \'msg\')')
    for s in possibilities: print(f'  {s}')

encode_msg("a cat", 2, 3)
decode_msg(encode_msg("a cat", 2, 3), 2, 3)
decode_msg(encode_msg("a cat", 2, 3), 4, 5)

secret = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]
enigma_decode(secret)