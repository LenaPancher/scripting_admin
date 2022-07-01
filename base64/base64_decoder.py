import re

from logging_conf_base64 import *

"""import sys
sys.setrecursionlimit(1500)"""


def base64_decoder(input, log):
    """
    The starter method
    Here we call all our methods
    """
    logging_conf(logging_level=log)
    logging.debut(input)

    if len(input_value) > 0:
        matches = check_if_value_is_base64_encoded(input_value)

        if matches:
            # second step
            string_formatted = remove_base64_last_characters(input_value)
            # third step
            array_base64_list_string = base64_string_to_array(string_formatted)
            # fourth step
            array_base64_int = convert_base_array_to_base64_int(array_base64_list_string)
            # fifth step
            array_binary = convert_list_of_int_to_binary(array_base64_int)
            # sixth step
            array_binary_with_zero = add_zero_before_or_after_value(array_binary)
            # seventh step
            binary_join_to_single_string = convert_binary_to_ascii(array_binary_with_zero)
            # height step
            val = remove_value_len_less_than_height(binary_join_to_single_string)
            # ninth step
            value_without_zero_at_beggining = remove_zero_at_beggining(val)
            # tenth
            return convert_ascii_to_string(value_without_zero_at_beggining)
        else:
            print("Veuillez saisir une chaine de caratère encoder en base 64")
            check_if_value_is_base64_encoded(input_value)
    else:
        decode_starter()


def check_if_value_is_base64_encoded(input_value):
    """
    Verify if given string is base64 encoded
    Args:
        input_value: The given string
    """
    expression = "^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$"
    matches = re.match(expression, input_value)
    logging.info(matches)
    return matches


def remove_base64_last_characters(base64_value):
    """
    Remove all equals at the end of base64 string
    e.g : "toto==" will be " toto "
    Args:
        base64_value: the given base64 string
    """
    result = re.sub(r"[^a-zA-Z0-9]", "", base64_value)
    logging.info(result)
    return result


def base64_string_to_array(value: str):
    """
    Convert base64 simple string
    to a array of letter
    e.g : "toto" will be converted to " ['t','o','t','o'] "
    Args:
        value: base64 single line string
    """
    list_result = list(value)
    logging.info(list_result)
    return list_result


def convert_base_array_to_base64_int(list_string: list):
    """
    Convert base64 list of string to
    base64 list of integer
    Args:
        list_string: List of base64 string
    """
    base64_to_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    base64_list_int = []
    for i in list_string:
        base64_list_int.append(base64_to_list.index(i))
    logging.info("converting base64 list of string to list of integer")
    logging.info(base64_list_int)
    return base64_list_int


def convert_list_of_int_to_binary(list_int):
    """
    Convert list of ASCII int to a binary list
    Args:
        list_int: ASCII list int
    """
    binary_array = []
    for i in list_int:
        binary_array.append(bin(i).replace("0b", ""))
    logging.info(binary_array)
    return binary_array


def convert_binary_to_ascii(binary_list):
    """
    Get a binary list and join it to a single line string value
    Args:
        binary_list: Binary list
    """
    final_string = encoder.join_elements_to_string(binary_list)
    logging.info(final_string)
    return final_string


def cut_binary_string(binary_string: str, by):
    """
    Cut binary string
    Args:
        binary_string: Binary string
        by: ( int ) the len of each cut
    """
    string_cuted = encoder.cut_string_array_6_length(binary_string, by)
    logging.info(string_cuted)
    return string_cuted


def add_zero_before_or_after_value(binary_int_list):
    """
    Add a zero before or after a binary value
    Args:
        binary_int_list: List of binary
    """
    array = []
    for index, v in enumerate(binary_int_list):
        if v is not binary_int_list[-1]:
            while len(v) < 6:
                v = "0" + v
            array.append(v)
        else:
            while len(v) < 6:
                v = v + "0"
            array.append(v)
    logging.info(array)
    return array


def remove_value_len_less_than_height(value):
    """
    Remove all binary that are less than 8 len
    Args:
        value: binary array
    """
    string_val = cut_binary_string(value, 8)
    new_array = []
    for v in string_val:
        if len(v) == 8:
            new_array.append(v)
    logging.info(new_array)
    return new_array


def remove_zero_at_beggining(value):
    """
    Remove zero at the beginning of binary code
    Args:
        value: Binary list
    """
    # array_val = remove_value_len_less_than_height(value)
    new_array = []
    new_array_of_number = []
    for v in value:
        new_array.append(v[1:])
    logging.info(new_array)

    for i in new_array:
        new_array_of_number.append(int(i, 2))
    logging.info(new_array_of_number)
    return new_array_of_number


def convert_ascii_to_string(val):
    """
    Convert given ascii list of number to
    list of ascii string
    then join the given list of string to a single line
    Args:
        val: ASCII list of number
    """
    value_converted = []
    for v in val:
        value_converted.append(chr(v))
    result = "".join(value_converted)
    logging.info(result)
    return result
