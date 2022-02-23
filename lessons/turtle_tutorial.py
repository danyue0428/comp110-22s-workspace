from turtle import Turtle, colormode, done  # from turtle import [function_name]
leo: Turtle = Turtle()  # <_turtlevariable_> : Turtle = Turtle()

# leo.forward(50)  # distance
# leo.left(30)  # angle
# leo.right(40) # angle

leo.speed(3)
leo.hideturtle()

# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)

colormode(255)
# leo.pencolor("blue")  # line
leo.pencolor(32, 67, 93)  #arrow

leo.penup()
leo.goto(45, 60)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()


# bob: Turtle = Turtle()
# bob.speed(5)

# colormode(255)
# bob.pencolor(0, 0, 0)
# # bob.fillcolor(0, 0, 0)

# bob.penup()
# bob.goto(45, 60)
# bob.pendown()

# side_length: int = 300

# bob.begin_fill()
# i: int = 0
# while (i < 200):
#     bob.forward(side_length)
#     bob.left(121)
#     i = i + 1
#     side_length = side_length * 0.97
# bob.end_fill()

# # leo.speed(50)
# # leo.hideturtle()

# # bob: Turtle = Turtle()

# # side_length: int = 300

# # i: int = 0
# # while (i < 3):
# #     bob.forward(side_length)
# #     bob.left(120)
# #     i = i + 1


# # while (i < 3):
# #     side_length = side_length * 0.97
# #     bob.forward(side_length)
# #     bob.left(121.5)
# #     i = i + 1


# quit()