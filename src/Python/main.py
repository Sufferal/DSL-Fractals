import ply.lex as lex
import ply.yacc as yacc

# Define tokens
tokens = [
    'SIZE', 'COLOR', 'ANGLE', 'ITERATIONS', 'SHAPE', 'CIRCLE', 'SQUARE', 'TRIANGLE', 'POLYGON', 'MOVE', 
    'SCALE', 'ROTATE', 'MIRROR', 'DRAW', 'SAVE', 'STRING', 'DIGIT', 'X_AXIS', 'Y_AXIS'
]

# Define token patterns
t_SIZE = r'size'
t_COLOR = r'color'
t_ANGLE = r'angle'
t_ITERATIONS = r'iterations'
t_SHAPE = r'shape'
t_MOVE = r'move'
t_SCALE = r'scale'
t_CIRCLE = r'circle'
t_SQUARE = r'square'
t_TRIANGLE = r'triangle'
t_POLYGON = r'polygon'
t_ROTATE = r'rotate'
t_MIRROR = r'mirror'
t_DRAW = r'draw'
t_SAVE = r'save'
t_STRING = r'\".*?\"'
t_DIGIT = r'\d+'
t_X_AXIS = r'x'
t_Y_AXIS = r'y'

# Define the grammar
def p_program(p):
    '''program : statement
               | statement program'''
    pass

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
    pass

def p_size_statement(p):
    '''size_statement : SIZE value'''
    pass

def p_color_statement(p):
    '''color_statement : COLOR value'''
    pass

def p_angle_statement(p):
    '''angle_statement : ANGLE value'''
    pass

def p_iterations_statement(p):
    '''iterations_statement : ITERATIONS value'''
    pass

def p_shape_statement(p):
    '''shape_statement : SHAPE shape'''
    pass

def p_move_statement(p):
    '''move_statement : MOVE value value'''
    pass

def p_scale_statement(p):
    '''scale_statement : SCALE value'''
    pass

def p_rotate_statement(p):
    '''rotate_statement : ROTATE value'''
    pass

def p_mirror_statement(p):
    '''mirror_statement : MIRROR axis'''
    pass

def p_draw_statement(p):
    '''draw_statement : DRAW'''
    pass

def p_save_statement(p):
    '''save_statement : SAVE filename'''
    pass

def p_filename(p):
    '''filename : STRING'''
    pass

def p_shape(p):
    '''shape : CIRCLE
             | SQUARE
             | TRIANGLE
             | POLYGON'''
    pass

def p_value(p):
    '''value : DIGIT
             | DIGIT value
             | STRING'''
    pass

def p_axis(p):
    '''axis : X_AXIS
            | Y_AXIS'''
    pass

# Define error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Define the parser error handling function
def p_error(p):
    if p:
        print("Syntax error at line %d, position %d: unexpected token '%s'" % (p.lineno, p.lexpos, p.value))
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
def analyze_program(program):
    try:
        # Parse the program
        parsed_result = parser.parse(program)

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
    # Add variables to the symbol table
    add_variable('canvas_size', 1000, 'size', 'global')
    add_variable('fractal_color', 0, 'color', 'global')
    add_variable('number_of_iterations', 10, 'iterations', 'global')
    add_variable('fractal_shape', 'circle', 'shape', 'global')

    # Get the values of variables from the symbol table
    canvas_size = get_variable_value('canvas_size', 'global')
    fractal_color = get_variable_value('fractal_color', 'global')
    number_of_iterations = get_variable_value('number_of_iterations', 'global')
    fractal_shape = get_variable_value('fractal_shape', 'global')

    test = 'size{}color{}angle90iterations{}shape{}scale2rotate180draw'.format(canvas_size, fractal_color, number_of_iterations, fractal_shape)

    # Analyze the program
    analyze_program(test)

    # Print the symbol table
    print("Symbol table:")
    for key, value in symbol_table.items():
      print(key, value)
