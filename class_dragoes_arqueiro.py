# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os




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
pygame.display.set_caption("The Archer!")
clock = pygame.time.Clock()

# ----- Inicia assets
background = os.path.join('imagens', 'cenário.jpg')
dragao_image = os.path.join('imagens','Dragão' ,'frame-1.png')
arqueiro_image = os.path.join('imagens','archer.png')
flecha_image = os.path.join('imagens','flecha.png')

#carrega imagens
background = pygame.image.load(background)
dragao_image = pygame.image.load(dragao_image).convert_alpha()
arqueiro_image = pygame.image.load(arqueiro_image).convert_alpha()
flecha_image = pygame.image.load(flecha_image).convert_alpha()


#reajuste de tamanho das imagens

class Arqueiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(arqueiro_image,(80,60))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/10
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

    def shoot(self):
        bullet = Bullet(self.rect.topleft,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(dragao_image ,(60,35))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(HEIGHT- self.rect.height)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 2)
        self.speedx = random.randrange(-1,3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > HEIGHT + 10 or self.rect.left <-25 or self.rect.right>WIDTH+20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 6)


class Bullet(pygame.sprite.Sprite):#classe para flechas
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(flecha_image ,(100,50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.topleft= x
        self.speedy = -5

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()




all_sprites = pygame.sprite.Group()
mobs =pygame.sprite.Group()
bullets = pygame.sprite.Group()
arqueiro = Arqueiro()
all_sprites.add(arqueiro)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)



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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                arqueiro.shoot()





    # ----- Atualiza estado do jogo
    all_sprites.update()
    pygame.display.update()

#verifica se a flecha atinge o dragão
    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)



#verifica se o dragão colide com o arqueiro
    hits = pygame.sprite.spritecollide(arqueiro,mobs,False)
    if hits:
        running = False



    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    all_sprites.draw(window)
    # *after* drawing everything, flip the display
    pygame.display.flip()

# ===== Finalização =====
pygame.quit()
