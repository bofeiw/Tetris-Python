from random import randrange

def get_shape(st):
    shape_index = randrange(0, st.shape_num)
    return list(st.shapes[shape_index])
