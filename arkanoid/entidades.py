import os

import pygame as pg
from pygame.sprite import Sprite

from . import ALTO, ANCHO, FPS

"""
1. Crear una clase Raqueta
   a. Sea un Sprite --- hecho
   b. El método update es el que se encarga de gestionarla --- ya sabemos lo que hace
2. Situarlo con las coordenadas y para eso, obtener el rectángulo ---
3. Método mostrar_paleta ----
4. En el bucle principal llamar a mostrar_paleta
Para animar las imágenes:
1. Función "animar" con una lista de imágenes y las mostramos en bucle
"""


class Raqueta(Sprite):

    margen_inferior = 20
    velocidad = 5
    fps_animacion = 12
    limite_iteracion = FPS // fps_animacion
    iteracion = 0

    def __init__(self):
        super().__init__()

        self.sprites = []
        for i in range(3):
            self.sprites.append(
                pg.image.load(
                    os.path.join("resources", "images", f"electric0{i}.png")
                )
            )
        # self.sprites = [
            #pg.image.load(os.path.join("resources", "images", "electric00.png")),
            #pg.image.load(os.path.join("resources", "images", "electric01.png")),
            #pg.image.load(os.path.join("resources", "images", "electric02.png")),

        self.siguiente_imagen = 0
        self.image = self.sprites[self.siguiente_imagen]
        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO-self.margen_inferior))

    def update(self):
        #
        tecla = pg.key.get_pressed()
        if tecla[pg.K_x]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
        if tecla[pg.K_z]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0

        # animamos el rayo de la raqueta
        #fps_animacion = 12
        #limite_iteracion = FPS / fps_animacion
        #iteracion = 0

        self.iteracion += 1
        if self.iteracion == self.limite_iteracion:
            self.siguiente_imagen += 1
            if self.siguiente_imagen >= len(self.sprites):
                self.siguiente_imagen = 0
            self.image = self.sprites[self.siguiente_imagen]
            self.iteracion = 0


"""
1. Crear un ladrillo que hereda de Sprite
2. Importar las imágenes
    "Darles posición" quiere decir calcular para cada ladrillo
    su posición con respecto al anterior para que no se solapen
    y queden pegados pero no amontonados
    (juntos pero no revueltos)

"""


class Ladrillo(Sprite):
    def __init__(self, fila, columna):
        super().__init__()

        ladrillo_verde = os.path.join("resources", "images", "greenTile.png")
        self.image = pg.image.load(ladrillo_verde)
        ancho_ladrillo = self.image.get_width()
        alto_ladrillo = self.image.get_height()

        self.rect = self.image.get_rect(
            x=columna * ancho_ladrillo, y=fila * alto_ladrillo)


class Pelota(Sprite):

    velocidad_x = -5
    velocidad_y = -5

    def __init__(self, **kwargs):
        super().__init__()
        self.image = pg.image.load(os.path.join(
            "resources", "images", "ball1.png"))
        self.rect = self.image.get_rect(**kwargs)

    def update(self, raqueta, juego_iniciado):
        if not juego_iniciado:
            self.rect = self.image.get_rect(midbottom=raqueta.rect.midtop)
        else:
            self.rect.y += self.velocidad_x
            if self.rect.right > ANCHO or self.rect.left < 0:
                self.velocidad_x = -self.velocidad_x

        self.rect.x += self.velocidad_y
        if self.rect.top <= 0:
            self.velocidad_y = self.velocidad_y

        if self.rect.top > ALTO:
            self.pierdes()
            self.reset()

    def pierdes(self):
        print("Pierdes una vida")

    def reset(self):
        print("Recolocamos la pelota en posición inicial")

    def hay_colision(self, otro):
        if self.rect.colliderect(otro):
            # hay colisión
            self.velocidad_y = self.velocidad_y
