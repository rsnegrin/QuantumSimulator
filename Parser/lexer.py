

# List of token names. 
tokens = (
   'OPENQASM',
   'INCLUDE',
   'QREG',
   'CREG',
   'GATE_H',
   'GATE_X',
   'GATE_T',
   'GATE_TDG',
   'GATE_CX',
   'IDENTIFIER',
    'STRING',
   'NUMBER',
   'SEMICOLON',
   'COMMA',
   'LBRACKET',
   'RBRACKET',
)

# Regular expression rules for simple tokens
t_SEMICOLON = r';'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_ignore = ' \t'  # A string containing ignored characters (spaces and tabs)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_OPENQASM(t):
    r'OPENQASM\s2\.0|\d+\.\d+'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  
    return t

def t_QREG(t):
    r'qreg'
    return t

def t_CREG(t):
    r'creg'
    return t

# Rules for gates
def t_GATE_H(t):
    r'h'
    return t

def t_GATE_X(t):
    r'x'
    return t

def t_GATE_TDG(t):
    r'tdg'
    return t

def t_GATE_T(t):
    r't'
    return t

def t_GATE_CX(t):
    r'cx'
    return t

# Rule for variable names 
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Int
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)