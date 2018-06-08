from pygame import Rect, draw

class Squares:
    def __init__(self, st, screen):
        self.st = st
        self.screen = screen
        self.squares = [[False for i in range(st.square_num_x)]
                        for j in range(st.square_num_y)]

    def get_square(self):
        return self.st.new

    def draw_squares(self, curr_sq, shape, st):
        self.draw_exist_sq(self)
        self.draw_curr_sq(self, curr_sq, shape)

    @staticmethod
    def draw_exist_sq(self):
        for y, row in enumerate(self.squares):
            for x, square in enumerate(row):
                self.draw_square(self, y, x, square)

    @staticmethod
    def draw_curr_sq(self, curr_sq, squares):
        self.draw_square(self, curr_sq[0], curr_sq[1], True)
        curr_y, curr_x = curr_sq[0], curr_sq[1]
        for y, x in squares:
            self.draw_square(self, y+curr_y, x+curr_x, True)

    @staticmethod
    def draw_square(self, y, x, square):
        x_pos = x * (self.st.square_space + self.st.square_length)
        y_pos = y * (self.st.square_space + self.st.square_length)
        rect = Rect(x_pos, y_pos, self.st.square_length, self.st.square_length)
        if square:
            draw.rect(self.screen, self.st.square_color, rect)
        else:
            draw.rect(self.screen, self.st.square_null_color, rect)
