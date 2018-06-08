class Settings:
    def __init__(self):
        # positions
        self.square_length = 30
        self.square_num_x = 13
        self.square_num_y = 20
        self.square_space = 5
        self.new = [0, int(self.square_num_x/2)]

        # colors
        self.bg_color = (0, 0, 0) # black
        self.square_color = (255, 255, 255) # white
        self.space_color = (50, 50, 50) # grey
        self.square_null_color = (20, 20, 20) # dark grey

        # screen
        self.screen_size = self.get_screen_size(self)
        self.screen_name = "Tetris"

        # keys
        self.left = False
        self.right = False
        self.down = False
        self.rotate = False

        # shapes
        self.shapes = (
            ((-1, 0), (0, -1), (0, 1)),
            ((-1, 0), (0, -1), (-1, 1)),
            ((-1, 0), (-1, -1), (0, 1)),
            ((-1, 0), (-1, 1), (0, 1)),
            ((-1, 0), (-2, 0), (1, 0)),
            ((-1, -1), (0, -1), (0, 1)),
            ((1, 1), (0, -1), (0, 1)),
        )
        self.shape_num = len(self.shapes)

    @staticmethod
    def get_screen_size(self):
        x = ((self.square_length + self.square_space)\
            * self.square_num_x) - self.square_space
        y = ((self.square_length + self.square_space)\
            * self.square_num_y) - self.square_space
        return (x, y)

