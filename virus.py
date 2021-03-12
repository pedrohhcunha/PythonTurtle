import turtle

t = turtle.Turtle()

t.pencolor('green')
t.speed(50)
for i in range(1000):
    for j in range(i%6):
        t.forward(50)
        t.left((i%6)*10)


input()