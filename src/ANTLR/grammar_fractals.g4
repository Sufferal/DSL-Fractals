grammar grammar_fractals;

program : statement | statement program;

statement : size_statement
          | color_statement
          | angle_statement
          | iterations_statement
          | shape_statement
          | move_statement
          | scale_statement
          | rotate_statement
          | mirror_statement
          | draw_statement
          | save_statement;

size_statement : 'size' value;
color_statement : 'color' value;
angle_statement : 'angle' value;
iterations_statement : 'iterations' value;
shape_statement : 'shape' shape;
move_statement : 'move' value value;
scale_statement : 'scale' value;
rotate_statement : 'rotate' value;
mirror_statement : 'mirror' axis;

axis : 'x' | 'y';

draw_statement : 'draw';
save_statement : 'save' filename;


shape : 'circle' | 'square' | 'triangle' | 'polygon';

digit : '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';
string : char | char string;

filename : STRING;
value : (DIGIT | STRING)* ;
char : LETTER | DIGIT | EQ | DOT | COMMA | LBRACK | RBRACK | SPACE | UNDERSCORE ;

STRING : '"' (ESC | ~["\\])* '"' ;
DIGIT : [0-9] ;
LETTER : [a-zA-Z] ;
EQ : '=' ;
DOT : '.' ;
COMMA : ',' ;
LBRACK : '[' ;
RBRACK : ']' ;
SPACE : ' ' ;
UNDERSCORE : '_' ;
ESC : '\\' ["\\/bfnrt] ;


