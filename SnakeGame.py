import turtle
import time
import random

#Crear ventana principal
ventana = turtle.Screen()
ventana.title("SnakeGame")
turtle.colormode(255)
ventana.bgcolor(155, 188, 15)
ventana.setup(width=600, height=600)
ventana.tracer(0)

#Crear la cabeza de la serpiente
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(48 ,98, 48)
head.goto(0,0)
head.penup()
head.direction = "stop"

#Crear objetivo de la serpiente
goal = turtle.Turtle()
goal.speed(0)
goal.penup()
goal.shape("circle")
goal.color(48 ,98, 48)
goal.goto(0, 100)

#Asignar teclas a funciones de movimiento
def mover_arriba():
    head.direction = "up"

while True:
    ventana.update()
