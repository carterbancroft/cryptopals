# https://cryptopals.com/sets/1/challenges/4

from binascii import unhexlify

def score_string(hex_str):
    unhexlified = unhexlify(hex_str)

    common = 'ETAOIN SHRDLU'

    current_high_score = 0
    current_high_string = ''
    key = ''

    for i in range(256):
        data = [i ^ char for char in unhexlified]
        b = bytes(data)
        # Need to remember why I used latin-1
        b_str = str(b, 'latin-1')

        score = 0
        for j in b_str.upper():
            if j in common:
                score += 1

        if score > current_high_score:
            current_high_score = score
            current_high_string = b_str
            key = chr(i)

    return {
        'score': current_high_score,
        'string': current_high_string
    }

def do_it():
    the_file = open('./4.txt', 'r')

    answer = {'score': 0, 'string': ''}
    for line in the_file:
        curr = score_string(line.strip())

        if (curr['score'] > answer['score']):
            answer = curr

    print(f"Highest score: {answer['score']}")
    print(f"For string: {answer['string']}")

do_it()
