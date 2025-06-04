# Function to draw filled rectangle
def draw_rectangle(color, width, height):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw filled circle
def draw_circle(color, radius):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw tree
def draw_tree():
    move(-150, -120)
    draw_rectangle("brown", 40, 90) # Recombined color, x and y
    move(-135, -45)
    draw_circle("green", 125) 
