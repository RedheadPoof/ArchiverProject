
import os.path


def read_file(file_path):
    file_path = os.path.abspath(file_path)
    file_name = os.path.basename(file_path).split(".")[0]
    try:
        with open(file_path, "r") as input_file:
            out_string = input_file.readline()
    except FileNotFoundError:
        print("So file is not found, try again")
        out_string = None
        file_name = None
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
    processed_sequence = chr(processed_list[0])
    uncompressed_string = processed_sequence
    for counter_list in range(1, len(processed_list)):
        if processed_list[counter_list] < 256:
            uncompressed_sequence = chr(processed_list[counter_list])
        else:
            uncompressed_sequence = additional_sequence[processed_list[counter_list]]
        uncompressed_string += uncompressed_sequence
        processed_sequence += uncompressed_sequence[0]
        additional_sequence[number_additional_sequence] = processed_sequence
        number_additional_sequence += 1
        processed_sequence = uncompressed_sequence
    return uncompressed_string


def menu(command_message="begin", file_path=None):
    if command_message == "begin":
        with open("menu.txt") as menu_file:
            menu_text = menu_file.readlines()
        menu_main = "Select option(print number without point):"
        if file_path:
            menu_status = "Selected file " + os.path.basename(file_path)
        else:
            menu_status = "No one file is selected"
        print(f"\n{menu_main} \n{menu_status} \n{menu_text}")
        new_command_message = str(input())
        menu(new_command_message, file_path)
    elif command_message == "1":
        input_file_path = str(input("\n Print file path or fie name: "))
        input_text, input_file_name = read_file(input_file_path)
        if input_text:
            print("File chosen successfully")
            menu("begin", input_file_path)
        else:
            menu()
    elif command_message == "2":
        input_text, input_file_name = read_file(file_path)
        zip_text = zip_string(input_text)
        write_file(zip_text, input_file_name)
        print("File zip successfully")
        menu()
    elif command_message == "3":
        if "compressed" in os.path.basename(file_path):
            input_text, input_file_name = read_file(file_path)
            unzip_text = unzip_string(input_text)
            write_file(unzip_text, input_file_name)
            print("File unzip successfully")
            menu()
        else:
            print("File cannot unzip, no 'compressed' in file name")
            menu()
    elif command_message == "4":
        print("Goodbye")


if __name__ == '__main__':
    menu()

