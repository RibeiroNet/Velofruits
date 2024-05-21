#DESENVOLVIDO POR NETO RIBEIRO 
import pygame
import random
from personagem import Personagem
from objetos import objeto

#CRIA JANELA DO JOGO
pygame.init()

#CONFIGURANDO A FONTE
fonte = pygame.font.SysFont("Arial", 14,)

#MÚSICA E SONS
som_bomba = pygame.mixer.Sound("sons/som_bomba.mp3")
som_ponto = pygame.mixer.Sound("sons/som_ponto.mp3")
som_final = pygame.mixer.Sound("sons/som_final.mp3")

#MÚSICA DE FUNDO
pygame.mixer.music.load("sons/som_fundo.mp3")
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.mixer.music.play()

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
lista_objetos = [objeto("imagens/comida.png",50,50,random.randint(100,700),0),
                 objeto("imagens/dinheiro.png",50,50,random.randint(100,700),0),
                 objeto("imagens/sono.png",50,50,random.randint(100,700),0),
                 objeto("imagens/viagem.png",50,50,random.randint(100,700),0),
                 objeto("imagens/festa.png",50,50,random.randint(100,700),0),          
                 objeto("imagens/donut.png",50,50,random.randint(100,700),0),
                 objeto("imagens/chocolate.png",50,50,random.randint(100,700),0)]

#LISTA BOMBA
lista_bomba = [objeto("imagens/chefe.png",80,80,random.randint(100,700),0),
               objeto("imagens/chefe.png",80,80,random.randint(100,700),0),
               objeto("imagens/chefe.png",80,80,random.randint(100,700),0)]


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

    for objeto in lista_bomba:
        objeto.movimenta()
        objeto.apareca(tela)  

        if jogador1.mascara.overlap(objeto.mascara,(objeto.pos_x-jogador1.pos_x , objeto.pos_y-jogador1.pos_y)):
            jogador1.pos_x = 350
            jogador1.pos_y = 390
            jogador1.pontuacao -= 5
            objeto.pos_y = 1 
            objeto.pos_x = random.randint(100,700)
            som_bomba.play()
          


    for objeto in lista_objetos:
        objeto.movimenta()
        objeto.apareca(tela)
         
        if jogador1.mascara.overlap(objeto.mascara,(objeto.pos_x-jogador1.pos_x , objeto.pos_y-jogador1.pos_y)):
            jogador1.pontuacao += 1
            objeto.pos_y = 1
            objeto.pos_x = random.randint(100,700)
            som_ponto.play()

    if jogador1.pontuacao < 0:
        tela.fill((0,0,0))
        texto_pontuacao_funcionario = fonte.render("Game Over!",True,(0,0,255))
        tela.blit(texto_pontuacao_funcionario,(350,104))
        som_final.play()
        
    if jogador1.pontuacao > 100:
        tela.fill((0,0,0))
        texto_pontuacao_funcionario = fonte.render("YOUR WIN!",True,(0,0,255))
        tela.blit(texto_pontuacao_funcionario,(350,104))
     


    texto_pontuacao_funcionario = fonte.render(f"Pontuação: {jogador1.pontuacao}",True,(0,0,0))
    tela.blit(texto_pontuacao_funcionario,(0,24))
    

    #ATUALIZA TELA 
    pygame.display.update()

    #REGULA FPS
    clock.tick(60)
