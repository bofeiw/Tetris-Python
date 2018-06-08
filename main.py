import pygame, time
import screens, events, functions
from settings import Settings
from squares import Squares

def game_start():
    st = Settings()
    pygame.init()
    screen = pygame.display.set_mode(st.screen_size)
    pygame.display.set_caption(st.screen_name)

    sqs = Squares(st, screen)
    curr_sq = [10,5]#sqs.get_square()
    shape = functions.get_shape(st)

    while True:
        events.check_events(curr_sq, st)
        screens.update_screen(screen, sqs, curr_sq, shape, st)




if __name__ == "__main__":
    game_start()