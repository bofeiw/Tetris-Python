import pygame
from sys import exit

def check_events(curr_sq, st):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            key_down(event.key, st)
        elif event.type == pygame.KEYUP:
            key_up(event.key, st)

def key_down(key, st):
    if key == pygame.K_q:
        exit()
    if key == pygame.K_DOWN:
        st.down = True
    elif key == pygame.K_LEFT:
        st.left = True
    elif key == pygame.K_RIGHT:
        st.right = True
    elif key == pygame.K_UP or key == pygame.K_SPACE:
        st.rotate = True

def key_up(key, st):
    if key == pygame.K_q:
        exit()
    if key == pygame.K_DOWN:
        st.down = False
    elif key == pygame.K_LEFT:
        st.left = False
    elif key == pygame.K_RIGHT:
        st.right = False
    elif key == pygame.K_UP or key == pygame.K_SPACE:
        st.rotate = False
