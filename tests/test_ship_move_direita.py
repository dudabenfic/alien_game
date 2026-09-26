import pygame
from src.ship import Ship
from src.settings import Settings

def tests_ship_move_direita():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    settings = Settings()

    ship = Ship(screen, settings)

    x_inicial = ship.x

    # ação
    ship.moving_rigjt = True
    ship.update()

    # verificação
    assert ship.x > x_inicial