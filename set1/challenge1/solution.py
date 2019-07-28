# https://cryptopals.com/sets/1/challenges/1

from base64 import b64encode
from binascii import unhexlify

string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# Convert the hex string to a sequence of bytes using unhexlify
byte_seq = unhexlify(string)

# base 64 encode it
b64 = b64encode(byte_seq)
expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

assert b64 == expected, 'Not properly encoded.'

# Interestingly the byte sequence is the song lyric
print(byte_seq)
print(b64)

