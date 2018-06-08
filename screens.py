import pygame

def update_screen(screen, sqs, st):
    """draw one screen"""
    screen.fill(st.bg_color)
    sqs.draw_squares()
    pygame.display.flip()
