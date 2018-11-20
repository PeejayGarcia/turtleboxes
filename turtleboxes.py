#turtle boxes

import turtle

def draw_square(t, sz):
    """Get turtle t to draw a square with sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")

    alex = turtle.Turtle()
    alex.color("hotpink")
    
    for i in range(5):
        draw_square(alex,20)
        alex.up()
        alex.forward(40)
        alex.down()    
    
    wn.exitonclick()

if __name__ == "__main__":
    main()
