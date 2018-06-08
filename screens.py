import pygame

def update_screen(screen, sqs, curr_sq, shape, st):
    update_curr_sq(sqs, curr_sq, shape, st)

    screen.fill(st.bg_color)
    sqs.draw_squares(curr_sq, shape, st)
    pygame.display.flip()

def update_curr_sq(sqs, curr_sq, shape, st):
    if st.down:
        put_curr_down(sqs, curr_sq, st)
    elif st.rotate:
        rotate(sqs, curr_sq, shape, st)
    elif st.right and can_right(curr_sq, shape, st):
        curr_sq[1] += 1
    elif st.left and can_left(curr_sq, shape, st):
        curr_sq[1] -= 1


def put_curr_down(sqs, curr_sq, st):
    if curr_sq[0] < st.square_num_y - 1 and\
        not(sqs.squares[curr_sq[0] + 1][curr_sq[1]]):
            curr_sq[0] += 1

def rotate(sqs, curr_sq, shape, st):
    new_shape = get_rotated_shape(shape)
    if can_rotate(curr_sq, new_shape, st):
        for i in range(len(shape)):
            shape[i] = new_shape[i]

def get_rotated_shape(shape):
    new_shape = []
    for sq in shape:
       new_shape.append([-sq[1], sq[0]])
    return new_shape

def can_rotate(new_sq, shape, st):
    for sq in shape:
        if sq[1]+new_sq[1] > st.square_num_x-1 or \
            sq[1]+new_sq[1] < 0 or \
            sq[0]+new_sq[0] > st.square_num_y-1:
            return False
    return True

def can_right(curr_sq, shape, st):
    for sq in shape:
        if sq[1]+curr_sq[1] >= st.square_num_x-1:
            return False
    return True

def can_left(curr_sq, shape, st):
    for sq in shape:
        if sq[1]+curr_sq[1] <= 0:
            return False
    return True