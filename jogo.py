#DESENVOLVIDO POR NETO RIBEIRO 
import pygame
from personagem import Personagem



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

#CRIANDO PERSONAGEM
jogador1 = Personagem("imagens/funcionário.png",60,60,350,390)

#CRIANDO OBJETOS
lista_objetos = [objeto("imagens/comida.png",100,50,0,0),
                objeto("imagens/dinheiro.png",100,50,0,0),
                objeto("imagens/sono.png",100,50,0,0),
                objeto("imagens/viagem.png",100,50,0,0),
                objeto("imagens/festa.png",100,50,0,0),
                objeto("imagens/chefe.png",100,50,0,0),
                objeto("imagens/chocolate.png",100,50,0,0)]



#RODANDO O JOGO
funcionando = True
while funcionando:
    #EVENTOS 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(FUNDO,(0,0))

    jogador1.movimenta_via_controle(pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.apareca(tela)

    


     #ATUALIZA TELA 
    pygame.display.update()

    #REGULA FPS
    clock.tick(60)
