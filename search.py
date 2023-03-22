# !/usr/bin/python
import os
import argparse
from fuzzywuzzy import fuzz

argparser = argparse.ArgumentParser(description='Search for files')

argparser.add_argument('-f', '--file', help='File to search for')

argparser.add_argument('-e', '--extension', help='File extensions to search for')

argparser.add_argument('-fz','--fuzzy', help='Fuzzy search query for file name (e.g. "main.py" will match "main.py", "main.pyc", "main.pyo", etc.')

argparser.add_argument('-p', '--path', help='Path to start searching')
 
args = argparser.parse_args()

file_name = args.file
extensions = args.extension.split(',') if args.extension else None
path = args.path
fuzzy = args.fuzzy

if path:
  for dirpath, dirnames, filenames in os.walk('.'):
    for filename in [f for f in filenames if f == file_name]:
      print(os.path.join(dirpath, filename))

if extensions:
  for dirpath, dirnames, filenames in os.walk('.'):
    for filename in [f for f in filenames if f.endswith(tuple(extensions))]:
      print(os.path.join(dirpath, filename))

if fuzzy:
  for dirpath, dirnames, filenames in os.walk('.'):
    for filename in [f for f in filenames if fuzz.ratio(fuzzy, f) > 40]:
      print(os.path.join(dirpath, filename))
