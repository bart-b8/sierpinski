import numpy as np
from math import sqrt
from random import choice, random

from numpy.random import default_rng

def create_new_point(old_point, base_points):
    ref = base_points[choice(range(np.shape(base_points)[0])),:]
    new_point = np.sum([old_point, ref], axis = 0)
    new_point = np.dot(0.5, new_point)
    return new_point


base_points = np.array([[0,0], [1,0], [0.5, sqrt(3)/2]])
start = default_rng().random((1,2))
points = start
old_point = start
for i in range(number_of_points):
    new_point = create_new_point(old_point, base_points)
    points = np.block([[points], [new_point]])
    old_point = new_point
