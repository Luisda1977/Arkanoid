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
    limite_iteracion = FPS / fps_animacion
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
