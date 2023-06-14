class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.tokens = []

    def error(self):
        raise Exception("Invalid character")
    
    def get_tokens(self):
        return self.tokens

    def get_keyword(self):
        keyword = ""
        while self.pos < len(self.text) and self.text[self.pos].isalpha():
            keyword += self.text[self.pos]
            self.pos += 1
        return keyword

    def get_next_token(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.text):
            return Token("EOF", None)

        current_char = self.text[self.pos]

        if current_char.isalpha():
            keyword = self.get_keyword()
            if keyword.lower() == 'size':
                token = Token("SIZE", keyword)
            elif keyword.lower() == 'color':
                token = Token("COLOR", keyword)
            elif keyword.lower() == 'background':
                token = Token("BACKGROUND", keyword)
            elif keyword.lower() == 'shape':
                token = Token("SHAPE", keyword)
            elif keyword.lower() == 'scale':
                token = Token("SCALE", keyword)
            elif keyword.lower() == 'rotate':
                token = Token("ROTATE", keyword)
            elif keyword.lower() == 'draw':
                token = Token("DRAW", keyword)
            else:
                self.error()
            # self.pos += len(keyword)
            self.tokens.append(token)
            return token

        if current_char.isdigit():
            num = ""
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                num += self.text[self.pos]
                self.pos += 1
            token = Token("NUMBER", int(num))
            self.tokens.append(token)
            return token

        if current_char in ['\'', '"']:
            quote_char = current_char
            string = ""
            self.pos += 1
            while self.pos < len(self.text) and self.text[self.pos] != quote_char:
                string += self.text[self.pos]
                self.pos += 1
            self.pos += 1
            token = Token("STRING", string)
            self.tokens.append(token)
            return token

        self.error()