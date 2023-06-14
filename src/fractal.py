import turtle

class Fractal:
    def __init__(self):
        self.size = 700  # default size
        self.color = 'black'  # default color
        self.shape = 'triangle'  # default shape
        self.background = 'white'  # default background color

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def set_shape(self, shape):
        self.shape = shape

    def set_background(self, background):
        self.background = background

    def draw(self):
        turtle.setup(width=self.size, height=self.size)
        turtle.bgcolor(self.background)
        turtle.speed(0)  # Set the turtle's speed to the fastest
        turtle.color(self.color)

        def start_at(x, y):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

        if self.shape == 'triangle':
            start_at(-self.size/2, -self.size/4)
            self.draw_sierpinski_triangle(self.size)
        elif self.shape == 'snowflake':
            start_at(-self.size/2, self.size/4)
            self.draw_koch_snowflake(self.size, 4)
        elif self.shape == 'dragon':
            start_at(0, 0)
            self.draw_dragon_curve(self.size * 10, 10)
        elif self.shape == 'custom':
            start_at(-self.size/2, 0)
            self.draw_custom_figure()

        turtle.done()

    def draw_sierpinski_triangle(self, side_length, depth=5):
        if depth == 0:
            for _ in range(3):
                turtle.forward(side_length)
                turtle.left(120)
        else:
            self.draw_sierpinski_triangle(side_length/2, depth-1)
            turtle.forward(side_length/2)
            self.draw_sierpinski_triangle(side_length/2, depth-1)
            turtle.backward(side_length/2)
            turtle.left(60)
            turtle.forward(side_length/2)
            turtle.right(60)
            self.draw_sierpinski_triangle(side_length/2, depth-1)
            turtle.left(60)
            turtle.backward(side_length/2)
            turtle.right(60)

    def draw_koch_snowflake(self, side_length, depth=3):
        for _ in range(3):
            self.draw_koch_curve(side_length, depth)
            turtle.right(120)

    def draw_koch_curve(self, length, depth):
        if depth == 0:
            turtle.forward(length)
        else:
            self.draw_koch_curve(length/3, depth-1)
            turtle.left(60)
            self.draw_koch_curve(length/3, depth-1)
            turtle.right(120)
            self.draw_koch_curve(length/3, depth-1)
            turtle.left(60)
            self.draw_koch_curve(length/3, depth-1)

    def draw_dragon_curve(self, length, depth):
        if depth == 0:
            turtle.forward(length)
        else:
            self.draw_dragon_curve(length/2, depth-1)
            turtle.right(90)
            self.draw_inverse_dragon_curve(length/2, depth-1)

    def draw_inverse_dragon_curve(self, length, depth):
        if depth == 0:
            turtle.forward(length)
        else:
            self.draw_dragon_curve(length/2, depth-1)
            turtle.left(90)
            self.draw_inverse_dragon_curve(length/2, depth-1)

    def draw_custom_figure(self):
        # Customize this method to draw your desired figure
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(45)
        turtle.forward(75)
        turtle.right(90)
        turtle.forward(100)