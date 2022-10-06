
<<<<<<< HEAD
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


if __name__ == '__main__':
    input_file_path = str(input())
    input_string = read_file(input_file_path)
    print(input_string)


=======
def filereading(filepath):
>>>>>>> origin/File_reading
