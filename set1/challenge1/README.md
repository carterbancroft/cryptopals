# [Cryptopals Set 1 Challenge 1](https://cryptopals.com/sets/1/challenges/1)
This challenge requires converting a hex encoded string to base 64.

## Approach
We can do this by first, converting the hex string to raw bytes and then base64 encoding it.

Converting to raw bytes is possible using Python's `binascii.unhexlify` and the resulting byte sequence can be base64 encoded using `base64.b64encode`.
