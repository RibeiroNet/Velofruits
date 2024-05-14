#DESENVOLVIDO POR NETO RIBEIRO 
import pygame
from personagem import Personagem
from objetos import objeto

#CRIA JANELA DO JOGO
pygame.init()

#CONFIGURANDO A FONTE
fonte = pygame.font.SysFont("Arial", 14,False,False)



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
lista_objetos = [objeto("imagens/comida.png",50,50,50,0),
                 objeto("imagens/dinheiro.png",50,50,100,0),
                 objeto("imagens/sono.png",50,50,150,0),
                 objeto("imagens/viagem.png",50,50,200,0),
                 objeto("imagens/festa.png",50,50,350,0),
                 objeto("imagens/chefe.png",100,100,450,0),
                 objeto("imagens/donut.png",50,50,120,0),
                 objeto("imagens/chocolate.png",50,50,300,0)]




#RODANDO O JOGO
funcionando = True
while funcionando:
    #EVENTOS 
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            funcionando = False

    tela.blit(FUNDO,(0,0))

    jogador1.movimenta_via_controle(pygame.K_RIGHT,pygame.K_LEFT)
    jogador1.apareca(tela)

    for objeto in lista_objetos:
        objeto.movimenta()
        objeto.apareca(tela)

        if jogador1.mascara.overlap(objeto.mascara,(objeto.pos_x-jogador1.pos_x , objeto.pos_y-jogador1.pos_y)):
            jogador1.pos_x = 350
            jogador1.pos_y = 390
            jogador1.pontuacao -= 1

        if jogador1.pos_y <= 10:
            jogador1.pos_x = 350
            jogador1.pos_y = 390
            jogador1.pontuacao += 1

        texto_pontuacao_funcionario = fonte.render(f"Pontuação: {jogador1.pontuacao}",True,(255,0,0))
        tela.blit(texto_pontuacao_funcionario,(0,24))


    


    #ATUALIZA TELA 
    pygame.display.update()

    #REGULA FPS
    clock.tick(60)
