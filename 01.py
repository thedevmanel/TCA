from webbrowser import BackgroundBrowser
import pygame as jooj
from pygame.locals import *     # IMPORTANDO TODAS AS FUNÇOES DO "LOCALS"
from sys import exit            #  PARA PODER FECHAR A JANELA

jooj.init()         # INICIANDO TODAS AS FUNÇOES E BIBLIOTECAS DO PYGAME

largura = 640
altura = 480

janela = jooj.display.set_mode((largura, altura))      # CRIANDO A TELA DO JOGO

while True:
    background = display.fill(255, 255, 255)
    for event in jooj.event.get():      # CHECAR SE HOUBE ALGUM INPUT DO TECLADO
        if event.type == QUIT:
            jooj.quit()
