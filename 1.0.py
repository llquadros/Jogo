import pygame
import os
import sys

pygame.init()

#testando github
#----------------- Criação da Tela --------------------#
LARGURA= 700
ALTURA= 400
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('THE ARCHER')

# carregando imagens
cenario = pygame.image.load("cenário.png").convert_alpha()

#----------------- Inicia estrutura de dados --------------------#
game=True

#----------------- Assets --------------------#
#imagens



#----------------- Pre sets --------------------#

Gravidade = 5

clock = pygame.time.Clock()

#classes
class flecha:
    def __init__(self,x_coord,y_coord):
        self.x=x_coord
        self.y=y_coord

    def distancia(self, outro_ponto):
        dx= outro_ponto.x - self.x
        dy=outro_ponto.y- self.y
        return ()

while True:
    fps = clock.tick(60) #define FPS 
    eventos = pygame.event.get() # função que pega qualquer evento dentro da janela (qualquer botao clicado)
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()# finaliza pygame
            sys.exit()#finaliza sistema

    window.blit(cenario, (0, 0))

































#----------------- Loop principal --------------------#

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (100, 100))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados




    



