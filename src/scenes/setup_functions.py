from src.collider import LineSegmentCollider
import numpy as np
from src.element import Element

def create_borders():
    top_right = np.array([1.0,1.0,0.0])
    top_left = np.array([-1.0,1.0,0.0])
    bottom_right = np.array([1.0,-1.0,0.0])
    bottom_left = np.array([-1.0,-1.0,0.0])

    borders = [
        LineSegmentCollider(top_left, top_right),
        LineSegmentCollider(top_left, bottom_left),
        LineSegmentCollider(top_right, bottom_right),
        LineSegmentCollider(bottom_left, bottom_right)
    ]

    complete_border = Element()

    for border in borders:
        complete_border.add_child_element(border)
    
    return complete_border
    
