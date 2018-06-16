import pygame

def update_screen(screen, sqs, func, status, st):
    """draw one screen"""
    screen.fill(st.bg_color)
    sqs.draw_squares()
    func.show_score(status.score)

def get_sqs_surface(screen, st):
    sqs_rect =  pygame.Rect(0, 0, st.game_size[0], st.game_size[1])
    return screen.subsurface(sqs_rect)

def get_func_surface(screen, st):
    func_surface = pygame.Rect(st.game_size[0], 0, st.func_size[0], st.func_size[1])
    return screen.subsurface(func_surface)
