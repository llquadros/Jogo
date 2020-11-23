# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import os
pygame.init()

# ----- Gera tela principal
WIDTH = 700
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The Archer')

# ----- Inicia assets

dragao_width = 50
dragao_height = 38
font = pygame.font.SysFont(None, 48)
background = os.path.join('imagens', 'cenário.jpg')
background = pygame.image.load(background).convert()

dragao_image = os.path.join('imagens','Dragão' ,'frame-1.png')
dragao_image= pygame.image.load(dragao_image).convert_alpha()
dragao_image_reajuste = pygame.transform.scale(dragao_image,(dragao_width,dragao_height))

# ----- Inicia estruturas de dados
game = True
# Sorteia posição aleatória
# Como x é o lado esquerdo da imagem, ele só pode ir até a largura da
# janela menos a largura da imagem
dragao_x = random.randint(0, WIDTH-dragao_width)
# y negativo significa que está acima do topo da janela. O dragao começa fora da janela
dragao_y = random.randint(-100, -dragao_height)
# Sorteia velocidade do dragao
dragao_speedx = random.randint(-3,3)
dragao_speedy = random.randint(2,9)

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 15


# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False


 # ----- Atualiza estado do jogo
    # Atualizando a posição do dragao
    dragao_x += dragao_speedx
    dragao_y+= dragao_speedy
    # Se o dragao passar do final da tela, volta para cima e sorteia
    # novas posições e velocidades
    if dragao_y > HEIGHT or dragao_x + dragao_width < 0 or dragao_x > WIDTH:
        dragao_x = random.randint(0,WIDTH-dragao_width)
        dragao_y = random.randint(-100,-dragao_height)
        dragao_speedx = random.randint(-3,3)
        dragao_speedy = random.randint(2,9)

# ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    window.blit(dragao_image_reajuste , (dragao_x, dragao_y))
    pygame.display.update()  # Mostra o novo frame para o jogador


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
