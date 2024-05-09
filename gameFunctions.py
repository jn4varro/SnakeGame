
#Verificar la colisión con los bordes de la ventana.
def colisiones(head, body, max_x, max_y):
    if head.xcor() > max_x or head.xcor() < -max_x or head.ycor() > max_y or head.ycor() < -max_y:
        return True
    
#Verificar la colisión con el propio cuerpo.
    for x in body:
        if head.distance(body) < 20:
            return True
        
    return False    