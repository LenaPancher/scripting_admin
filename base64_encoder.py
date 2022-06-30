from logging_conf_base64 import *


def char_in_array(input_string):
    """
    Split value into table
    Args:
        input_string: user input (String)
    """
    char_array = list(input_string)
    logging.info(char_array)
    return char_array


def convert_char_to_ascii(char_array):
    """
    Convert char in table to ascii
    Args:
        char_array: string table of each element of the user input
    """
    ascii_array = []
    for c in char_array:
        ascii_array.append(ord(c))
    logging.info(ascii_array)
    return ascii_array


def convert_number_ascii_to_binary(ascii_array):
    """
    Convert every number in table to binary
    Args:
        ascii_array: number table that represents ascii
    """
    binary_array = []
    for c in ascii_array:
        binary = bin(c).replace('b', '')
        binary_array.append(binary)
    logging.info(binary_array)
    return binary_array


def join_elements_to_string(binary_array):
    """
    Join every element of array into one string
    Args:
        binary_array: string array where each element represents a binary string
    """
    binary_join = "".join(binary_array)
    logging.info(binary_join)
    return binary_join


def cut_string_array_6_length(binary_join):
    """
    Cut string into array of 6 length string
    Args:
        binary_join: character string that groups all the elements of the previous table
    """
    six_binary_array = []
    for i in range(0, len(binary_join), 6):
        six_binary_array.append(binary_join[i:i + 6])
    logging.info(six_binary_array)
    return six_binary_array


def verify_string_6_length(six_binary_array):
    """
    Add zero to last elem if length not equals to 6
    Args:
        six_binary_array: 6-character string table
    """
    last_elem = six_binary_array[-1]
    last_elem_len = len(last_elem)
    if last_elem_len != 6:
        zeros = (6 - last_elem_len) * "0"
        six_binary_array[-1] = last_elem + zeros
    logging.info(six_binary_array)
    return six_binary_array


def convert_elements_to_base64(six_binary_array):
    """
    Convert array elems to base64 string
    Args:
        six_binary_array: 6-character string table
    """
    final_ascii_array = []
    base64_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    for i in six_binary_array:
        index = int(i[1:], 2)
        final_ascii_array.append(base64_table[index])
    logging.info(final_ascii_array)
    return final_ascii_array


def join_elements_ascii_to_string(final_ascii_array):
    """
    Join every element of array into one string
    Args:
        final_ascii_array: string array where each element represents a string
    """
    base64_str = "".join(final_ascii_array)
    logging.info(base64_str)
    return base64_str


def verify_string_base64(base64_str):
    """
    Add = to string if not base 64
    Args:
        base64_str: character string that groups all the elements of the previous table
    """
    modulo = len(base64_str) % 8
    if modulo != 0:
        equals = (8 - modulo) * "="
        base64_str = base64_str + equals
    logging.info(base64_str)
    return base64_str


def base64_encode(input, log):
    logging_conf(logging_level=log)
    logging.debug(input)
    return verify_string_base64(
        join_elements_ascii_to_string(
            convert_elements_to_base64(
                verify_string_6_length(
                    cut_string_array_6_length(
                        join_elements_to_string(
                            convert_number_ascii_to_binary(
                                convert_char_to_ascii(
                                    char_in_array(input)))))))))
