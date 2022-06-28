import base64_encoder_v2 as encoder
import re
import sys
sys.setrecursionlimit(1500)

def check_if_value_is_base64_encoded(input_value):
    expression = "^([A-Za-z0-9+/]{4})*([A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{2}==)?$"
    matches = re.match(expression, input_value)
    if matches:
        decode_base64_to_ascii(input_value)
    else:
        print("Veuillez saisir une chaine de caratère encoder en base 64")
        check_if_value_is_base64_encoded(input_value)


def decode_base64_to_ascii(base64_value):
    convert_ascii_to_string(base64_value)


def remove_base64_last_characters(base64_value):
    return re.sub(r"[^a-zA-Z0-9]", "", base64_value)


def base64_string_to_array(value: str):
    string_without_special_character = remove_base64_last_characters(value)
    return list(string_without_special_character)


def convert_base_array_to_base64_int(value: str):
    array = base64_string_to_array(value)
    base64_to_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    base64_list_int = []
    for i in array:
        base64_list_int.append(base64_to_list.index(i))
    return base64_list_int


def convert_list_of_int_to_binary(value):
    array = convert_base_array_to_base64_int(value)
    binary_array = []
    for i in array:
        binary_array.append(bin(i).replace("0b", ""))
    return binary_array


def convert_binary_to_ascii(value: str):
    binary_list = add_zero_before_or_after_value(value)
    return encoder.join_elements_to_string(binary_list)
    

def cut_binary_string(value: str, by):
    pol = convert_binary_to_ascii(value)
    return encoder.cut_string_array_6_length(pol, by)


def add_zero_before_or_after_value(value: str):
    array_binary_string = convert_list_of_int_to_binary(value)
    array = []
    for index, v in enumerate(array_binary_string):
        if v is not array_binary_string[-1]:
            while len(v) < 6:
                v = "0" + v
            array.append(v)
        else:
            while len(v) < 6:
                v = v + "0"
            array.append(v)
    return array


def remove_value_len_less_than_height(value: str):
    string_val = cut_binary_string(value, 8)
    new_array = []
    for v in string_val:
        if len(v) == 8:
            new_array.append(v)
    return new_array
    

def remove_zero_at_beggining(value: str):
    array_val = remove_value_len_less_than_height(value)
    print(array_val)
    new_array = []
    new_array_of_number = []
    for v in array_val:
        new_array.append(v[1:])
    
    print(new_array)
    for i in new_array:
        new_array_of_number.append(int(i, 2))
    return new_array_of_number


def convert_ascii_to_string(val: str):
    ascii_array = remove_zero_at_beggining(val)
    value_converted = []
    for v in ascii_array:
        value_converted.append(chr(v))
    print("".join(value_converted))
    return "".join(value_converted)
    

if __name__ =="__main__":
    input_val = input("enter value base64 : ")
    check_if_value_is_base64_encoded(input_val)