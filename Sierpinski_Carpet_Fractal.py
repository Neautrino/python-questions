import turtle

# Function to draw a Sierpinski Carpet
def sierpinski_carpet(order, size):
    if order == 0:
        for _ in range(4):
            turtle.forward(size)
            turtle.left(90)
    else:
        size /= 3
        for _ in range(4):
            sierpinski_carpet(order - 1, size)
            turtle.forward(size)
        turtle.backward(size * 4)
        turtle.right(90)

# Initialize the Turtle
turtle.speed(0)  # Fastest drawing speed
turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()

# Set the order and size of the Sierpinski Carpet
order = 3  # You can adjust this to change the level of detail
size = 300

# Draw the Sierpinski Carpet
sierpinski_carpet(order, size)

# Close the Turtle graphics window on click
turtle.exitonclick()
