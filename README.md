# Search for string in repository

***This Python script searches for a specified string within all files of a repository, excluding the node_modules directory, but you can change or add directories to omit the search. It outputs the file paths and line numbers where the specified string is found.***

## Features

- Recursively searches through all files and nested folders in a repository.

- Ignores the node_modules directory to improve performance.

- Searches within files with extensions: .js, .jsx, .ts, .tsx, .html, .css, and .json.

- Outputs the location (file path and line number) of each instance of the specified string.

### Prerequisites
- Python 3.x must be installed on your machine.

### Usage

1. Make any necessary repository omits within the script file, by default it excludes searching through node_modules

2. Run the script
```
python search_string.py
```

3. Follow the Prompts:

- Enter the appropriate file path to your repository when prompted.
```
C:\Users\username\Desktop\projects\my-app
```
- Enter the string you want to search for.
```
Hello world
```
```
Found 'Hello world' in file: C:\Users\username\Desktop\projects\my-app\index.html on line 10
Found 'Hello world' in file: C:\Users\username\Desktop\projects\my-app\script.js on line 1
Found 'Hello world' in file: C:\Users\username\Desktop\projects\my-app\style.css on line 7
```

### Python:
```
import os

def search_string_in_file(file_path, search_string):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines, 1):
            if search_string in line:
                print(f"Found '{search_string}' in file: {file_path} on line {line_number}")

def search_string_in_directory(directory, search_string):
    for root, dirs, files in os.walk(directory):
        # Exclude node_modules directory
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        for file in files:
            if file.endswith(('.js', '.jsx', '.ts', '.tsx', '.html', '.css', '.json')):  # Add other file extensions if needed
                file_path = os.path.join(root, file)
                search_string_in_file(file_path, search_string)

def main():
    directory = input("Enter the path to the repository: ")
    search_string = input("Enter the string to search for: ")
    search_string_in_directory(directory, search_string)

if __name__ == "__main__":
    main()
```

### Notes

**The script currently searches for the specified string in files with the following extensions: .js, .jsx, .ts, .tsx, .html, .css, and .json. You can modify the file extensions list in the script to suit the specific types of files you want to search through in your project.**

Ensure you have the necessary permissions to read the files in the specified directory.

### Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

