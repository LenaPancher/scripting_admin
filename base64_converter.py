def converter():
    while True:
        input_string = input("Enter a value: ")

        # split value into table
        char_array = list(input_string)

        # convert char in table to ascii
        ascii_array = []
        for c in char_array:
            ascii_array.append(ord(c))
        print(ascii_array)

        # convert every number in table to binary
        binary_array = []
        for c in ascii_array:
            binary = bin(c).replace('b', '')
            binary_array.append(binary)
        print(binary_array)

        # join every element of array into one string
        binary_join = "".join(binary_array)
        print(binary_join)

        # cut string into array of 6 lenght string
        six_binary_array = []
        for i in range(0, len(binary_join), 6):
            six_binary_array.append(binary_join[i:i + 6])
        print(six_binary_array)

        # add zero to last elem if length not equals to 6
        last_elem = six_binary_array[-1]
        last_elem_len = len(last_elem)
        if last_elem_len != 6:
            zeros = (6 - last_elem_len) * "0"
            six_binary_array[-1] = last_elem + zeros
        print(six_binary_array)

        # convert array elems to base64 string
        final_ascii_array = []
        base64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        for i in six_binary_array:
            index = int(i[1:], 2)
            final_ascii_array.append(base64_table[index])
        print(final_ascii_array)
        base64_str = "".join(final_ascii_array)

        # add = to string if not base 64
        modulo = len(base64_str) % 8
        if modulo != 0:
            equals = (8 - modulo) * "="
            base64_str = base64_str + equals
        print(base64_str)


if __name__ == '__main__':
    converter()