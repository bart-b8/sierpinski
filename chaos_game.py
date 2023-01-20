import numpy as np
from math import sqrt
from random import choice, random

from numpy.random import default_rng

base_points = np.array([[0,0], [1,0], [0.5, sqrt(3)/2]])

def create_new_point(old_point, base_points):
    ref = base_points[choice(range(np.shape(base_points)[0])),:]
    new_point = np.sum([old_point, ref], axis = 0)
    new_point = np.dot(0.5, new_point)
    return new_point

def create_start():
    start = default_rng().random((1,2))
    return start


def create_points(start=create_start()):
    points = start
    return points
    
def add_points(total_number_of_points, points=create_points()):
    while len(points) < total_number_of_points:
        old_point = points[-1,:]
        new_point = create_new_point(old_point, base_points)
        points = np.vstack((points, new_point))
    return points

if __name__ == "__main__":
    points = add_points(10)
    print(points)
