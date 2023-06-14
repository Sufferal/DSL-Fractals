class Parser:
    def __init__(self, lexer, fractal):
        self.lexer = lexer
        self.fractal = fractal
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception("Invalid syntax")

    def match(self, expected_token_type):
        if self.current_token.type == expected_token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def parse(self):
        self.parse_commands()

    def parse_commands(self):
        while self.current_token.type != "EOF":
            self.parse_command()

    def parse_command(self):
        command = self.current_token.value.lower()
        if command == 'size':
            self.match("SIZE")
            size_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.set_size(int(size_value))
        elif command == 'color':
            self.match("COLOR")
            color_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_color(color_value.strip("'").strip('"'))
        elif command == 'background':
            self.match("BACKGROUND")
            background_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_background(background_value.strip("'").strip('"'))
        elif command == 'shape':
            self.match("SHAPE")
            shape_value = self.current_token.value
            self.match("STRING")
            self.fractal.set_shape(shape_value.strip("'").strip('"'))
        elif command == 'draw':
            self.match("DRAW")
            draw_value = self.current_token.value
            self.match("NUMBER")
            self.fractal.draw()
        else:
            self.error()