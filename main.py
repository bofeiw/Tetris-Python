import time, sys
try:
    import pygame   # This must be installed. All functionality relies on it.
except:
    sys.stderr.write("Please install Pygame module and then come back.")
    sys.exit()
import screens, events, functions, interface
from settings import Settings
from squares import Squares


def game_start():
    # initialisations
    status = functions.Status()

    pygame.init()

    st = Settings()
    screen = pygame.display.set_mode(st.screen_size)
    pygame.display.set_caption(st.screen_name)

    sqs = Squares(st, status, screens.get_sqs_surface(screen, st))
    func = functions.Fucntions(st, screens.get_func_surface(screen, st))

    # main loop
    while True:
        pygame.display.flip()
        events.check_events(sqs, status)
        if status.is_game_active():
            if sqs.update():
                screens.update_screen(screen, sqs, func, status, st)
        elif status.is_game_over():
            interface.game_over(screen, st)
        elif status.is_game_new():
            interface.start(screen, st)
        elif status.is_game_renew():
            status.refresh()
            sqs = Squares(st, status, screens.get_sqs_surface(screen, st))
            status.game_status = status.ACTIVE
        else:
            sys.exit(1) # this should never happen


if __name__ == "__main__":
    game_start()
