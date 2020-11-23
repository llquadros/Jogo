import pygame
import os
import sys
import random

pygame.init()

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
arquivo2 = os.path.join('imagens','Dragão' ,'frame-1.png')


# carregando imagem
try:
    cenario = pygame.image.load(arquivo0).convert() #imagem de backgroud
    flecha_img = pygame.image.load(arquivo1).convert_alpha()
    dragao_img= pygame.image.load(arquivo2).convert_alpha()
except pygame.error:
    sys.exit()

#modificando escala das imagens    
flecha_img = pygame.transform.scale(flecha_img, (100, 100))
dragao_img = pygame.transform.scale(dragao_img, (100, 100))
#----------------- Inicia estrutura de dados --------------------#
game=True

Gravidade = 5

clock = pygame.time.Clock()

#classes
class Flecha(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = (200)
        self.rect.y = (200)
        self.speedy = (6)
        self.gravidade = (0.1)
        #self.speedx = (funçao)
        # self.mask = pygame.mask.from_surface(fruit_img)
        # self.mask = pygame.mask.from_surface(fruit2_img)

    # def update(self, fps):
    #     # Atualizando a posição da fruta 
    #     self.rect.y += -self.speedy + self.gravidade
    #     # Se a fruta passar do final da tela, volta para cima e sorteia
    #     # novas posições e velocidades
    #     if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
    #         self.rect.x = random.randint(0, WIDTH-FRUIT_WIDTH)
    #         self.rect.y = random.randint(-100, -FRUIT_HEIGHT)
    #         self.speedy = random.randint(2, 5)



class Dragão(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image= img 
        self.rect= self.image.get_rect()
        self.rect.x= random.randint(LARGURA-LARGURA/5, LARGURA)
        self.rect.y= random.randint(0, ALTURA-altura_chão)
        self.speedx= -2
        self.speedy= 2
        self.mask = pygame.mask.from_surface(dragao_img)
        self.mask = pygame.mask.from_surface(dragao_img)

    def update (self, fps):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # if self.rect.left = 0:
        #     self.speedx = 0
        # if self.rect.botton = altura_chão:
        #     self.speedy = 0





# class arqueiro:
#     def __init__(self, img):

ob_flecha = Flecha(flecha_img)
ob_dragao= Dragão(dragao_img)

# for dragao in Dragão
#     ob_dragao = Dragão()
sprites = pygame.sprite.Group()
sprites2 = pygame.sprite.Group()
#criando flecha
sprites.add(ob_flecha)


# loop de criação dos dragões 
for i in range(4):
    ob_dragao= Dragão(dragao_img)
    sprites2.add(ob_dragao)

#contador marcador de pontos
score = 0     

while game:
    fps = clock.tick(60) #define FPS
    eventos = pygame.event.get() # função que pega qualquer evento dentro da janela (qualquer botao clicado)
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()# finaliza pygame
            sys.exit()#finaliza sistema
            game = False

    

    # Verifica se houve contato entre o player e a bomba
    hits = pygame.sprite.spritecollide(ob_flecha, sprites2, True, pygame.sprite.collide_mask)
    
    for dragao in hits:
        #pop_sound.play()
        d = Dragão(dragao_img)
        score += 10               
        sprites2.add(d)
        sprites2.add(d)

    window.blit(cenario, (0, 0))
    #adiciona o score na tela
    # text_surface = assets['score_font'].render("{:08d}".format(score), True, (255, 255, 0))
    # text_rect = text_surface.get_rect()
    # text_rect.midtop = (WIDTH / 2,  10)
    # window.blit(text_surface, text_rect)

    sprites.update(fps)
    sprites.draw(window)
    sprites2.update(fps)
    sprites2.draw(window)
    pygame.display.flip()# atualiza a tela






































    



