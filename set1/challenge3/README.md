# [Cryptopals Set 1 Challenge 3](https://cryptopals.com/sets/1/challenges/3)
This challenge requires decrypting a hex encoded string that has been encrypted by XORing the plaintext against a single character.

## Approach
The hint is that we can use frequency analysis to determine which single character (i.e. the key) the plaintext was XOR'd against. We could devise a complex system of scoring based on all the letters in the English alphabet however, `ETAOIN SHRDLU` (the most commonly used English alphabet characters in approximate order) is a further hint.

I decided to XOR bytes representing all ASCII characters against the raw bytes of the hex string and if it produced a character contained within `ETAOIN SHRDLU` that key's "score" would increase by 1. The highest score should be the key.

So, here's what we do:
1. Convert our hex string to bytes using `unhexlify`
2. Loop over the 128 ASCII characters
3. For each character, XOR it with the bytes of our hex string
4. Increase the score by one for every character produced that is contained within `ETAOIN SHRDLU`
5. Return the highest score, the produced string (which should be the plaintext) and the key characte
