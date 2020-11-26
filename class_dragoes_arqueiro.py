# ===== Inicialização =====
# ----- Importa e inicia pacotes

#obs: Musicas, sons e imagens são de codigo aberto , estavao portanto sem autores para eu colocar como ref.


import pygame
import random
import os
import math
import time


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
tela_inicial = os.path.join('imagens', 'tela-inicial.jpg')
background1 = os.path.join('imagens', 'cenário.jpg')
dragao_image = os.path.join('imagens','Dragão' ,'frame-1.png')
arqueiro_image = os.path.join('imagens','archer.png')
flecha_image = os.path.join('imagens','flecha.png')



musics = os.path.join(os.path.dirname(__file__),'musicas')

alvo_image = os.path.join('imagens', 'alvo.png')

fonte = pygame.font.Font('fonte/PressStart2P.ttf', 28)


#carregando imagens

background = pygame.image.load(background1)
dragao_image = pygame.image.load(dragao_image).convert_alpha()
arqueiro_image = pygame.image.load(arqueiro_image).convert_alpha()
flecha_image = pygame.image.load(flecha_image).convert_alpha()
startscreen=pygame.image.load(tela_inicial)
startscreen = pygame.transform.scale(startscreen, (WIDTH, HEIGHT))
alvo_image = pygame.image.load(alvo_image).convert_alpha()


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
def newmob(): #adicionar drgão no all_sprites
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
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
        self.rect.bottom = HEIGHT -10
        self.speedx = 0
        self.shield = 100 #"status bar"-
         # Só será possível atirar uma vez a cada 500 milissegundos


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

    def shoot(self, mx, my):
        bullet = Bullet(self.rect.topleft,self.rect.top, mx, my)
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
        self.speedx = random.randrange(-2,2)
        self.rot = 0 #para os dragoes rotacionarem
        self.rot_speed = random.randrange(-8,8) #velocida de rotacao
        
        self_last_update = pygame.time.get_ticks()

#tesyte
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left > WIDTH or self.rect.right<0:
            self.kill
            
        elif self.rect.top > HEIGHT:
            self.kill

class Bullet(pygame.sprite.Sprite):#classe para flechas
    def __init__(self, x, y, mx, my):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(flecha_image ,(100,50))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.topleft= x
        self.speedy = my - arqueiro.rect.top 
        self.speedx = mx - arqueiro.rect.centerx

        self.lad_x= mx- arqueiro.rect.centerx # lado x e lado y para calcular o pitagoras
        self.lad_y= my- arqueiro.rect.centery
        self.tang= self.lad_y/self.lad_x
        if self.lad_x == 0 and self.lad_y > 0:
            self.angle = 360 - 90
        elif self.lad_x == 0 and self.lad_y < 0:
            self.angle = 360 - 180
        else:
            if self.lad_x > 0 and self.lad_y < 0:
                self.angle = - math.degrees(math.atan(self.tang))
            elif self.lad_x > 0 and self.lad_y > 0:
                self.angle = 360 - math.degrees(math.atan(self.tang))
            elif self.lad_x < 0 and self.lad_y > 0:
                self.angle = 180 - math.degrees(math.atan(self.tang))
            elif self.lad_x < 0 and self.lad_y < 0:
                self.angle = 180 - math.degrees(math.atan(self.tang))
        
        
        
        # self.angle =  math.degrees(math.atan(self.tang)) #calcula o angulo de lançamento da flecha  
        self.image = pygame.transform.rotate(self.image, self.angle) #salva a imagem
        

        
        print(self.angle)
    def update(self):
        self.rect.y += self.speedy/ 50
        self.rect.x += self.speedx/ 50

        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
       


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = pygame.transform.scale(alvo_image ,(60,35))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center










all_sprites = pygame.sprite.Group()
mobs =pygame.sprite.Group()
bullets = pygame.sprite.Group()
arqueiro = Arqueiro()
all_sprites.add(arqueiro)
for i in range(8):
    newmob()

score = 0  #pontuação inicial
pygame.mixer.music.play(loops=-1)# #inicia musica de fundo

#-----loop do menu-------
end = False
while (end==False):
    
    window.blit(startscreen, (0,0))
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    nlabel=myfont.render("Press UP to Start", 1, (255, 255, 255))
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                end=True
    window.blit(nlabel,(200,200))
    pygame.display.flip()

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
            if event.key == pygame.K_SPACE or event.key == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                arqueiro.shoot(mx, my)
    




    # ----- Atualiza estado do jogo
    all_sprites.update()
    pygame.display.update()

#verifica se a flecha atinge o dragão
    hits = pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        newmob()
        newmob()



#verifica se o dragão colide com o arqueiro
    hits = pygame.sprite.spritecollide(arqueiro,mobs,True, pygame.sprite.collide_circle)
    for hit in hits: #se o "escudo" chegar a 0 o jogo termina
        arqueiro.shield -= hit.radius * 2 #um escudo para cada acerto cm base em seu raio
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        newmob()
        if arqueiro.shield <= 0:
            running = False


    # ----- Gera saídas/desenhos na tela
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    all_sprites.draw(window)
    draw_text(window,str(score),18,WIDTH/2,10)
    draw_shield_bar(window,5,5,arqueiro.shield) #desenha status ba



    pygame.display.flip()

    #finalização
listascore = []
listascore.append(score)
#cria tela de encerramento do jogo
if running == False:
    window.fill((0, 0, 0))
    myfont=pygame.font.SysFont("Britannic Bold", 50)
    nlabel=myfont.render("your score is:{:08d}".format(score), 1, (255, 255, 255))
    nlabel2=myfont.render("Game Over", 1, (255, 0, 0))
    window.blit(nlabel,(100,200))
    window.blit(nlabel2,(200,150))
    pygame.display.flip()
    time.sleep(3)
    


# ===== Finalização =====
pygame.quit()
