'''Este codigo es un paint a base de comandos que escribes en terminal
y se ven reflegados en la ventana de pygame'''
import math
import sys
import pygame

# Crear una superficie de 800x600 píxeles
WIDTH = 800
HEIGHT = 600
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_COLOR = (0, 0, 0)
SURFACE.fill(BACKGROUND_COLOR)
pygame.display.flip()

# Colores predeterminados
COLOR = (255, 120, 10)

# Colores intercambiables para el fondo
COLORS = {
    'rojo': (255, 0, 0),
    'verde': (0, 255, 0),
    'azul': (0, 0, 255),
    'amarillo': (255, 255, 0),
    'blanco': (255, 255, 255),
    'negro': (0, 0, 0)
}
class Triangulos:
    '''
    Esta clase contiene los tres tipos de triangulos
    '''
    @staticmethod
    def dibujar_triangulo_equilatero(tex_, tey_, lado_):
        '''
        Aqui estan las formulas del triangulo equilatero
        '''
        rell_ = int(lado_ * math.sqrt(3) / 2)
        parte_1 = (tex_, tey_)
        parte_2 = (tex_ + lado_, tey_)
        parte_3 = (tex_ + lado_ // 2, tey_ - rell_)
        pygame.draw.polygon(SURFACE, COLOR, [parte_1, parte_2, parte_3], TAMANO_PIXEL)
        pygame.display.flip()

    @staticmethod
    def dibujar_triangulo_isoceles(tix_, tiy_, base, altura):
        '''
        Aqui estan las formulas del triangulo isoceles
        '''
        parte_4 = (tix_, tiy_)
        parte_5 = (tix_ + base, tiy_)
        parte_6 = (tix_ + base // 2, tiy_ - altura)
        pygame.draw.polygon(SURFACE, COLOR, [parte_4, parte_5, parte_6], TAMANO_PIXEL)
        pygame.display.flip()

    @staticmethod
    def dibujar_triangulo_escaleno(tesx_, tesy_, tesx_1, tesy_1, tesx_2, tesy_2):
        '''
        Aqui estan las formulas del triangulo escaleno
        '''
        parte_7 = (tesx_, tesy_)
        parte_8 = (tesx_1, tesy_1)
        parte_9 = (tesx_2, tesy_2)
        pygame.draw.polygon(SURFACE, COLOR, [parte_7, parte_8, parte_9], TAMANO_PIXEL)
        pygame.display.flip()

TAMANO_PIXEL = 1
TRAZOS = []

# Funciones

def rectangulo_command():
    '''
    Aqui estan las formulas del rectangulo
    '''
    rectx = int(input("Ingrese la coordenada x del centro del rectangulo: "))
    recty = int(input("Ingrese la coordenada y del centro del rectangulo: "))
    width = int(input("Ingrese el ancho del rectangulo: "))
    height = int(input("Ingrese el largo del rectangulo: "))
    pygame.draw.rect(SURFACE,COLOR,pygame.Rect(rectx,recty,width*TAMANO_PIXEL,height*TAMANO_PIXEL))
    pygame.display.flip()

def linea_h_command():
    '''
    Aqui estan las formulas para dibujar una linea horizontal
    '''
    linea_x = int(input("Ingrese la coordenada x inicial de la línea horizontal: "))
    linea_y = int(input("Ingrese la coordenada x final de la línea horizontal: "))
    coord_y = int(input("Ingrese la coordenada y de la línea horizontal: "))
    pygame.draw.line(SURFACE, COLOR, (linea_x, coord_y), (linea_y, coord_y), TAMANO_PIXEL)
    pygame.display.flip()

def linea_v_command():
    '''
    Aqui estan las formulas para dibujar una linea vertical
    '''
    linea_a = int(input("Ingrese la coordenada x de la línea vertical: "))
    linea_b = int(input("Ingrese la coordenada y inicial de la línea vertical: "))
    linea_c = int(input("Ingrese la coordenada y final de la línea vertical: "))
    pygame.draw.line(SURFACE, COLOR, (linea_a, linea_b), (linea_a, linea_c), TAMANO_PIXEL)
    pygame.display.flip()

def linea_command():
    '''
    Aqui estan las formulas para dibujar una linea de punto A a un punto B
    '''
    linea_d = int(input("Ingrese la coordenada x inicial de la línea: "))
    linea_e = int(input("Ingrese la coordenada y inicial de la línea: "))
    linea_f = int(input("Ingrese la coordenada x final de la línea: "))
    linea_g = int(input("Ingrese la coordenada y final de la línea: "))
    pygame.draw.line(SURFACE, COLOR, (linea_d, linea_e), (linea_f, linea_g), TAMANO_PIXEL)
    pygame.display.flip()

def circulo_command():
    '''
    Aqui estan las formulas del circulo
    '''
    cir_x = int(input("Ingrese la coordenada x del centro del círculo: "))
    cir_y = int(input("Ingrese la coordenada y del centro del círculo: "))
    radio = int(input("Ingrese el radio del círculo: "))
    pygame.draw.circle(SURFACE, COLOR, (cir_x, cir_y), radio, TAMANO_PIXEL)
    pygame.display.flip()

def cambiar_color_command():
    '''
    Esta funcion cambia el color de las lineas dibujadas
    '''
    global COLOR
    color = input("Elige un color (rojo, verde, azul, amarillo, blanco o negro): ")
    if color in COLORS:
        COLOR = COLORS[color]
    else:
        print("Color no válido.")

def color_fondo_command():
    '''
    Esta funcion cambia el color del fondo
    '''
    color = input("Elige un color de fondo (rojo, verde, azul, amarillo, blanco o negro): ")
    if color in COLORS:
        background_color = COLORS[color]
        SURFACE.fill(background_color)
        pygame.display.flip()
    else:
        print("Color no válido.")

def configurar_tamano_pixel_command():
    '''
    Esta funcion cambia el tamano de las lineas dibujadas
    '''
    global TAMANO_PIXEL
    tamano = int(input("Ingrese el grosor de las líneas: "))
    TAMANO_PIXEL = tamano

def cuadrado_command():
    '''
    Aqui estan las formulas del cuadrado
    '''
    cua_x = int(input("Ingrese la coordenada x del vértice superior izquierdo del cuadrado: "))
    cua_y = int(input("Ingrese la coordenada y del vértice superior izquierdo del cuadrado: "))
    lado = int(input("Ingrese la longitud del lado del cuadrado: "))
    pygame.draw.rect(SURFACE, COLOR, (cua_x, cua_y, lado, lado), TAMANO_PIXEL)
    pygame.display.flip()

def exit_command():
    '''
    Esta funcion hace que te salgas del programa
    '''
    pygame.quit()
    sys.exit()

def main():
    '''
    Aqui se encontrara toda la logica del codigo
    '''
    while True:
        command = input("Ingrese un comando (\n circulo\n cambiar_color\n color_fondo\n"
        " configurar_tamano_pixel\n cuadrado\n equilatero\n isoceles\n escaleno\n"
        " rectangulo\n linea -h\n linea -v\n linea\n exit): ")
        if command == "circulo":
            circulo_command()
        elif command == "cambiar_color":
            cambiar_color_command()
        elif command == "configurar_tamano_pixel":
            configurar_tamano_pixel_command()
        elif command == "cuadrado":
            cuadrado_command()
        elif command == "rectangulo":
            rectangulo_command()
        elif command == "linea -h":
            linea_h_command()
        elif command == "linea -v":
            linea_v_command()
        elif command == "linea":
            linea_command()
        elif command == "color_fondo":
            color_fondo_command()
        elif command == "exit":
            exit_command()
        # Comandos de los objetos
        elif command == "equilatero":
            tex_ = int(input("Ingrese la coordenada x: "))
            tey_ = int(input("Ingrese la coordenada y: "))
            lado_ = int(input("Ingrese el tamaño del lado: "))
            Triangulos.dibujar_triangulo_equilatero(tex_, tey_, lado_)

        elif command == "isoceles":
            tix_ = int(input("Ingrese la coordenada x: "))
            tiy_ = int(input("Ingrese la coordenada y: "))
            base = int(input("Ingrese el tamaño de la base: "))
            altura = int(input("Ingrese la altura: "))
            Triangulos.dibujar_triangulo_isoceles(tix_, tiy_, base, altura)

        elif command == "escaleno":
            tesx_ = int(input("Ingrese la coordenada x1: "))
            tesy_ = int(input("Ingrese la coordenada y1: "))
            tesx_1 = int(input("Ingrese la coordenada x2: "))
            tesy_1 = int(input("Ingrese la coordenada y2: "))
            tesx_2 = int(input("Ingrese la coordenada x3: "))
            tesy_2 = int(input("Ingrese la coordenada y3: "))
            Triangulos.dibujar_triangulo_escaleno(tesx_, tesy_, tesx_1, tesy_1, tesx_2, tesy_2)
        else:
            print("Comando no válido.")

if __name__ == "__main__":
    main()
