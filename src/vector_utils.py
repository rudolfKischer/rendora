
import numpy as np

def extend_vectors(vectors, length):
    """
    extends a vector to a given length.
    """
    zero_filled_vectors = np.zeros((vectors.shape[0], length))
    zero_filled_vectors[:, :vectors.shape[1]] = vectors
    vectors = zero_filled_vectors
    return vectors

def shorten_vectors(vectors, length):
    """
    Cuts off a vector to a given length.
    """
    vectors = vectors[:, :length]
    return vectors

def reshape_vectors(vectors, length):
    """
    Cuts off or extends a vector to a given length.
    """
    if not isinstance(vectors, np.ndarray):
        vectors = np.array(vectors)
    if vectors.shape[1] < length:
        vectors = extend_vectors(vectors, length)
    elif vectors.shape[1] > length:
        vectors = shorten_vectors(vectors, length)
    return vectors