import streamlit as st
import matplotlib.pyplot as plt

from chaos_game import base_points, add_points

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

number_of_points = st.sidebar.slider("Number of points:", min_value=2, max_value=50)

scale = 1000

try:
    points = add_points(number_of_points, points)
except NameError:
    points = add_points(number_of_points)

# scaled_basepoints = [(scale*x, scale*y) for x,y in base_points]

fig = plt.figure()
x, y = zip(*base_points)
plt.scatter(x,y)
x, y = zip(*points)
plt.scatter(x[0],y[0], s = 50, marker=".")
plt.scatter(x[1:],y[1:], s=1, marker=".")
# plt.scatter(start[0], start[1], s = 50, marker='.')
# x,y = zip(*points[1:])
# plt.scatter(x,y, s=1, marker='.')

st.pyplot(fig)

