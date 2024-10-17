import json
import os

def extract_field(input_file: str, output_file: str, field: str):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            try:
                data = json.loads(line.strip())
                if data["results"][0]["Status"] == "Ok":
                    field_value = data["results"][0][field]
                    outfile.write(f"{field_value}\n")  # Write each D_cm value to a new line
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error parsing line: {line.strip()} - {e}")


def process_directory(input_directory, output_directory, field):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_directory, filename)
            output_file = os.path.join(output_directory, f"{field}_{filename}.txt")
            print(f"Processing {filename}...")
            extract_field(input_file, output_file, field)
            print(f"Saved {field} readings to {output_file}")


if __name__ == "__main__":
    input_directory = input("Enter the input directory: ")
    output_directory = input("Enter the output directory: ")
    field = input("Enter the field (singular) of the logs to process: ")

    process_directory(input_directory, output_directory, field)
