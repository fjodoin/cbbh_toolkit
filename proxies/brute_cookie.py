import sys

# Specify the file path and open the file for reading (default mode)
file_path = ''  # Replace with your file path
try:
    with open(file_path, 'r') as file:
        # Perform operations on the file here
        # The 'with' statement ensures that the file is properly closed when done
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
