
import os.path


def read_file(file_path):
    file_path = os.path.abspath(file_path)
    file_name = os.path.basename(file_path)[:-4]
    try:
        with open(file_path, "r") as input_file:
            read_string = input_file.readline()
        print(f"File {file_name} chosen")
    except FileNotFoundError:
        print("File not found, try again")
        read_string = None
        file_name = None
    out_data = {"read_string": read_string, "file_name": file_name}
    return out_data


def write_file(final_string, input_file_name, zipping=True):
    if zipping:
        output_file_name = input_file_name + "_compress.txt"
    else:
        output_file_name = input_file_name + "_uncompress.txt"
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


def menu():
    menu_file_status = "File status: no file selected"
    menu_main = "Select an option:"
    menu_text = "1.Choose file\n2.Compress chosen file\n3.Decompress chosen file\n4.Exit"
    menu_command = "begin"
    while menu_command != "4":
        print(f"\n{menu_file_status} \n{menu_main} \n{menu_text}")
        menu_command = str(input("Print number of option: "))
        #  Choose file
        if menu_command == "1":
            file_path = str(input("Print file name or file path: "))
            input_data = read_file(file_path)
            if input_data["file_name"]:
                menu_file_status = "File status: selected " + os.path.abspath(file_path)
        #  Compress chosen file
        elif menu_command == "2":
            if menu_file_status != "File status: no file selected":
                output_string = zip_string(input_data["read_string"])
                write_file(output_string, input_data["file_name"])
                print("Compress done")
            else:
                print("No file selected, zip is not")
        #  Decompress chosen file
        elif menu_command == "3":
            if menu_file_status != "File status: no file selected":
                if input_data["file_name"].endswith("compress"):
                    output_string = unzip_string(input_data["read_string"])
                    write_file(output_string, input_data["file_name"])
                    print("Decompress done")
                else:
                    print("File name is wrong, unzip is not")
            else:
                print("No file selected, zip is not")
    print("Goodbye")


if __name__ == '__main__':
    menu()
