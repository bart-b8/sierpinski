import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from math import sqrt
from random import choice

def create_new_point(old_point, base_points):
    ref = choice(base_points)
    new_point = np.sum([old_point, ref], axis = 0)
    new_point = np.dot(0.5, new_point)
    return new_point


st.title("Sierpinski Triangle")

base_points = [(0,0), (1,0), (0.5, sqrt(3)/2)]
points = []
start = (0.5,0.5)
points.append(start)
old_point = start
for i in range(10000):
    new_point = tuple(create_new_point(old_point, base_points))
    points.append(new_point)
    old_point = new_point



scale = 1000
scaled_basepoints = [(scale*x, scale*y) for x,y in base_points]

fig = plt.figure()
x, y = zip(*base_points)
plt.scatter(x,y)
x,y = zip(*points)
plt.scatter(x,y, s=1, marker='.')

st.pyplot(fig)

