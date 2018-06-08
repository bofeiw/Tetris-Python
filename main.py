import pygame, time
import screens, events, functions
from settings import Settings
from squares import Squares


def game_start():
    # initialisations
    st = Settings()
    pygame.init()
    screen = pygame.display.set_mode(st.screen_size)
    pygame.display.set_caption(st.screen_name)
    sqs = Squares(st, screen)

    # main loop
    while True:
        events.check_events(sqs, st)
        if st.game_active:
            if sqs.update():
                screens.update_screen(screen, sqs, st)
        else:
            time.sleep(0.1)  # game over


if __name__ == "__main__":
    game_start()
