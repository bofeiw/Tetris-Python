class Settings:
    def __init__(self):
        # game status
        self.game_active =True

        # positions
        self.square_length = 30
        self.square_num_x = 12
        self.square_num_y = 20
        self.square_space = 5
        self.new = [0, int(self.square_num_x/2)]    # upper center

        # colors
        self.bg_color = (30, 30, 30) # black
        self.square_color = (255, 255, 255) # white
        self.square_active_color = (255, 0, 0) # red
        self.space_color = (50, 50, 50) # grey
        self.square_null_color = (40, 40, 40) # dark grey

        # screen
        self.screen_size = self.get_screen_size(self)
        self.screen_name = "Tetris by Bofei Wang"

        # keys
        self.left = False
        self.right = False
        self.down = False
        self.rotate = False

        # times, in seconds
        self.time_drop = 0.3  # period to force drop
        self.time_move = 0.05 # minimum time interval to move
        self.time_rotate = 0.2 # minimum time interval to rotate
        self.time_to_quick = 0.2 # time interval to activate quick move mode
        self.time_move_quik = 0.02 # minimum time interval to move in quick mode

        # shapes
        self.shapes = (
            ([-1, 0], [0, -1], [0, 1]),
            ([-1, 0], [0, -1], [-1, 1]),
            ([-1, 0], [-1, -1], [0, 1]),
            ([-1, 0], [-1, 1], [0, 1]),
            ([-1, 0], [-2, 0], [1, 0]),
            ([-1, -1], [0, -1], [0, 1]),
            ([1, 1], [0, -1], [0, 1]),
        )
        self.shape_num = len(self.shapes)

    @staticmethod
    def get_screen_size(self):
        x = ((self.square_length + self.square_space)\
            * self.square_num_x) - self.square_space
        y = ((self.square_length + self.square_space)\
            * self.square_num_y) - self.square_space
        return (x, y)

