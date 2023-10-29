import turtle

# Function to draw a Koch snowflake
def koch_snowflake(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        size /= 3.0
        koch_snowflake(order - 1, size)
        turtle.left(60)
        koch_snowflake(order - 1, size)
        turtle.right(120)
        koch_snowflake(order - 1, size)
        turtle.left(60)
        koch_snowflake(order - 1, size)

# Initialize the Turtle
turtle.speed(0)  # Fastest drawing speed
turtle.penup()
turtle.goto(-150, 90)
turtle.pendown()

# Set the order and size of the Koch snowflake
order = 4  # You can adjust this to change the level of detail
size = 300

# Draw the Koch snowflake
for _ in range(3):
    koch_snowflake(order, size)
    turtle.right(120)

# Close the Turtle graphics window on click
turtle.exitonclick()
