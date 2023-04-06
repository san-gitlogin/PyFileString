from configProcessing import read_config

# ------ TERMINAL INTERACTION ------ #

def process_input(input_config_file, input_text_file):
    try:
        result = read_config(config_path = input_config_file, file_path = input_text_file)
        print(f"\n{result}")
    except Exception as e:
        print(f"Found exception: \n{e}")

input_text_file = input("Enter the path to text file: \n")
input_config_file = input("Enter the path to config file: \n")

if input_text_file and input_config_file:
    process_input(input_config_file, input_text_file)
else:
    print("Enter valid input")

