# ===== Inicialização =====
# ----- Importa e inicia pacotes

#obs: Musicas, sons e imagens são de codigo aberto , estavao portanto sem autores para eu colocar como ref.


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

musics = os.path.join(os.path.dirname(__file__),'musicas')




#carrega imagens
background = pygame.image.load(background)
dragao_image = pygame.image.load(dragao_image).convert_alpha()
arqueiro_image = pygame.image.load(arqueiro_image).convert_alpha()
flecha_image = pygame.image.load(flecha_image).convert_alpha()


#carregando sons

flecha_sound = pygame.mixer.Sound(os.path.join(musics,"explosion_dull.flac"))
expl_sounds = []
for music in ['explosion_dull.flac']:
    expl_sounds.append(pygame.mixer.Sound(os.path.join(musics,music)))

pygame.mixer.music.load(os.path.join(musics,'battle theme.flac'))
pygame.mixer.music.set_volume(0.4)


##Escreve na Tela
font_name = pygame.font.match_font('arial') #fonte da letra
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


##....
def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

#funcão para o status bar
def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)




class Arqueiro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(arqueiro_image,(80,60))#reajuste de tamanho das imagens
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/10
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.shield = 100 #"status bar"-

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
        flecha_sound.play()




class Mob(pygame.sprite.Sprite):#classe dos dragões
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(dragao_image ,(60,35))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85/2)
        self.rect.x = random.randrange(HEIGHT- self.rect.height)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 2)
        self.speedx = random.randrange(-1,3)
        self.rot = 0 #para os dragoes rotacionarem
        self.rot_speed = random.randrange(-8,8) #velocida de rotacao
        self_last_update = pygame.time.get_ticks()


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
    newmob()

score = 0  #pontuação inicial
pygame.mixer.music.play(loops=-1)# #inicia musica de fundo


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
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        newmob()



#verifica se o dragão colide com o arqueiro
    hits = pygame.sprite.spritecollide(arqueiro,mobs,True, pygame.sprite.collide_circle)
    for hit in hits: #se o "escudo" chegar a 0 o jogo termina
        arqueiro.shield -= hit.radius * 2 #um escudo para cada acerto cm base em seu raio
        newmob()
        if arqueiro.shield <= 0:
            running = False


    # ----- Gera saídas/desenhos na tela
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    all_sprites.draw(window)
    draw_text(window,str(score),18,WIDTH/2,10)
    draw_shield_bar(window,5,5,arqueiro.shield) #desenha status bar



    pygame.display.flip()

# ===== Finalização =====
pygame.quit()
