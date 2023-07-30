
import numpy as np
import math as mth

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

def get_length(vector):
    if not isinstance(vector, np.ndarray):
        vector = np.array(vector)
    return np.linalg.norm(vector)

def get_distance(vec_1, vec_2):
    if not isinstance(vec_1, np.ndarray):
        vector = np.array(vector)
    if not isinstance(vec_2, np.ndarray):
        vector = np.array(vector)
    
    return get_length((vec_2 - vec_1))

def normalize(vec):
    return vec / np.linalg.norm(vec)

def projection(vector, onto_vector):
    onto_vector_norm = normalize(onto_vector)
    return np.dot(vector, onto_vector_norm ) * onto_vector_norm


def get_2d_line_normal(line_point_1, line_point_2):
    p_1 = np.array(line_point_1)
    p_2 = np.array(line_point_2)
    segment_vec = p_2 - p_1
    segment_normal_vec = normalize(np.array([-segment_vec[1],segment_vec[0], 0]))
    return segment_normal_vec

def get_reflected_vec(incident, normal):
    length = get_length(incident)
    incident = normalize(incident)
    normal = normalize(normal)
    projected_vec = projection(incident,normal)
    return (incident - 2 * projected_vec) * length


def get_distance_to_line(point, line_point_1, line_point_2):
    if not isinstance(point, np.ndarray):
        point = np.array(point)
    if not isinstance(line_point_1, np.ndarray):
        line_point_1 = np.array(line_point_1)
    if not isinstance(line_point_2, np.ndarray):
        line_point_2 = np.array(line_point_2)

    a = point - line_point_1
    b = line_point_2 - line_point_1

    a_proj_b = projection(a,b) + line_point_1

    distance_to_line = point - a_proj_b
    return get_length(distance_to_line)

def threshold_vector(vec, threshold):
    # if the vectors length is smaller than the threshold, return a zero vector
    if get_length(vec) < threshold:
        return np.zeros(vec.shape)
    return vec