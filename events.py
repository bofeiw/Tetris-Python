import pygame
from sys import exit

# listen to every event and respond
def check_events(sqs, status):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            key_down(sqs, event.key, status)
        elif event.type == pygame.KEYUP:
            key_up(event.key, status)

# deal with keys that are pressed down
def key_down(sqs, key, status):
    if status.is_game_new():
        status.game_status = status.ACTIVE
    elif status.is_game_over():
        status.game_status = status.RENEW
    if key == pygame.K_q:   # q stands for quit
        exit()
    if key == pygame.K_DOWN:
        status.down = True
    elif key == pygame.K_LEFT:
        status.left = True
        sqs.clock.update_left_down()
    elif key == pygame.K_RIGHT:
        status.right = True
        sqs.clock.update_right_down()
    # both keys could be used for rotate
    elif key == pygame.K_UP or key == pygame.K_SPACE:
        status.rotate = True

# deal with keys that are released
def key_up(key, status):
    if key == pygame.K_q:
        exit()
    if key == pygame.K_DOWN:
        status.down = False
    elif key == pygame.K_LEFT:
        status.left = False
    elif key == pygame.K_RIGHT:
        status.right = False
    # both keys could be used for rotate
    elif key == pygame.K_UP or key == pygame.K_SPACE:
        status.rotate = False