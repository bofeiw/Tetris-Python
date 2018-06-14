from time import clock

class Clock:
    """set up a timer to record what is time to do"""

    def __init__(self, st):
        self.st = st
        self.last_drop = clock()
        self.last_move = clock()
        self.last_rotate = clock()
        self.last_left_down = clock()
        self.last_right_down = clock()
        self.last_quick_drop = clock()
        self.last_stop = clock()
        self.last_should_stop = None    # for detection of the stop at the very bottom
        self.stop_detection_started = False
        self.last_straight_drop = clock()

    def update_drop(self):
        self.last_drop = clock()

    def update_move(self):
        self.last_move = clock()

    def update_rotate(self):
        self.last_rotate = clock()

    def update_left_down(self):
        self.last_left_down = clock()

    def update_right_down(self):
        self.last_right_down = clock()

    def update_quick_drop(self):
        self.last_quick_drop = clock()

    def update_stop(self):
        self.last_stop = clock()

    def update_should_stop(self, mode):
        if mode is True and self.stop_detection_started is False:
            self.last_should_stop = clock()
            self.stop_detection_started = True
        elif mode is None:
            self.stop_detection_started = False


    def update_straight_drop(self):
        self.last_straight_drop = clock()

    def is_time_to_drop(self):
        return ((clock() - self.last_drop) > self.st.time_drop)

    def is_time_to_quick_drop(self):
        return ((clock() - self.last_quick_drop) > self.st.time_quick_drop) and\
               ((clock() - self.last_stop) > self.st.time_before_drop)

    def is_time_to_move(self):
        return (clock() - self.last_move) > self.st.time_move

    def is_time_to_rotate(self):
        return (clock() - self.last_rotate) > self.st.time_rotate

    def is_time_to_quick_left(self):
        return (clock() - self.last_left_down) > self.st.time_to_quick

    def is_time_to_quick_right(self):
        return (clock() - self.last_right_down) > self.st.time_to_quick

    def is_time_to_straight_drop(self):
        return (clock() - self.last_straight_drop) > self.st.time_to_straight_drop

    def is_time_to_stop(self):
        return  self.stop_detection_started and\
                ((clock() - self.last_should_stop) > self.st.time_stop)
