import pygame
from bullet import Bullet

class GameRenderer:
    #Responsável por renderizar os elementos do jogo na tela    
    def __init__(self, screen, bg_color, ship, bullets, aliens) -> None:
        self.screen = screen
        self.bg_color = bg_color
        self.ship = ship
        self.aliens = aliens
        self.bullets = bullets

    def _render_screen(self) -> None:
        #Redesenha a tela a cada passagem pelo laço
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()


    def _draw_bullets(self) -> None:
       #Desenha os projéteis na tela.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()