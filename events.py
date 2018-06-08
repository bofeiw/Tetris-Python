import pygame
from sys import exit

# listen to every event and respond
def check_events(sqs, st):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            key_down(sqs, event.key, st)
        elif event.type == pygame.KEYUP:
            key_up(event.key, st)

# deal with keys that are pressed down
def key_down(sqs, key, st):
    if key == pygame.K_q:   # q stands for quit
        exit()
    if key == pygame.K_DOWN:
        st.down = True
    elif key == pygame.K_LEFT:
        st.left = True
        sqs.clock.update_left_down()
    elif key == pygame.K_RIGHT:
        st.right = True
        sqs.clock.update_right_down()
    # both keys could be used for rotate
    elif key == pygame.K_UP or key == pygame.K_SPACE:
        st.rotate = True

# deal with keys that are released
def key_up(key, st):
    if key == pygame.K_q:
        exit()
    if key == pygame.K_DOWN:
        st.down = False
    elif key == pygame.K_LEFT:
        st.left = False
    elif key == pygame.K_RIGHT:
        st.right = False
    # both keys could be used for rotate
    elif key == pygame.K_UP or key == pygame.K_SPACE:
        st.rotate = False
