import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng

from math import sqrt
from random import choice, random

def create_new_point(old_point, base_points):
    ref = base_points[choice(range(np.shape(base_points)[0])),:]
    new_point = np.sum([old_point, ref], axis = 0)
    new_point = np.dot(0.5, new_point)
    return new_point


st.title("Sierpiński Triangle")

with st.sidebar:
    st.header("Info:")
    st.write("Draws a number of points following the chaos game to construct the Sierpiński Triangle.")
    st.markdown("""

## The chaos game.

1. Take three points in a plane to form a triangle
2. Randomly select any point inside the triangle.
3. Randomly select any of the three vertex points.
4. Move half of the distance from your current position to the selecter vertex.
5. Plot the current position.
6. Repeat from step 3.

Source : [Wikipedia: Sierpinski](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#Chaos_game)  

             """)
number_of_points = st.sidebar.slider("Number of points:", min_value=2, max_value=5000)

base_points = np.array([[0,0], [1,0], [0.5, sqrt(3)/2]])
start = default_rng().random((1,2))
points = start
old_point = start
for i in range(number_of_points):
    new_point = create_new_point(old_point, base_points)
    points = np.block([[points], [new_point]])
    old_point = new_point



scale = 1000
scaled_basepoints = [(scale*x, scale*y) for x,y in base_points]

fig = plt.figure()
x, y = zip(*base_points)
plt.scatter(x,y)
plt.scatter(start[0], start[1], s = 50, marker='.')
x,y = zip(*points[1:])
plt.scatter(x,y, s=1, marker='.')

st.pyplot(fig)

