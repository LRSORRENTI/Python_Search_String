import os

def search_string_in_file(file_path, search_string):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, 1):
            if search_string in line:
                print(f"Found '{search_string}' in file: {file_path} on line {line_number}")

def search_string_in_directory(directory, search_string):
    for root, dirs, files in os.walk(directory):
        # Exclude node_modules directory to search through as it's usually massive
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if 'package-lock.json' in dirs:
            dirs.remove('package-lock.json')
        for file in files:
            if file.endswith(('.js', '.jsx', '.ts', '.tsx', '.html', '.css', '.json', '.txt', '.py',)):  # Add other file extensions if needed
                file_path = os.path.join(root, file)
                search_string_in_file(file_path, search_string)

def main():
    directory = input("Enter the path to the repository: ")
    search_string = input("Enter the string to search for: ")
    search_string_in_directory(directory, search_string)

if __name__ == "__main__":
    main()
