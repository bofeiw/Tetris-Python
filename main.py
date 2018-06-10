requirements = ['pygame']

import sys

def game_start():
    # initialisations
    pygame.init()
    status = functions.Status()
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

# find and install any missing external packages
def check_requirements(requirements):
    # find missing packages
    from importlib.util import find_spec
    missing = [requirement for requirement in requirements if not(find_spec(requirement))]
    if not missing:
        return
    # install missing packages
    sys.stdout.write("Installing" + ','.join(missing) + ".\n")
    # redirect out to nothing so no installing messages will be seen.
    sys_stdout = sys.stdout
    sys_stderr = sys.stderr
    sys.stdout = None
    sys.stderr = None
    from pip.commands.install import InstallCommand
    from pip.status_codes import SUCCESS
    cmd = InstallCommand()
    for requirement in requirements:
        try:
            if cmd.main([requirement]) is not SUCCESS:
                sys_stderr.write("Can not install " + requirement + ", program aborts.\n")
                sys.exit()
        # this might occur because of redirection of stdout and stderr
        except AttributeError:
            pass
    # direct out back to normal
    sys.stdout = sys_stdout
    sys.stderr = sys_stderr
    sys.stdout.write("All packages are installed, starting game...")
    sys.stdout.flush()

if __name__ == "__main__":
    check_requirements(requirements)
    import pygame
    import screens, events, functions, interface
    from settings import Settings
    from squares import Squares
    game_start()
