# CLI File Search Tool

This is a command-line tool for searching for files in a given directory. It allows for searching by name or extension, and also includes fuzzy search functionality to allow for more flexible searching.

## Prerequisites

To run this tool, you'll need to have Python 3 installed on your machine. You'll also need to install the `argparse` and `fuzzywuzzy` packages using pip:

```bash
pip install argparse fuzzywuzzy
```


## Usage

To use the tool, open a terminal window and navigate to the directory containing the `search.py` file. Then, run the following command:


```bash
python search.py [-h] [-f FILE] [-e EXTENSION] [-fz FUZZY] [-p PATH]
```


The tool takes several optional arguments:

- `-h`, `--help`: Shows the help message and exits.
- `-f FILE`, `--file FILE`: The name of the file to search for.
- `-e EXTENSION`, `--extension EXTENSION`: The file extension to search for. You can specify multiple extensions separated by commas.
- `-fz FUZZY`, `--fuzzy FUZZY`: A fuzzy search query for the file name.
- `-p PATH`, `--path PATH`: The path to start searching from. If not specified, the tool will search in the current directory.

### Examples

To search for a file named `main.py` in the current directory and its subdirectories:


To search for all Python files in the `/home/user/projects` directory and its subdirectories:

** its important to note that sometimes you will need to put the `search.py` file in the root directory


## Limitations

This tool has a few limitations to keep in mind:

- The search functionality only works with files, not directories.
- The fuzzy search algorithm may not always return the expected results, particularly if the search query is very similar to multiple file names in the directory. It's recommended
