import pygame

from arkanoid import ALTO, ANCHO
class Arkanoid:
    def __init__(self) -> None:
        print("Arranaca el juego!!")
        pygame.init()
        pygame.display.set_mode((ANCHO, ALTO))

if __name__ == "__main__":
    Arkanoid()