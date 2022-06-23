import os

import pygame as pg
from pygame.sprite import Sprite

from . import ALTO, ANCHO

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

    def __init__(self):
        super().__init__()

        self.sprites = [
            pg.image.load(os.path.join(
                "resources", "images", "electric00.png")),
            pg.image.load(os.path.join(
                "resources", "images", "electric01.png")),
            pg.image.load(os.path.join(
                "resources", "images", "electric02.png")),
        ]
        self.contador = 0

        image_path = os.path.join("resources", "images", "electric00.png")
        self.image = pg.image.load(image_path)
        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO-self.margen_inferior))

    def update(self):
        # self.rect.x = self.rect.x + 1
        #self.image = self.sprites[self.contador]
        #self.contador += 1
        # if self.contador > 2:
        #self.contador = 0
        tecla = pg.key.get_pressed()
        if tecla[pg.K_x]:
            self.rect.x += self.velocidad
            if self.rect.right > ANCHO:
                self.rect.right = ANCHO
        if tecla[pg.K_z]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0
