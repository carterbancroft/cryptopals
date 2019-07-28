# [Cryptopals Set 1 Challenge 7](https://cryptopals.com/sets/1/challenges/7)
This challenge requires using internal code libraries to decrypt base64 encoded content encrypted with AES-128 in ECB mode using a known key.

## Approach
The challenge tells us to use code libraries which makes this fairly straightforward. We can:
1. Base64 decode the data since we know it's base64 encoded
2. Use `Cypto.Cipher.AES` to decrypt the ciphertext
