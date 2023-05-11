import ply.lex as lex
import ply.yacc as yacc


# List of reserved tokens
reserved = {
    'size': 'SIZE',
    'color': 'COLOR',
    'angle': 'ANGLE',
    'iterations': 'ITERATIONS',
    'shape': 'SHAPE',
    'circle': 'CIRCLE',
    'square': 'SQUARE',
    'polygon': 'POLYGON',
    'move': 'MOVE',
    'scale': 'SCALE',
    'rotate': 'ROTATE',
    'mirror': 'MIRROR',
    'draw': 'DRAW',
    'save': 'SAVE',
    'triangle': 'TRIANGLE'
}

# Define tokens
tokens = [
    'NUMBER', 'X_AXIS', 'Y_AXIS', 'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'DOT',
    'COMMA',
    'APOSTROPHE',
    'QUOTATION'
] + list(reserved.values())

# Define token patterns
t_STRING = r'[a-zA-Z][a-zA-Z0-9_]*'
t_X_AXIS = r'x'
t_Y_AXIS = r'y'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOT = r'\.'
t_COMMA = r'\,'
t_APOSTROPHE = r"\'"
t_QUOTATION = r'\"'

# Rule for reserved words
def t_SIZE(t):
    r'size'
    return t


def t_COLOR(t):
    r'color'
    return t


def t_ANGLE(t):
    r'angle'
    return t


def t_SHAPE(t):
    r'shape'
    return t


def t_ITERATIONS(t):
    r'iterations'
    return t


def t_CIRCLE(t):
    r'circle'
    return t


def t_SQUARE(t):
    r'square'
    return t


def t_POLYGON(t):
    r'polygon'
    return t


def t_MOVE(t):
    r'move'
    return t


def t_SCALE(t):
    r'scale'
    return t


def t_ROTATE(t):
    r'rotate'
    return t


def t_MIRROR(t):
    r'mirror'
    return t


def t_DRAW(t):
    r'draw'
    return t


def t_SAVE(t):
    r'save'
    return t


def t_TRIANGLE(t):
    r'triangle'
    return t

# Rule for comments
def t_COMMENT(t):
    r'\#.*'
    pass


# Compute column
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) - 1


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Define the grammar
def p_program(p):
    '''program : statement
               | statement program'''


def p_statement(p):
    '''statement : size_statement
                 | color_statement
                 | angle_statement
                 | iterations_statement
                 | shape_statement
                 | move_statement
                 | scale_statement
                 | rotate_statement
                 | mirror_statement
                 | draw_statement
                 | save_statement'''


def p_size_statement(p):
    '''size_statement : SIZE NUMBER'''


def p_color_statement(p):
    '''color_statement : COLOR LPAREN NUMBER COMMA NUMBER COMMA NUMBER COMMA RPAREN
                       | COLOR NUMBER
                       | COLOR QUOTATION STRING QUOTATION
                       | COLOR APOSTROPHE STRING APOSTROPHE'''


def p_angle_statement(p):
    '''angle_statement : ANGLE NUMBER'''


def p_iterations_statement(p):
    '''iterations_statement : ITERATIONS NUMBER'''


def p_shape_statement(p):
    '''shape_statement : SHAPE shape'''


def p_move_statement(p):
    '''move_statement : MOVE NUMBER NUMBER'''


def p_scale_statement(p):
    '''scale_statement : SCALE NUMBER'''


def p_rotate_statement(p):
    '''rotate_statement : ROTATE NUMBER'''


def p_mirror_statement(p):
    '''mirror_statement : MIRROR axis'''


def p_draw_statement(p):
    '''draw_statement : DRAW'''


def p_save_statement(p):
    '''save_statement : SAVE STRING'''


def p_shape(p):
    '''shape : CIRCLE
             | SQUARE
             | TRIANGLE
             | POLYGON'''


def p_axis(p):
    '''axis : X_AXIS
            | Y_AXIS'''


# Define the parser error handling function
def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno-7}: unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")


# Create the lexer
lexer = lex.lex()

# Create the parser
parser = yacc.yacc()

# Initialize the symbol table
symbol_table = {}


# Define a function to add variables to the symbol table
def add_variable(name, value, data_type, scope):
    if name in symbol_table:
        raise Exception(f"Error: Variable {name} already exists in the symbol table.")
    else:
        symbol_table[name] = {'value': value, 'type': data_type, 'scope': scope}


# Define a function to get the value of a variable from the symbol table
def get_variable_value(name, scope):
    if name in symbol_table:
        if symbol_table[name]['scope'] == scope:
            return symbol_table[name]['value']
        else:
            raise Exception(f"Error: Variable {name} is not defined in the current scope.")
    else:
        raise Exception(f"Error: Variable {name} is not defined.")


# Define a function to set the value of a variable in the symbol table
def set_variable_value(name, value, scope):
    if name in symbol_table:
        if symbol_table[name]['scope'] == scope:
            symbol_table[name]['value'] = value
        else:
            raise Exception(f"Error: Variable {name} is not defined in the current scope.")
    else:
        raise Exception(f"Error: Variable {name} is not defined.")


# Define a function to analyze a program
def analyze_program(program, lexer):
    # TODO: take the tokens into parser
    try:
        # Parse the program
        parsed_result = parser.parse(program, lexer=lexer)
        # Analyze the symbol table
        for variable in symbol_table:
            # Check if a variable has been assigned a value
            if symbol_table[variable]['value'] is None:
                raise Exception(f"Error: Variable {variable} has not been assigned a value.")

            # Check if a variable is used in the correct context
            if symbol_table[variable]['type'] == 'size':
                if symbol_table[variable]['value'] <= 0:
                    raise Exception(f"Error: Size value of {variable} should be greater than 0.")
            elif symbol_table[variable]['type'] == 'color':
                if symbol_table[variable]['value'] < 0 or symbol_table[variable]['value'] > 255:
                    raise Exception(f"Error: Color value of {variable} should be between 0 and 255.")
            elif symbol_table[variable]['type'] == 'angle':
                if symbol_table[variable]['value'] < 0 or symbol_table[variable]['value'] > 360:
                    raise Exception(f"Error: Angle value of {variable} should be between 0 and 360.")
            elif symbol_table[variable]['type'] == 'iterations':
                if symbol_table[variable]['value'] < 1:
                    raise Exception(f"Error: Iterations value of {variable} should be greater than 0.")

        print(f"[Status] Program parsed successfully.")
    except Exception as e:
        print(f"Parsing failed with error: {e}")
        return False

    return True


if __name__ == '__main__':
    # # Add variables to the symbol table
    # add_variable('canvas_size', 1000, 'size', 'global')
    # add_variable('fractal_color', 0, 'color', 'global')
    # add_variable('number_of_iterations', 10, 'iterations', 'global')
    # add_variable('fractal_shape', 'triangle', 'shape', 'global')
    #
    # # Get the values of variables from the symbol table
    # canvas_size = get_variable_value('canvas_size', 'global')
    # fractal_color = get_variable_value('fractal_color', 'global')
    # number_of_iterations = get_variable_value('number_of_iterations', 'global')
    # fractal_shape = get_variable_value('fractal_shape', 'global')


    # Extracting code from file
    file = open('source.txt', 'r')
    data = file.read()
    lexer.input(data)
    # Debugging purpose
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    # program = data.format(canvas_size, fractal_color, number_of_iterations, fractal_shape)

    # Analyze the program
    analyze_program(data, lexer)
    # analyze_program(program, lexer)
    # Print the symbol table
    # print("Symbol table:")
    # for key, value in symbol_table.items():
    #     print(key, value)
