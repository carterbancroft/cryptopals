# https://cryptopals.com/sets/1/challenges/6

# An important lesson I took away from this... Understand what kind of data you are working with...
# Strings, base64, hex, etc

# Also, take maybe the top 3 key lengths or top 10

from base64 import b64decode

# Calculate the Hamming distance between two equal length strings.
def hamming_distance(string1, string2):
    # The strings must be equal length or this will fail.
    assert len(string1) == len(string2)

    distance = 0
    for i in range(len(string1)):
        # XOR the integer representations of the current char in the string.
        # This gets us a value whose byte representation is the integer where
        # each bit is different between the two.
        #
        # Example: 
        #   for ascii chars a and b
        #   ord('a') = 97 and ord('b') = 98
        #   97 in bytes is 0110 0001
        #   98 in bytes is 0110 0010
        #   97 ^ 98     is 0000 0011 (aka 3 in decimal)
        #
        # Where each bit is set in this new value represents a hamming distance
        # of one. Now it's just a matter of summing those set bits.
        x = string1[i] ^ string2[i]

        set_bits = 0
        while (x > 0):
            # Check if the right most bit is set. If it is then track it.
            set_bits += x & 1;

            # Shift the decimal value one bit to the right and do the process
            # again.
            #
            # Bit shifting example:
            # 3 in decimal is 0000 0011 in binary
            # 3 >> 1       is 0000 0001 in binary
            #
            # We use each shifted value to compare to 1 (or 0000 0001 in bin)
            # on the previous lines.
            x >>= 1; 

        # Add the number of set bits for the current chars to the total distance
        distance += set_bits

    return distance


#s1 = 'this is a test'
#s2 = 'wokka wokka!!!'

#assert hamming_distance(s1, s2) == 37

def get_lowest_hamming_distance(data):
    lowest = None
    best_keylength = None

    for i in range(2, 41):
        keylength = i
        to_average = []

        start = 0
        end = start + keylength
        while (1):
            first_chunk = data[start:end]
            second_chunk = data[start + keylength:end + keylength]

            if (len(second_chunk) < keylength):
                break

            distance = hamming_distance(first_chunk, second_chunk)
            normalized = distance / keylength

            to_average.append(normalized)

            start = end + keylength
            end = start + keylength

        average = sum(to_average) / len(to_average)
        to_average = []

        if lowest == None or average < lowest:
            lowest = average
            best_keylength = keylength

    return best_keylength

def get_keylength_chunks(keylength, data):
    chunks = dict.fromkeys(range(keylength))
    i = 0
    for byte in data:
        if (i == keylength): i = 0

        if (chunks[i] == None): chunks[i] = []

        chunks[i].append(byte)

        i += 1

    return chunks

def get_key(blocks):
    common = 'ETAOIN SHRDLU'

    key = ''

    for i in blocks:
        current_high_score = 0
        current_high_string = ''
        current_key_char = ''

        for j in range(127):
            xord = [j ^ dec for dec in blocks[i]]
            b = bytes(xord)
            b_str = str(b, 'utf-8')

            score = 0
            for k in b_str.upper():
                if k in common:
                    score += 1

            if score > current_high_score:
                current_high_score = score
                current_high_string = b_str
                current_key_char = chr(j)

        key += current_key_char

    return key

    #print(f'highest score is: {current_high_score}')
    #print(f"for the string: '{current_high_string}'")
    #print(f"with the key: '{key}'")


def do_it():
    the_file = open('./6.txt', 'r')
    data = the_file.read()
    decoded = b64decode(data)

    keylength = get_lowest_hamming_distance(decoded)
    chunks = get_keylength_chunks(keylength, decoded)
    key = get_key(chunks)

    #print(keylength)
    #print('-----------------')
    #print(chunks[1])
    #print('-----------------')
    print(key)


do_it()
