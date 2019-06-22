# https://cryptopals.com/sets/1/challenges/6

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
        x = ord(string1[i]) ^ ord(string2[i])

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


s1 = 'this is a test'
s2 = 'wokka wokka!!!'

assert hamming_distance(s1, s2) == 37
