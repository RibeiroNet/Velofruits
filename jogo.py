#DESENVOLVIDO POR NETO RIBEIRO 
import pygame

#CRIA JANELA DO JOGO
pygame.init()

#TELA
pygame.display.set_caption("Corrida do CLT")
tela = pygame.display.set_mode((800,500))

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
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO,(0,0))

     #ATUALIZA TELA 
    pygame.display.update()

    #REGULA FPS
    clock.tick(60)
