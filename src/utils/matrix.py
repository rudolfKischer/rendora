import numpy as np

"""
This file contains functions for working with transformation matrices.
"""

def get_translation_matrix(position):
    """
    Returns a translation matrix for a given position (nparray).
    """
    translation_matrix = np.identity(4)
    translation_matrix[0, 3] = position[0]
    translation_matrix[1, 3] = position[1]
    translation_matrix[2, 3] = position[2]
    return translation_matrix

def get_scale_matrix(scale):
    """
    Returns a scale matrix for a given scale (nparray).
    """
    scale_matrix = np.identity(4)
    scale_matrix[0, 0] = scale[0]
    scale_matrix[1, 1] = scale[1]
    scale_matrix[2, 2] = scale[2]
    return scale_matrix

def get_rotation_matrix(orientation):
    """
    Returns a rotation matrix for a given orientation (nparray).
    """
    rotation_matrix = np.identity(4)
    cos_theta = np.cos(orientation[0])
    sin_theta = np.sin(orientation[0])
    cos_phi = np.cos(orientation[1])
    sin_phi = np.sin(orientation[1])
    cos_psi = np.cos(orientation[2])
    sin_psi = np.sin(orientation[2])
    rotation_matrix[0, 0] = cos_phi * cos_psi
    rotation_matrix[0, 1] = cos_phi * sin_psi
    rotation_matrix[0, 2] = -sin_phi
    rotation_matrix[1, 0] = sin_theta * sin_phi * cos_psi - cos_theta * sin_psi
    rotation_matrix[1, 1] = sin_theta * sin_phi * sin_psi + cos_theta * cos_psi
    rotation_matrix[1, 2] = sin_theta * cos_phi
    rotation_matrix[2, 0] = cos_theta * sin_phi * cos_psi + sin_theta * sin_psi
    rotation_matrix[2, 1] = cos_theta * sin_phi * sin_psi - sin_theta * cos_psi
    rotation_matrix[2, 2] = cos_theta * cos_phi
    return rotation_matrix

def get_model_matrix(position, orientation, scale):
    """
    Returns a model matrix for a given position, orientation, and scale (nparrays).
    """
    model_matrix = np.identity(4)
    model_matrix = np.matmul(model_matrix, get_translation_matrix(position))
    model_matrix = np.matmul(model_matrix, get_rotation_matrix(orientation))
    model_matrix = np.matmul(model_matrix, get_scale_matrix(scale))
    return model_matrix

