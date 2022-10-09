
import os.path


def read_file(file_path, zipping=False):
    file_path = os.path.abspath(file_path)
    file_name = os.path.basename(file_path).split(".")[0]
    if zipping:
        if "compressed" not in file_name:
            print("File name is not correct. Name must include word 'compressed'.")
            out_string = None
            return out_string
    try:
        with open(file_path, "r") as input_file:
            out_string = input_file.readline()
    except FileNotFoundError as NoFile:
        print("So file is not found, try again")
        out_string = None
    return out_string, file_name


def write_file(final_string, input_file_name, zipping=False):
    if zipping:
        output_file_name = input_file_name + "_uncompressed.txt"
    else:
        output_file_name = input_file_name + "_compressed.txt"
    with open(output_file_name, "w") as output_file:
        output_file.write(final_string)
    return


def zip_string(processed_string):
    symbol_of_string_number = 0
    additional_sequence = {}
    number_additional_sequence = 256
    compressed_string = ""
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
            compressed_string += additional_sequence[compressed_sequence] + " "
        else:
            compressed_string += str(ord(compressed_sequence)) + " "
        symbol_of_string_number += 1
    print(additional_sequence)
    return compressed_string


def unzip_string(processed_string):
    processed_list = list(map(int, processed_string.split()))
    additional_sequence = {}
    number_additional_sequence = 256
    processed_sequense = chr(processed_list[0])
    uncompressed_string = processed_sequense
    for counter_list in range(1, len(processed_list)):
        if processed_list[counter_list] < 256:
            uncompressed_sequence = chr(processed_list[counter_list])
        else:
            uncompressed_sequence = additional_sequence[processed_list[counter_list]]
        uncompressed_string += uncompressed_sequence
        processed_sequense += uncompressed_sequence[0]
        additional_sequence[number_additional_sequence] = processed_sequense
        number_additional_sequence += 1
        processed_sequense = uncompressed_sequence
    return uncompressed_string


if __name__ == '__main__':
    input_string = str(input())
    output_string = unzip_string(input_string)
    print(output_string)
