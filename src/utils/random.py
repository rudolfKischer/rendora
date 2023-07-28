import numpy as np

def rand(include_negative=False):
    rand = np.random.uniform(0.0, 1.0)
    if include_negative:
        rand = rand * 2 - 1
    return rand

def rand_vec(vec_len=3, include_negative=False):
    rand_vec = np.zeros(vec_len)
    for i in range(vec_len):
        rand_vec[i] = rand(include_negative)
    return rand_vec

    
