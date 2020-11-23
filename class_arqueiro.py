# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os

#-------------------------

# ----- Gera tela principal

WIDTH = 700
HEIGHT = 400
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Inicia pygame e cria uma janela(tela)

pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Archer")
clock = pygame.time.Clock()

# ----- Inicia assets
background = os.path.join('imagens', 'cenário.jpg')
background = pygame.image.load(background).convert()

class Arqueiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

all_sprites = pygame.sprite.Group()
arqueiro = Arqueiro()
all_sprites.add(arqueiro)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False



    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    all_sprites.draw(window)
    # *after* drawing everything, flip the display
    pygame.display.flip()

# ----- Atualiza estado do jogo
all_sprites.update()
pygame.display.update()


# ===== Finalização =====
pygame.quit()

