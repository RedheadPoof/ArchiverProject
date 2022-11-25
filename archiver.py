
def number_to_bytes(number, type_number):
    count_bytes = 1
    while True:
        if number >= 256 ** count_bytes:
            count_bytes += 1
        else:
            break
    info_number = type_number * 100 + count_bytes
    info_byte = info_number.to_bytes(1, byteorder="big")
    number_in_bytes = number.to_bytes(count_bytes, byteorder="little")
    converted_number = info_byte + number_in_bytes
    return converted_number


def bytes_to_number(list_bytes):
    processed_list = list_bytes.copy()
    type_number = processed_list[0] // 100
    count_bytes = processed_list[0] % 100
    number = 0
    for i in range(1, count_bytes + 1):
        number += processed_list[i] * (256 ** (i - 1))
    out_data = {"number": number, "type_number": type_number, "length_number": count_bytes + 1}
    return out_data


def zip_string(processed_string):
    symbol_of_string_number = 0
    additional_sequence = {}
    number_additional_sequence = 256
    compress_list_bytes = bytearray()
    while symbol_of_string_number < len(processed_string):
        compressed_sequence = processed_string[symbol_of_string_number]
        while symbol_of_string_number + 1 < len(processed_string):
            processed_sequence = compressed_sequence + processed_string[symbol_of_string_number + 1]
            if processed_sequence in additional_sequence:
                compressed_sequence = processed_sequence
                symbol_of_string_number += 1
            else:
                additional_sequence[processed_sequence] = str(number_additional_sequence)
                number_additional_sequence += 1
                break
        if len(compressed_sequence) != 1:
            compress_sequence = int(additional_sequence[compressed_sequence])
            type_number = 1
        else:
            compress_sequence = ord(compressed_sequence)
            type_number = 0
        compress_list_bytes += number_to_bytes(compress_sequence, type_number)
        symbol_of_string_number += 1
    return compress_list_bytes


def unzip_string(processed_list_bytes):
    processed_list = list(processed_list_bytes)
    additional_sequence = {}
    number_additional_sequence = 256
    processed_data = bytes_to_number(processed_list[0:56])
    processed_sequence = chr(processed_data["number"])
    first_byte_counter = processed_data["length_number"]
    uncompressed_string = processed_sequence
    while first_byte_counter < len(processed_list):
        processed_data = bytes_to_number(processed_list[first_byte_counter:(first_byte_counter + 56)])
        processed_counter = processed_data["number"]
        first_byte_counter += processed_data["length_number"]
        if processed_data["type_number"] == 0:
            uncompressed_sequence = chr(processed_counter)
        else:
            if processed_counter < number_additional_sequence:
                uncompressed_sequence = additional_sequence[processed_counter]
            elif processed_counter == number_additional_sequence:
                uncompressed_sequence = processed_sequence + processed_sequence[0]
        processed_sequence += uncompressed_sequence[0]
        uncompressed_string += uncompressed_sequence
        if (processed_sequence not in additional_sequence) & (number_additional_sequence < 256 * 256):
            additional_sequence[number_additional_sequence] = processed_sequence
            number_additional_sequence += 1
        processed_sequence = uncompressed_sequence
    return uncompressed_string
