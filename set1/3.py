# https://cryptopals.com/sets/1/challenges/3

from binascii import unhexlify


def do_it(hex_str):
    unhexlified = unhexlify(hex_str)

    common = 'ETAOIN SHRDLU'

    current_high_score = 0
    current_high_string = ''
    key = ''

    for i in range(127):
        data = [i ^ char for char in unhexlified]
        b = bytes(data)
        b_str = str(b, 'utf-8')

        score = 0
        for j in b_str.upper():
            if j in common:
                score += 1

        if score > current_high_score:
            current_high_score = score
            current_high_string = b_str
            key = chr(i)

    print(f'highest score is: {current_high_score}')
    print(f"for the string: '{current_high_string}'")
    print(f"with the key: '{key}'")

hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
do_it(hex_str)
