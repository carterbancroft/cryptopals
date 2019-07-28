# [Cryptopals Set 1 Challenge 8](https://cryptopals.com/sets/1/challenges/8)

This code reads in a file of hex encoded lines of bytes, looks at each individual line and and tries to determine if the line is encrypted using AES in ECB mode.

As the challenge states:
```
...the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
```

## Approach
The hint above is key and since this is a contrived scenario it implies that the plaintext probably contains some repeating 16 byte chunks to look for. Assuming this, we can...
1. Iterate over each line in the file
2. For each line, break it into chunks of 16 bytes (or 32 hex chars)
3. Count how many times the block occurs in the ciphertext

If a block occurs more than once in a ciphertext there's a decent chance we're working with AES in ECB mode.

_Note: Even though you should typically work with raw bytes I decided it wasn't necessary to decode the file from hex. Raw bytes or hex, the patterns will repeat, if they exist._
