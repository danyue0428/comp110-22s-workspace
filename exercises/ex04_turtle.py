"""The Turtle Scene Program of Chinese Knot."""

__author__ = "730490913"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    vlines: Turtle = Turtle()
    draw_vertical_lines(vlines, 0, 50)
    hlines: Turtle = Turtle()
    draw_horizontal_lines(hlines, 0, 50)
    ring: Turtle = Turtle()
    draw_ring(ring, 0, 50, 13)
    tassel: Turtle = Turtle()
    draw_tassel(tassel, 0, 50)
    tail: Turtle = Turtle()
    draw_tail(tail, 0, 0)
    done()


def draw_vertical_lines(vlines: Turtle, x: float, y: float) -> None:
    """Drawing the vertical lines."""
    vlines.width(2)
    vlines.speed(50)
    vlines.pencolor("Red")
    vlines.hideturtle()

    i: int = 0
    while i < 11:
        vlines.penup()
        vlines.goto(x, y)
        vlines.setheading(315)
        vlines.pendown()
        vlines.forward(100)
        x -= 7.07
        y -= 7.07
        i = i + 1


def draw_horizontal_lines(hlines: Turtle, x: float, y: float) -> None:
    """Drawing the horizontal lines."""
    hlines.width(2)
    hlines.speed(50)
    hlines.pencolor("Red")
    hlines.hideturtle()

    t: int = 0
    while t < 11:
        hlines.penup()
        hlines.goto(x, y)
        hlines.setheading(225)
        hlines.pendown()
        hlines.forward(100)
        x += 7.07
        y -= 7.07
        t += 1


def draw_ring(ring: Turtle, x: float, y: float, r: float) -> None:
    """Drawing the upper handle of the Chinese knot."""
    ring.width(3)
    ring.speed(50)
    ring.pencolor("Red")
    ring.hideturtle()

    ring.penup()
    ring.goto(x, y + 20)
    ring.pendown()
    ring.circle(r)
    ring.setheading(270)
    ring.forward(20)

    ring.width(2)
    ring.penup()
    ring.goto(x + 63, y - 79)
    ring.setheading(335)
    ring.pendown()
    ring.circle(9.1, 230)
   
    ring.width()
    ring.penup()
    ring.goto(x - 65, y - 62)
    ring.setheading(150)
    ring.pendown()
    ring.pencolor("Red")
    ring.circle(9.1, 240)
    ring.penup()
    ring.goto(x - 65, y - 62)
   

def draw_tassel(tassel: Turtle, x: float, y: float) -> None:
    """Drawing the tassels at the bottom."""
    tassel.speed(5)
    tassel.pencolor(230, 0, 0)
    tassel.fillcolor(210, 0, 0)
    tassel.hideturtle()
    tassel.penup()
    tassel.goto(x + 13, y - 127)
    tassel.setheading(135)
    tassel.pendown()
    
    tassel.begin_fill()
    tassel.pendown()
    tassel.forward(20)
    tassel.left(90)
    tassel.forward(20)
    tassel.left(45)
    i: int = 0
    while i < 2:
        tassel.forward(40)
        tassel.left(90)
        tassel.forward(29.5)
        tassel.left(90)
        i += 1
    tassel.end_fill()
    

def draw_tail(tail: Turtle, x: float, y: float) -> None: 
    """Drawing seven tails at the bottom of tassel."""
    tail.speed(5)
    tail.pencolor("Red")
    tail.hideturtle()
    tail.setheading(270)
    i: int = 0
    while i < 7:
        tail.penup()
        tail.goto(x - 15, y - 115)
        tail.pendown()
        tail.forward(70)
        x += 4.8
        i += 1
    

if __name__ == "__main__":
    main()