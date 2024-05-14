#DESENVOLVIDO POR NETO RIBEIRO 

import pygame

pygame.init()

#TELA
tela = pygame.display.set_mode((800,500))
pygame.display.set_caption("Velofruits")
tela.fill((80,120,200))

#IMAGEM DE FUNDO
FUNDO = pygame.image.load("imagens/fundo.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))
