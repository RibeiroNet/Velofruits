#DESENVOLVIDO POR NETO RIBEIRO 

import pygame


pygame.init()

#TELA
pygame.display.set_caption("Velofruits")
tela = pygame.display.set_mode((800,500))
tela.fill((80,120,200))


#IMAGEM DE FUNDO
FUNDO = pygame.image.load("imagens/fundo.png")
FUNDO = pygame.transform.scale(FUNDO,(800,500))

#RELÓGIO FPS
clock = pygame.time.Clock()

#RODANDO O JOGO
funcionando = True
while funcionando:
    #EVENTOS 
    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou!!")
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO,(0,0))

#CRIANDO JOGADOR
jogador1 = Jogador("imagens/.png",40,30,400,460)