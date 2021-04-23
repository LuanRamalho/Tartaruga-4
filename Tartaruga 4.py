# -*- coding: utf-8 -*-

import turtle            # cria alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0,1,2,3]:      # repita 4 vezes
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
