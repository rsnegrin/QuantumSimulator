import sys
# Loads the parser from the Parser folder
from Parser.parser import parser

if __name__ == "__main__":
    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            # Reads the file from the command line
            data = file.read()

            # Parses the data and builds the circuit
            circuti = parser.parse(data)
    except FileNotFoundError:
        print(f"File not found: {filename}")
