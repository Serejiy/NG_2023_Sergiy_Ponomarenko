import argparse
import os

def find_files(folder, file_name):
    found_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file_name in file:
                found_files.append(os.path.join(root, file))
    return found_files

parser = argparse.ArgumentParser(description='Searching for files in folder')
parser.add_argument('--folder', type=str, help='Path to folder, for the searched files')
parser.add_argument('--file', type=str, help='Name of the file to search')

args = parser.parse_args()

if args.folder and args.file:
    files = find_files(args.folder, args.file)
    if files:
        print(f'Found {len(files)} files:')
        for file in files:
            print(file)
    else:
        print(f'Files with name "{args.file}" not found in folder "{args.folder}".')
else:
    print("Enter the path to folder and name of the file for searching\nExample: python rfind.py --folder 'your folder here' --file 'your file here'")
