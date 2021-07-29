from turtle import Turtle, Screen
import turtle as t

import colorgram

tim = t.Turtle()
t.colormode(255)

rgb_colors = []
colors = colorgram.extract('images.jpg', 40)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
colors = rgb_colors[3:]
print(len(colors))

def color(object):
    number = object % len(colors)
    get_color = colors[number]
    r = get_color[0]
    g = get_color[1]
    b = get_color[2]

    return (r, g, b)


tim = t.Turtle()
t.colormode(255)
tim. speed(0)
tim.shape("turtle")
# tim.width(width = 100)
# tim.pensize(width = 20)
tim.penup()
tim.setpos(-250, -200 )
tim.pendown()
for x in range(0,100):
    if x % 10 == 0:
        print(x)
        tim.penup()
        tim.setpos(-250, x / 10 * 50 -200)
        tim.pendown()
    choice = color(x)
    tim.dot(20, choice)
    tim.penup()
    tim.fd(50)
    tim.pendown()


screen = Screen()
print(screen.screensize())
screen.exitonclick()