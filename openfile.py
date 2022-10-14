
import os.path


def read_file(file_path):
    file_path = os.path.abspath(file_path)
    file_name = ".".join(os.path.basename(file_path).split(".")[:-1])
    if os.path.basename(file_path).split(".")[-1] == "txt":
        try:
            with open(file_path, "r") as input_file:
                read_string = input_file.readline()
            print(f"File {file_name}.txt chosen")
            file_size = os.path.getsize(file_path)
            out_data = {"read_string": read_string, "file_name": file_name, "file_size": file_size}
            return out_data
        except FileNotFoundError:
            print("File not found, try again")
    else:
        print("Incorrect extension. Choose the file with the extension 'txt'")
    out_data = {"read_string": None, "file_name": None, "file_size": 0}
    return out_data


def write_file(final_string, input_file_name, zipping=True):
    if zipping:
        output_file_name = input_file_name + "_compress.txt"
    else:
        output_file_name = input_file_name + "_uncompress.txt"
    with open(output_file_name, "w") as output_file:
        output_file.write(final_string)
    file_path = os.path.abspath(output_file_name)
    file_size = os.path.getsize(file_path)
    out_data = {"file_size": file_size}
    return out_data
