# https://cryptopals.com/sets/1/challenges/2

import base64
import binascii

def xor_hex_str(a, b):
    bytes1 = binascii.unhexlify(a)
    bytes2 = binascii.unhexlify(b)

    data = [i ^ j for i, j in zip(bytes1, bytes2)]

    return bytes(data)

#str1 = '1c0111001f010100061a024b53535009181c'
#str2 = '686974207468652062756c6c277320657965'
str1 = '1c'
str2 = '68'
# 746865206b696420646f6e277420706c6179

xor = xor_hex_str(str1, str2)
print(xor)
