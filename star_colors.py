import turtle #Importando a biblioteca Turtle.
import random

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange'] #Criando uma lista de cores

t = turtle.Turtle()
t.speed(8)
s = turtle.Screen()
s.bgcolor("black")
t.pensize(3)


for i in range(1000):
    t.pencolor(colors[random.randint(0, 5)])
    t.forward(i * 8)
    t.right(144)
    
turtle.done()
