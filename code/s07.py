import turtle

def main():
    t = turtle.Turtle()
    t.speed(0)
    draw_square(t)
    turtle.mainloop()
    
def draw_square(turtle_obj, size = 100):
    """Draw a sqare with given size."""
    for i in range(4):
        turtle_obj.forward(size)
        turtle_obj.left(90)

