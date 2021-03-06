import turtle #Importando a biblioteca Turtle.

colors = ['red', 'purple', 'cyan', 'green', 'magenta', 'orange', 'blue', 'pink', 'white'] #Criando uma lista de cores

t = turtle.Turtle() #Criando uma Turtle com o nome "t".
t.speed(100) #Definido a velocidade de "t" como 30.

s = turtle.Screen() #Nomeando a tela como "s".
s.bgcolor("black") #Definindo a cor de fundo da tela como preta.

for i in range(1000): #Criando um laço de repetição que se repetirá 360x. 
    t.pencolor(colors[i % 9]) #Define a cor do traço como sendo uma das colors em ordem.
    t.width(i / 100 * 1.2) #definindo a lagura da turtle.
    t.forward(i) #andando a quantidade de laços já feitos.
    t.left(90) #virando a 60 graus.
