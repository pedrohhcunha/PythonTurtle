import turtle #Importando a biblioteca Turtle.

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange'] #Criando uma lista de cores

t = turtle.Turtle() #Criando uma Turtle com o nome "t".
t.speed(30) #Definido a velocidade de "t" como 30.

s = turtle.Screen() #Nomeando a tela como "s".
s.bgcolor("black") #Definindo a cor de fundo da tela como preta.

for i in range(360): #Criando um laço de repetição que se repetirá 360x. 
    t.pencolor(colors[i % 6]) #Define a cor do traço como sendo uma das colors em ordem.
    t.width(i / 100 + 1) #definindo a lagura da turtle.
    t.forward(i) #andando a quantidade de laços já feitos.
    t.left(59) #virando a 60 graus.
