import pygame

pygame.init()

#----------------- Criação da Tela --------------------#
LARGURA= 800
ALTURA= 450
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('THE ARCHER')

#----------------- Inicia estrutura de dados --------------------#
game=True

#----------------- Assets --------------------#
#imagens



#----------------- Pre sets --------------------#

Gravidade = 5



TipoTerreno = {T:"Terra",F: "Fundo", P:"Plataforma"}





































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




    



