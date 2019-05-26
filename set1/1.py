# https://cryptopals.com/sets/1/challenges/1

from base64 import b64encode
from binascii import unhexlify

string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

byte_seq = unhexlify(string)
print(byte_seq)

b64 = b64encode(byte_seq)

print(b64)

