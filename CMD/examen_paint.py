# Librerias
import pygame
import math

# Inicializar Pygame
pygame.init()

# Crear una superficie de 800x600 píxeles
width = 800
height = 600
surface = pygame.display.set_mode((width, height))
background_color = (0,0,0)
surface.fill(background_color)
pygame.display.flip()

# Color predeteminado de la pantalla
color = (255, 120, 10)

# Colores intercambiables para el fondo
colors = {
    'rojo': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
    'amarillo': (255, 255, 0),
    'blanco': (255, 255, 255),
    'negro': (0, 0, 0)}
tamano_pixel = 1
trazos = []

# Objeto y sus metodos
class Triangulos:

    def dibujar_triangulo_equilatero(x, y, lado):
        h = int(lado * math.sqrt(3) / 2)
        p1 = (x, y)
        p2 = (x + lado, y)
        p3 = (x + lado // 2, y - h)
        pygame.draw.polygon(surface, color, [p1, p2, p3], tamano_pixel)
        pygame.display.flip()

    def dibujar_triangulo_isoceles(x, y, base, altura):
        p1 = (x, y)
        p2 = (x + base, y)
        p3 = (x + base // 2, y - altura)
        pygame.draw.polygon(surface, color, [p1, p2, p3], tamano_pixel)
        pygame.display.flip()

    def dibujar_triangulo_escaleno(x1, y1, x2, y2, x3, y3):
        p1 = (x1, y1)
        p2 = (x2, y2)
        p3 = (x3, y3)
        pygame.draw.polygon(surface, color, [p1, p2, p3], tamano_pixel)

# Funciones
def help():
    print ("--Bienvenidos a Paint--\n"
           "Los Comandos que se pueden utilizar son los siguientes:\n\n"
           "exit; con este cierras el programa\n"
           "linea -h; puedes dibujar una linea horizontal, te pedira ingresar los valores\n"
           "linea -v; puedes dibujar una linea vertical, te pedira ingresar los valores\n"
           "cambiar color; puedes cambiar el color de los dibujos, Puedes elejir entre: rojo,verde,azul,amarillo y cian\n"
           "linea; podras hacer una linea de un punto A a un punto B, te pedira ingresar los valores\n"
           "configurar_tamano_pixel; puedes cambiar el grosor de las lineas, te pedira ingresar el tamano\n"
           "cuadrado; podras hacer un cuadrado, te pedira ingresar los valores\n"
           "triangulo; puedes hacer un triangulo, te pedira ingresar seis valores\n"
           "circulo; puedes hacer un circulo, te pedira ingresar los valores\n"
           "rectangulo; dibujara un rectangulo, le tendras que ingresar los valores\n"
           "color_fondo; puedes cambiar el fondo de la ventana, Puedes elejir entre: rojo,verde,azul,amarillo,blanco y negro\n"
           "equilatero; dibujara un triangulo equilatero, te pedira ingresar los valores\n"
           "isoceles; dibujara un triangulo isoceles, te pedira ingresar los valores\n"
           "escaleno; dibujara un triangulo escaleno, te pedira ingresar los valores\n")

def color_fondo():
    color_name = input("Ingrese el nombre del color de fondo: ")
    color = colors.get(color_name.lower())
    if color is None:
        print("Color no válido")
        return
    surface.fill(color)
    pygame.display.flip()

def cambiar_color(nombre_color):
    global color
    if nombre_color == "rojo":
        color = (255, 0, 0)
    elif nombre_color == "verde":
        color = (0, 255, 0)
    elif nombre_color == "azul":
        color = (0, 0, 255)
    elif nombre_color == "amarillo":
        color = (255, 255, 0)
    elif nombre_color == "cian":
        color = (0, 255, 255)
    else:
        print("Color no válido")

def linea_h(i, desplazamiento):
    for j in range(0, 100):
        for k in range(tamano_pixel):
            surface.set_at((100 + desplazamiento + j, 200 + i + k), color)
    pygame.display.flip()

def linea_v(i, desplazamiento):
    for j in range(0, 100):
        for k in range(tamano_pixel):
            surface.set_at((100 + i + k, 200 + desplazamiento + j), color)
    pygame.display.flip()

def dibujar_linea(A, B):
    pygame.draw.line(surface, color, A, B, tamano_pixel)
    pygame.display.flip()
    trazos.append((A, B))

def dibujar_cuadrado(x, y, lado):
    for i in range(x, x + lado):
        for j in range(y, y + lado):
            surface.set_at((i, j), color)
    pygame.display.flip()
    configurar_tamano_pixel(tamano_pixel)

def dibujar_rectangulo(x, y, width, height):
    pygame.draw.rect(surface, color, pygame.Rect(x, y, width * tamano_pixel, height * tamano_pixel))
    pygame.display.flip()

def dibujar_triangulo(x1, y1, x2, y2, x3, y3):
    pygame.draw.polygon(surface, color, [(x1, y1), (x2, y2), (x3, y3)])
    pygame.display.flip()
    configurar_tamano_pixel(tamano_pixel)

def circulo(x_centro, y_centro, radio):
    for i in range(360):
        angulo_rad = math.radians(i)
        x = int(x_centro + radio * math.cos(angulo_rad))
        y = int(y_centro + radio * math.sin(angulo_rad))
        surface.set_at((x, y), color)
    pygame.display.flip()
    configurar_tamano_pixel(tamano_pixel)

def configurar_tamano_pixel(nuevo_tamano):
    global tamano_pixel
    tamano_pixel = max(1, nuevo_tamano)

# Loop principal
while True:
    cmd = input("cmd> ")
    if cmd == "exit":
        pygame.quit()

    elif cmd == "help":
        help()
    
    elif cmd.startswith("linea -h"):
        params = cmd.split(" ")
        if len(params) >= 4:
            try:
                i = int(params[2])
                desplazamiento = int(params[3])
                linea_h(i, desplazamiento)
            except ValueError:
                print("Comando incorrecto. Uso: linea -h <valor_i> <desplazamiento>")
        else:
            print("Comando incorrecto. Uso: linea -h <valor_i> <desplazamiento>")
    elif cmd.startswith("linea -v"):
        params = cmd.split(" ")
        if len(params) >= 4:
            try:
                i = int(params[2])
                desplazamiento = int(params[3])
                linea_v(i, desplazamiento)
            except ValueError:
                print("Comando incorrecto. Uso: linea -v <valor_i> <desplazamiento>")
        else:
            print("Comando incorrecto. Uso: linea -v <valor_i> <desplazamiento>")
    
    elif cmd.startswith("cambiar color"):
        params = cmd.split(" ")
        if len(params) >= 2:
            nombre_color = params[2]
            cambiar_color(nombre_color)
        else:
            print("Comando incorrecto. Uso: cambiar color <nombre_color>")

    elif cmd.startswith("linea"):
        params = cmd.split(" ")
        if len(params) >= 5:
            try:
                x1 = int(params[1])
                y1 = int(params[2])
                x2 = int(params[3])
                y2 = int(params[4])
                A = (x1, y1)
                B = (x2, y2)
                dibujar_linea(A, B)
            except ValueError:
                print("Comando incorrecto. Uso: linea <x1> <y1> <x2> <y2>")
        else:
            print("Comando incorrecto. Uso: linea <x1> <y1> <x2> <y2>")

    elif cmd.startswith("configurar_tamano_pixel"):
        params = cmd.split(" ")
        if len(params) == 2:
            try:
                nuevo_tamano = int(params[1])
                configurar_tamano_pixel(nuevo_tamano)
                print("Tamaño de píxel configurado:", tamano_pixel)
            except ValueError:
                print("Comando incorrecto. Uso: configurar_tamano_pixel <tamano>")
        else:
            print("Comando incorrecto. Uso: configurar_tamano_pixel <tamano>")

    elif cmd.startswith("cuadrado"):
        params = cmd.split(" ")
        if len(params) == 4:
            try:
                x = int(params[1])
                y = int(params[2])
                lado = int(params[3])
                dibujar_cuadrado(x, y, lado)
            except ValueError:
                print("Comando incorrecto. Uso: cuadrado <x> <y> <lado>")
        else:
            print("Comando incorrecto. Uso: cuadrado <x> <y> <lado>")

    elif cmd.startswith("triangulo"):
        params = cmd.split(" ")
        if len(params) == 7:
            try:
                x1 = int(params[1])
                y1 = int(params[2])
                x2 = int(params[3])
                y2 = int(params[4])
                x3 = int(params[5])
                y3 = int(params[6])
                dibujar_triangulo(x1, y1, x2, y2, x3, y3)
            except ValueError:
                print("Comando incorrecto. Uso: triangulo <x1> <y1> <x2> <y2> <x3> <y3>")
        else:
            print("Comando incorrecto. Uso: triangulo <x1> <y1> <x2> <y2> <x3> <y3>")

    elif cmd.startswith("circulo"):
        params = cmd.split(" ")
        if len(params) == 4:
            try:
                x_centro = int(params[1])
                y_centro = int(params[2])
                radio = int(params[3])
                circulo(x_centro, y_centro, radio)
            except ValueError:
                print("Comando incorrecto. Uso: circulo <x_centro> <y_centro> <radio>")
        else:
            print("Comando incorrecto. Uso: circulo <x_centro> <y_centro> <radio>")
    
    elif cmd.startswith("rectangulo"):
        params = cmd.split(" ")
        if len(params) >= 5:
            try:
                x = int(params[1])
                y = int(params[2])
                width = int(params[3])
                height = int(params[4])
                dibujar_rectangulo(x, y, width, height)
            except ValueError:
                print("Comando incorrecto. Uso: rectangulo <x> <y> <width> <height>")
        else:
            print("Comando incorrecto. Uso: rectangulo <x> <y> <width> <height>")

    elif cmd == "color_fondo":
        color_fondo()

    # Comandos de los objetos
    elif cmd == "equilatero":
        x = int(input("Ingrese la coordenada x: "))
        y = int(input("Ingrese la coordenada y: "))
        lado = int(input("Ingrese el tamaño del lado: "))
        Triangulos.dibujar_triangulo_equilatero(x, y, lado)

    elif cmd == "isoceles":
        x = int(input("Ingrese la coordenada x: "))
        y = int(input("Ingrese la coordenada y: "))
        base = int(input("Ingrese el tamaño de la base: "))
        altura = int(input("Ingrese la altura: "))
        Triangulos.dibujar_triangulo_isoceles(x, y, base, altura)

    elif cmd == "escaleno":
        x1 = int(input("Ingrese la coordenada x1: "))
        y1 = int(input("Ingrese la coordenada y1: "))
        x2 = int(input("Ingrese la coordenada x2: "))
        y2 = int(input("Ingrese la coordenada y2: "))
        x3 = int(input("Ingrese la coordenada x3: "))
        y3 = int(input("Ingrese la coordenada y3: "))
        Triangulos.dibujar_triangulo_escaleno(x1, y1, x2, y2, x3, y3)


    



    
