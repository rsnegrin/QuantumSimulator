import sys
import  ply.yacc as yacc
import ply.lex as lex
from Parser.parser import *
from Parser.lexer import *

def simulate(qasm_string):
    lexer = lex.lex()
    parser = yacc.yacc()
    qc = parser.parse(qasm_string)
    print(qc)
    result = qc.run()
    parser.restart()
    return result


if __name__ == "__main__":
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            # Reads the file from the command line
            data = file.read() 
            # Parses the data and builds the circuit
            result = simulate(data)
            print("Final state:", result)
    except FileNotFoundError:
        print(f"File not found: {filename}")

