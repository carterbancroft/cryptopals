# https://cryptopals.com/sets/1/challenges/5

from binascii import hexlify

def repeating_key_xor(key, string):
    print(string)

    # The position within the key
    i = 0
    arr = []
    for ch in string:
        arr.append(ord(ch) ^ ord(key[i]))

        i += 1
        if (i == len(key)):
            i = 0

    return hexlify(bytearray(arr))

key = 'ICE'
string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

encrypted = repeating_key_xor(key, string)
expected = b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

assert encrypted == expected, 'The string is not encrypted properly.'

print(f'encrypted: {encrypted}')
print(f'expected:  {expected}')
