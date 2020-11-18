import pygame
import os
import sys

pygame.init()

#testando

#testando github
#----------------- Criação da Tela --------------------#
LARGURA= 700
ALTURA= 400
altura_chão = 360
altura_boneco = 10
posicao_y_boneco = altura_chão - altura_boneco 
posicao_x_boneco = 175 #posição eixo x do jogador

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('THE ARCHER')

# linkando pasta com arquivo
arquivo0 = os.path.join('imagens', 'cenário.jpg')
arquivo1 = os.path.join('imagens', 'flecha.png')

# carregando imagem
try:
    cenario = pygame.image.load(arquivo0).convert()
    flecha = pygame.image.load(arquivo1).convert_alpha()
except pygame.error:
    sys.exit()

#modificando escala das imagens    
flecha = pygame.transform.scale(flecha, (100, 100))
#----------------- Inicia estrutura de dados --------------------#
game=True

#----------------- Assets --------------------#
#imagens

#----------------- Pre sets --------------------#

Gravidade = 5

clock = pygame.time.Clock()

#classes
class Flecha(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (posicao_x_boneco)
        self.rect.y = (posicao_y_boneco + 1/3 * altura_boneco)
        self.speedy = (6)
        self.gravidade = (0.1)
        #self.speedx = (funçao)
        self.mask = pygame.mask.from_surface(fruit_img)
        self.mask = pygame.mask.from_surface(fruit2_img)

    def update(self):
        # Atualizando a posição da fruta 
        self.rect.y += -self.speedy + self.gravidade
        # Se a fruta passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-FRUIT_WIDTH)
            self.rect.y = random.randint(-100, -FRUIT_HEIGHT)
            self.speedy = random.randint(2, 5)

# class arqueiro:
#     def __init__(self, img):

while game:
    fps = clock.tick(60) #define FPS
    eventos = pygame.event.get() # função que pega qualquer evento dentro da janela (qualquer botao clicado)
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()# finaliza pygame
            sys.exit()#finaliza sistema
            game = False

    window.blit(cenario, (0, 0))
    window.blit(flecha, (200, 200))
    pygame.display.flip()# atualiza a tela






































    



