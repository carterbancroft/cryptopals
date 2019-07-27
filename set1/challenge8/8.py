# https://cryptopals.com/sets/1/challenges/8

# The problem with ECB is that it is stateless and deterministic; the same 16
# byte plaintext block will always produce the same 16 byte ciphertext.

# Every 32 hex characters is 16 bytes (a hex character is 4 bits wide). This
# function returns chunks of that size.
def split_in_n(ciphertext, length):
    blocks = []

    start = 0
    end = length
    while(1):
        if (start >= len(ciphertext)): break

        blocks.append(ciphertext[start:end])
        start = end
        end += length

    return blocks


def score_ciphertext(ciphertext):
    blocks = split_in_n(ciphertext, 32)

    total = 0

    for block in blocks:
        score = blocks.count(block)
        total += score

    return total


the_file = open('./8.txt', 'r')
data = the_file.read()
ciphertexts = data.split('\n')

#print(score_ciphertext(ciphertexts[0]))

max_score = 0
max_ciphertext = ''
for ciphertext in ciphertexts:
    score = score_ciphertext(ciphertext)
    if (score > max_score):
        max_score = score
        max_ciphertext = ciphertext

print(max_score)
print(max_ciphertext)
