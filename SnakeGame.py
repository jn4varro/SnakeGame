import turtle
import time
import random

#Variables globales
velocidad = 0.1
body = []
score = 0
high_score = 0

#Crear ventana principal
ventana = turtle.Screen()
ventana.title("SnakeGame")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)
max_x = ventana.window_width()/2 - 20
max_y = ventana.window_height()/2 - 20

#Crear la cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.goto(0,0)
head.penup()
head.direction = "stop"

#Crear objetivo de la serpiente
goal = turtle.Turtle()
goal.speed(0)
goal.penup()
goal.shape("circle")
goal.color("red")
goal.goto(0, 100)

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.color("white")
texto.write(f"  Score: {score}    High Score: {high_score}", align ="center", font=("Courier",20,"normal"))

#Funciones de movimiento
def mover_arriba():
    head.direction = "up"
def mover_abajo():
    head.direction = "down"    
def mover_izquierda():
    head.direction = "left"
def mover_derecha():
    head.direction = "right"

def mov():
    if head.direction == "up":
        y = head.ycor()    
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)            

#Asignar teclas de movimiento
ventana.listen()
ventana.onkeypress(mover_arriba, "Up")
ventana.onkeypress(mover_abajo, "Down")
ventana.onkeypress(mover_izquierda, "Left")
ventana.onkeypress(mover_derecha, "Right")

        


while True:
    ventana.update()

    #Colisión con los bordes
    if head.xcor() > max_x or head.xcor() < -max_x or head.ycor() > max_y or head.ycor() < -max_y:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segmento in body:
            segmento.clear()
            segmento.hideturtle() 
        body.clear()
        score = 0
        texto.clear()      
        texto.write(f"  Score: {score}    High Score: {high_score}", align ="center", font=("Courier",20,"normal"))
    
    #Colisión con el propio cuerpo
    for x in body:
        if head.distance(x) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segmento in body:
                segmento.clear()
                segmento.hideturtle() 
            body.clear()
            score = 0
            texto.clear()      
            texto.write(f"  Score: {score}    High Score: {high_score}", align ="center", font=("Courier",20,"normal"))

    #Colisión con el objetivo
    if head.distance(goal) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        goal.goto(x,y)
        #Añadir nuevo segmento al cuerpo cada vez que se alcanza el objetivo
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.penup()
        new_body.color("grey")
        body.append(new_body)
        #aumentar marcador
        score += 10
        if score > high_score:
            high_score = score  
        texto.clear()      
        texto.write(f"  Score: {score}    High Score: {high_score}", align ="center", font=("Courier",20,"normal"))

    #Movimiento del cuerpo
    totalBody = len(body)
    for index in range(totalBody -1, 0, -1):
        x = body[index - 1].xcor()
        y = body[index - 1].ycor()
        body[index].goto(x,y)

    if totalBody > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)   

    mov()
    time.sleep(velocidad)    