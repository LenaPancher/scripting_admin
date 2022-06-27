def char_in_array(input_string):
    """
    Split value into table
    Args:
        input_string:
    """
    char_array = list(input_string)
    convert_char_to_ascii(char_array)


def convert_char_to_ascii(char_array):
    """
    Convert char in table to ascii
    Args:
        char_array:
    """
    ascii_array = []
    for c in char_array:
        ascii_array.append(ord(c))
    print(ascii_array)
    convert_number_ascii_to_binary(ascii_array)


def convert_number_ascii_to_binary(ascii_array):
    """
    Convert every number in table to binary
    Args:
        ascii_array:
    """
    binary_array = []
    for c in ascii_array:
        binary = bin(c).replace('b', '')
        binary_array.append(binary)
    print(binary_array)
    join_elements_to_string(binary_array)


def join_elements_to_string(binary_array):
    """
    Join every element of array into one string
    Args:
        binary_array:
    """
    binary_join = "".join(binary_array)
    print(binary_join)
    cut_string_array_6_length(binary_join)


def cut_string_array_6_length(binary_join):
    """
    Cut string into array of 6 lenght string
    Args:
        binary_join:
    """
    six_binary_array = []
    for i in range(0, len(binary_join), 6):
        six_binary_array.append(binary_join[i:i + 6])
    print(six_binary_array)
    verify_string_6_length(six_binary_array)


def verify_string_6_length(six_binary_array):
    """
    Add zero to last elem if length not equals to 6
    Args:
        six_binary_array:
    """
    last_elem = six_binary_array[-1]
    last_elem_len = len(last_elem)
    if last_elem_len != 6:
        zeros = (6 - last_elem_len) * "0"
        six_binary_array[-1] = last_elem + zeros
    print(six_binary_array)
    convert_elements_to_base64(six_binary_array)


def convert_elements_to_base64(six_binary_array):
    """
    Convert array elems to base64 string
    Args:
        six_binary_array:
    """
    final_ascii_array = []
    base64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for i in six_binary_array:
        index = int(i[1:], 2)
        final_ascii_array.append(base64_table[index])
    print(final_ascii_array)
    join_elements_ascii_to_string(final_ascii_array)


def join_elements_ascii_to_string(final_ascii_array):
    """

    Args:
        final_ascii_array:
    """
    base64_str = "".join(final_ascii_array)
    verify_string_base64(base64_str)


def verify_string_base64(base64_str):
    """
    Add = to string if not base 64
    Args:
        base64_str:
    """
    modulo = len(base64_str) % 8
    if modulo != 0:
        equals = (8 - modulo) * "="
        base64_str = base64_str + equals
    print(base64_str)


if __name__ == '__main__':
    while True:
        input_user = input("Enter a value : ")
        char_in_array(input_user)
