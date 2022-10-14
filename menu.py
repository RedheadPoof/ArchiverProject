
import os.path
import openfile
import archiver


def display_menu():
    menu_file_status = "File status: no file selected"
    menu_text = "Select an option:\n" \
                "1.Choose file\n" \
                "2.Compress chosen file\n" \
                "3.Decompress chosen file\n" \
                "4.Exit"
    menu_command = "begin"
    while menu_command != "4":
        print(f"\n{menu_file_status} \n{menu_text}")
        menu_command = str(input("Print number of option: "))
        #  Choose file
        if menu_command == "1":
            file_path = str(input("Print file name or file path: "))
            input_data = openfile.read_file(file_path)
            if input_data["file_name"]:
                menu_file_status = "File status: selected " + os.path.abspath(file_path)
        #  Compress chosen file
        elif menu_command == "2":
            if menu_file_status != "File status: no file selected":
                output_string = archiver.zip_string(input_data["read_string"])
                output_file_data = openfile.write_file(output_string, input_data["file_name"])
                compress_ratio = output_file_data["file_size"] / input_data["file_size"] * 100
                print(f"Compress done, compress ratio: {compress_ratio}%")
            else:
                print("No file selected, zip is not possible")
        #  Decompress chosen file
        elif menu_command == "3":
            if menu_file_status != "File status: no file selected":
                if input_data["file_name"].endswith("compress"):
                    output_string = archiver.unzip_string(input_data["read_string"])
                    openfile.write_file(output_string, input_data["file_name"], zipping=False)
                    print("Decompress done")
                else:
                    print("File name is wrong, unzip is not possible")
            else:
                print("No file selected, zip is not possible")
    print("Goodbye")
