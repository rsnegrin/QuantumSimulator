import ply.yacc as yacc
from Models.Circuit import QuantumCircuit

# Get the token map from the lexer
from .lexer import tokens

# This runs the program 
def p_program(p):
    '''program : OPENQASM FLOAT SEMICOLON include qreg creg statements'''
    p[0] = ('program', p[2], p[4], p[5], p[6], p[7])


    # Create a new circuit with the given number of qubits and bits
    circuit = QuantumCircuit(p[5], p[6])

    # Add the gates and other statements to the circuit
    for gate in p[7]:
        circuit.add_gate(gate)

    # Print the final circuit
    print("Final Quantum Circuit:")
    print(circuit)
    # The result of the rule
    p[0] = circuit

# Reads the include statement
def p_include(p):
    '''include : INCLUDE STRING SEMICOLON'''
    p[0] = ('include', p[2])


# Reads the number of qubits
def p_qreg(p):
    '''qreg : QREG IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON'''
    p[0] = p[4]


# Reads the number of classical bits
def p_creg(p):
    '''creg : CREG IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON'''
    p[0] = p[4]

# Concatenates the statements
def p_statements(p):
    '''statements : statement statements
                  | '''
    if len(p) > 1:
        p[0] = [p[1]] + (p[2] if p[2] is not None else [])

# Reads the gate and the number of the qubits
def p_statement(p):
    '''statement : GATE_H IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON
                 | GATE_X IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON
                 | GATE_T IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON
                 | GATE_TDG IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON
                 | GATE_CX IDENTIFIER LBRACKET NUMBER RBRACKET COMMA IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON'''
    if len(p) == 7:
        # Single-qubit gate
        p[0] = (p[2], p[4])
    elif len(p) == 12:
        # Multi-qubit gate (e.g., CNOT)
        p[0] = (p[1], p[4], p[9])
    

# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} with value '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")


# Build the parser
parser = yacc.yacc()