import pygame as jooj

jooj.init() # Faz a biblioteca funfar

width = 640
height = 480

display = jooj.display.set_mode([width, height]) # Janela
jooj.display.set_caption('Jogo legal') # Nome da janela

#                      x    y    w  h                 "PLANO CARTESIANO"
retangulo = jooj.Rect(200, 100, 12, 5) # Criando 

# retangulo.center = ´[]

# drawGroup = pygame.sprite.Group()     
# personagem = pygame.sprite.Sprite(drawGroup)
# personagem.image = pygame.image.load("<nome da pasta>/<arquivo.png>")     Chamar imagem 
# personagem.image = pygame.transform.scale(personagem.image, [100, 100])
# personagem.rect = pygame.Rect(500, 100, 100, 100)


gameLoop = True # Para manter a janela ligada
while gameLoop: # Pode se usar o Whilhe True, mas vai ficar assim
    background = display.fill([255, 000, 100]) # Ele vai ficar com a tela com as denominações de cors em RGB
    
    for event in jooj.event.get(): # Quando houver um evento ele faz o tal evento
        if event.type == jooj.QUIT: # Se apertar o "X" ele fecha
            gameLoop = False

        keys = jooj.key.get_pressed() # A variavel ira receber TODAS AS TECLAS PRESSIONADAS, vai servir como um enquanto

        if keys[jooj.K_a]:
            jooj.draw.rect(display, [000, 000, 000, 255], retangulo) # Ultimo parametro é a transparencia

            # drawGropu.draw(display)

# Quando apertar apenas um botao da para usar isso

        # elif event.type == jooj.KEYDOWN: # "KEYDOWN" se refere a tecla que foi apertada
        #     if event.key == jooj.K_a: # É meio que "enquanto a tecla estiver precionada, faça"
        #         display.fill([255, 255, 255])


        # elif event.type == jooj.KEYUP: 
        #     if event.key == jooj.K_q:# "event .key" event de evento & key de tecla do teclado-
        #         gameLoop = False      
        
        jooj.display.update()
