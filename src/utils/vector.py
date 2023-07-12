
import numpy as np

def extend_vectors(vectors, length, fill = 0.0):
    """
    extends a vector to a given length.
    """
    filled_vectors = np.full((vectors.shape[0], length), fill)
    filled_vectors[:, :vectors.shape[1]] = vectors
    vectors = filled_vectors
    return vectors

def shorten_vectors(vectors, length):
    """
    Cuts off a vector to a given length.
    """
    vectors = vectors[:, :length]
    return vectors

def reshape_vectors(vectors, length, fill = 0.0):
    """
    Cuts off or extends a vector to a given length.
    """
    if not isinstance(vectors, np.ndarray):
        vectors = np.array(vectors)
    if vectors.shape[1] < length:
        vectors = extend_vectors(vectors, length, fill)
    elif vectors.shape[1] > length:
        vectors = shorten_vectors(vectors, length)
    return vectors