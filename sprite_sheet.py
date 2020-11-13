import pygame


class SpriteSheet():
#classe para recortar as imagens da sprite sheet

    sprite_sheet = None

    def __init__(self,file_name):
        #carrega a imagem 
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def recorta(self, x, y, largura, altura):
        # vai até a posição x,y e recorta a figura com largura e altura definida

        #cria uma imagem vazia
        image= pygame.Surface([largura,altura]).convert()
        
        #atribui a imagem o recorte
        image.blit(self.sprite_sheet, (0,0),(x, y, largura, altura))


        image.set_colorkey(0,0,0)
        

        return image
        

        