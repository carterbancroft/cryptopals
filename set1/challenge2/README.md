# [Cryptopals Set 1 Challenge 2](https://cryptopals.com/sets/1/challenges/2)
This challenge requires XORing two equal length hex strings together.

## Approach
We can do this by:
1. Converting each hex string into raw bytes (using `binascii.unhexlify`)
2. Looping over every byte in the first string and XORing (`^`) it with the correspoonding byte in the second string

The challenge provides the correct answer which we can use to verify that the code is working correctly.
