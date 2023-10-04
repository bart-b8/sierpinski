# Sierpiński Triangle

Lets use python/streamlit to visualise the creation of a Sierpiński triangle using the chaos game.

## The chaos game.

1. Take three points in a plane to form a triangle
2. Randomly select any point inside the triangle.
3. Randomly select any of the three vertex points.
4. Move half of the distance from your current position to the selected vertex.
5. Plot the current position.
6. Repeat from step 3.

Source : [Wiki:Sierpinski](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#Chaos_game)  

## Start locations and possible results

[todo]: this section will go report on experimenting with different start points and there influence on the game. 

## How this program selects a random point in the triangle.

[todo]
Points are represented by Cartesian coordinates. Points inside the triangle comply to following constraints:
```math
$$
\begin{case}
x>=0\\
y <= sqrt(3)x\\
y <= -sqrt(3)(x-1)
\end{cases}
$$
```

## Waking up the app

When the web app hasn't been visited in a week, you'll have to press this button "Yes, get this app back up!"

![](./images/Zzzz-Streamlit.PNG) 
