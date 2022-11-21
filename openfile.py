
import os.path


def check_file(file_path):
    file_path = os.path.abspath(file_path)
    file_name = ".".join(os.path.basename(file_path).split(".")[:-1])
    if os.path.basename(file_path).split(".")[-1] == "txt":
        try:
            input_file = open(file_path, "r")
            print(f"File {file_name}.txt chosen")
            out_data = {"file_name": file_name}
            return out_data
        except FileNotFoundError:
            print("File not found, try again")
    else:
        print("Incorrect extension. Choose the file with the extension 'txt'")
    out_data = {"file_name": None}
    return out_data


def read_file(file_path, zipping=True):
    file_path = os.path.abspath(file_path)
    file_name = ".".join(os.path.basename(file_path).split(".")[:-1])
    if zipping:
        with open(file_path, "r", encoding="utf-8") as input_file:
            read_string = input_file.readline()
    else:
        with open(file_path, "rb") as input_file:
            read_string = input_file.read()
    file_size = os.path.getsize(file_path)
    out_data = {"read_string": read_string, "file_name": file_name, "file_size": file_size}
    return out_data


def write_file(final_string, input_file_name, zipping=True):
    if zipping:
        output_file_name = input_file_name + "_compress.txt"
        with open(output_file_name, "wb") as output_file:
            output_file.write(final_string)
    else:
        output_file_name = input_file_name + "_uncompress.txt"
        with open(output_file_name, "w") as output_file:
            output_file.write(final_string)
    file_path = os.path.abspath(output_file_name)
    file_size = os.path.getsize(file_path)
    out_data = {"file_size": file_size}
    return out_data
