from random import randrange
from pygame import Rect, draw
from clock import Clock

class Squares:
    """method for malipulating squares in the game"""
    def __init__(self, st, status, screen):
        self.st = st
        self.status = status
        self.screen = screen
        self.empty_line = ['none' for i in range(st.square_num_x)]
        self.squares = [self.empty_line.copy() for i in range(st.square_num_y)]
        self.new_sq(self)
        self.clock = Clock(st)

    # draw all squares
    def draw_squares(self):
        self.screen.fill(self.st.space_color)
        self.draw_tip(self)
        self.draw_exist_sq(self)
        self.draw_curr_sq(self)

    # update squares' information
    def update(self):
        updated = False # for update screen
        # vertical drop, straight drop
        if self.status.straight_drop and self.clock.is_time_to_straight_drop():
            updated = True
            self.drop_straight(self)
            self.clock.update_straight_drop()
        # vertical drop, force drop
        elif self.clock.is_time_to_drop():
            updated = True
            self.drop(self)
            self.clock.update_drop()
        # vertical drop, quick drop
        elif self.status.down and self.clock.is_time_to_quick_drop():
            updated = True
            self.drop(self)
            self.clock.update_quick_drop()
        # rotation
        if self.status.rotate and self.clock.is_time_to_rotate():
            updated = True
            self.rotate(self)
            self.clock.update_rotate()
        # horizontal move
        if self.status.right:
            updated = True
            if self.clock.is_time_to_move() or self.clock.is_time_to_quick_right():
                self.right(self)
            self.clock.update_move()
        if self.status.left:
            updated = True
            if self.clock.is_time_to_move() or self.clock.is_time_to_quick_left():
                self.left(self)
            self.clock.update_move()
        # crash detection
        if self.should_stop(self):
            updated = True
            self.stop(self)
        return updated

    # renew current square
    @staticmethod
    def new_sq(self):
        self.curr_sq = self.st.new.copy()
        shape = self.get_shape(self)
        self.origin_shape = shape['pos']
        self.curr_shape = shape['pos']
        self.curr_color = shape['color']
        self.rotate_limit = shape['rotate']
        self.rotate_curr = 1
        # if new squares are crashed, game over.
        if not self.valid(self, self.curr_sq, self.curr_shape):
            self.status.game_status = self.status.GAMEOVER

    # return a random shape dictionary
    @staticmethod
    def get_shape(self):
        shape_index = randrange(0, self.st.shape_num)
        return self.st.shapes[shape_index].copy()

    @staticmethod
    def drop_straight(self):
        while not self.should_stop(self):
            self.curr_sq[0] += 1

    @staticmethod
    def drop(self):
        new_sq = self.curr_sq.copy()
        new_sq[0] += 1
        if self.valid(self, new_sq, self.curr_shape):
            self.curr_sq = new_sq

    @staticmethod
    def rotate(self):
        new_shape = self.get_rotated_shape(self)
        # regular check
        if self.valid(self, self.curr_sq, new_shape):
            self.curr_shape = new_shape
        # move horizontally if not valid
        else:
            tolerance = 2
            for i in range(tolerance):
                # left
                new_sq_left = self.curr_sq.copy()
                new_sq_left[1] -= 1
                if self.valid(self, new_sq_left, new_shape):
                    self.curr_sq = new_sq_left
                    self.curr_shape = new_shape
                    return
                # right
                new_sq_right = self.curr_sq.copy()
                new_sq_right[1] += 1
                if self.valid(self, new_sq_right, new_shape):
                    self.curr_sq = new_sq_right
                    self.curr_shape = new_shape
                    return


    @staticmethod
    def get_rotated_shape(self):
        # rotation limit must not exceed, if exceed, reset it
        if self.rotate_curr >= self.rotate_limit:
            self.rotate_curr = 1
            new_shape = self.origin_shape
        else:
            self.rotate_curr += 1
            new_shape = []
            for sq in self.curr_shape:
                new_shape.append([sq[1], -sq[0]])
        return new_shape

    @staticmethod
    def right(self):
        new_sq = self.curr_sq.copy()
        new_sq[1] += 1
        if self.valid(self, new_sq, self.curr_shape):
            self.curr_sq = new_sq

    @staticmethod
    def left(self):
        new_sq = self.curr_sq.copy()
        new_sq[1] -= 1
        if self.valid(self, new_sq, self.curr_shape):
            self.curr_sq = new_sq

    @staticmethod
    def stop(self):
        # wait for a moment before stop, give player time to adjust
        if not self.clock.is_time_to_stop():
            self.clock.update_should_stop(True)
            return
        else:
            self.clock.update_should_stop(None)
            self.clock.update_stop()
        # copy squares to map
        for sq in self.curr_shape:
            x = sq[1] + self.curr_sq[1]
            y = sq[0] + self.curr_sq[0]
            if y >= 0:
                self.squares[y][x] = self.curr_color
        x = self.curr_sq[1]
        y = self.curr_sq[0]
        if y >= 0:
            self.squares[y][x] = self.curr_color
        full_lines = self.clean_full_lines(self)
        self.status.score += full_lines  # add score
        self.new_sq(self)

    # delete full lines and insert empty lines at the front
    @staticmethod
    def clean_full_lines(self):
        full_lines = 0
        for index, line in enumerate(self.squares):
            if line.count('none') == 0:
                full_lines += 1
                self.st.time_drop *= self.st.time_drop_adjust # adjust time
                self.squares.pop(index)
                self.squares.insert(0, self.empty_line.copy())
        return full_lines

    # validate current squares of shapes relative to center with with one drop vertically
    @staticmethod
    def should_stop(self):
        # check shape squares
        for sq in self.curr_shape:
            x = sq[1] + self.curr_sq[1]
            y = sq[0] + self.curr_sq[0] + 1
            if y - 1 >= 0 and not self.valid_sq(self, [y, x]):
                return True
        # check center square
        x = self.curr_sq[1]
        y = self.curr_sq[0] + 1
        return not (self.valid_sq(self, [y, x]))

    # validate the given center square and shape squires relative to center square
    @staticmethod
    def valid(self, square, shape):
        # check shape squares
        for sq in shape:
            x = sq[1] + square[1]
            y = sq[0] + square[0]
            if y >= 0 and not (self.valid_sq(self, [y, x])):
                return False
        # check center square
        return self.valid_sq(self, square)

    @staticmethod
    def valid_sq(self, sq):
        # check border
        if sq[0] >= self.st.square_num_y or \
                        sq[1] >= self.st.square_num_x or \
                        sq[1] < 0:
            return False
        # check crash
        return self.squares[sq[0]][sq[1]] == 'none'

    @staticmethod
    def draw_exist_sq(self):
        for y, row in enumerate(self.squares):
            for x, square in enumerate(row):
                color = self.st.colors[self.squares[y][x]]
                self.draw_square(self, y, x, color)

    @staticmethod
    def draw_tip(self):
        # find the lowrest position
        curr_sq = self.curr_sq.copy()
        while not self.should_stop(self):
            self.curr_sq[0] += 1
        curr_sq, self.curr_sq = self.curr_sq, curr_sq

        # draw their tips
        color = self.st.colors['tip']
        self.draw_square(self, curr_sq[0], curr_sq[1], color, True)
        self.draw_square(self, curr_sq[0], curr_sq[1], self.st.colors['none'])
        for y, x in self.curr_shape:
            curr_y, curr_x = curr_sq[0], curr_sq[1]
            self.draw_square(self, y + curr_y, x + curr_x, color, True)
            self.draw_square(self, y + curr_y, x + curr_x, self.st.colors['none'])

    @staticmethod
    def draw_curr_sq(self):
        # draw center
        color = self.st.colors[self.curr_color]
        self.draw_square(self, self.curr_sq[0], self.curr_sq[1], color)
        # draw shapes
        curr_y, curr_x = self.curr_sq[0], self.curr_sq[1]
        for y, x in self.curr_shape:
            self.draw_square(self, y + curr_y, x + curr_x, color)

    # draw one single square with given information
    @staticmethod
    def draw_square(self, y, x, color, border=False):
        x_pos = x * (self.st.square_space + self.st.square_length)
        y_pos = y * (self.st.square_space + self.st.square_length)
        length = self.st.square_length
        # adding borders borders
        if border:
            y_pos -= self.st.square_space
            x_pos -= self.st.square_space
            length += 2 * self.st.square_space
        rect = Rect(x_pos + self.st.square_space, y_pos + self.st.square_space, length, length)
        draw.rect(self.screen, color, rect)