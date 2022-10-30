import random

class Feature:
    def __init__(self, life, atk, defs, vel, atk1, atk2):  # STATUS DOS PERSONAGENS
        self.life = life
        self.atk = atk
        self.defs = defs
        self.vel = vel
        self.atk1 = atk1
        self.atk2 = atk2

    def cal_catk1_lin(self):    # CALCULO DO ATAQUE 1 DE LINCONL
        linconl.atk1 = random.randint(5, 15)
        abraham.life = abraham.life - \
            (linconl.atk1 * linconl.atk) / abraham.defs

    def cal_catk2_lin(self):    # CALCULO DO ATAQUE 2 DE LINCONL
        linconl.atk2 = random.randint(15, 40)
        abraham.life = abraham.life - \
            (linconl.atk1 * linconl.atk) / abraham.defs
        linconl.atk = linconl.atk - 3

    def calc_atk1_abr(self):    # CALCULO DO ATAQUE 1 DE ABRAHAM
        abraham.atk1 = random.randint(5, 15)
        linconl.life = linconl.life - \
            (abraham.atk1 * abraham.atk) / linconl.defs

    def cal_catk2_abr(self):    # CALCULO DO ATAQUE 2 DE ABRAHAM
        abraham.atk2 = random.randint(15, 40)
        linconl.life = linconl.life - \
            (abraham.atk1 * abraham.atk) / linconl.defs
        abraham.atk = abraham.atk - 3

    def up_stats1(self):    # UP STATS DOS PERSONAGENS
        self.vel += 10

    def down_stats1(self):      # ABAIXAR STATUS DO ADVERSARIO
        self.defs = self.defs - 10

# -======================================================================================================================================================-

    def funatklin_1(self):        # FUNCAO DO PRIMEIRO ATAQUE DO LINCONL
        self.cal_catk1_lin()
        input('Aperte "ENTER" para prosseguir')

        print('\nDANO CAUSADO {}'.format(self.atk1))

    def funatklin_2(self):        # FUNCAO DO SEGUNDO ATAQUE DO LINCONL
        self.cal_catk2_lin()
        input('Aperte "ENTER" para prosseguir')

        print('\nDANO CAUSADO {}\n\nREDUÇÂO DO ATAQUE DO USUARIO!!'.format(self.atk2))

    def funatkabr_1(self):        # FUNCAO DO PRIMEIRO ATAQUE DO ABRAHAM
        self.calc_atk1_abr()
        input('Aperte "ENTER" para prosseguir')

        print('\nDANO CAUSADO {}'.format(self.atk1))

    def funatkabr_2(self):        # FUNCAO DO SEGUNDO ATAQUE DO ABRAHAM
        self.cal_catk2_abr()
        input('Aperte "ENTER" para prosseguir')

        print('\nDANO CAUSADO {}\n\nREDUÇÂO DO ATAQUE DO USUARIO!!'.format(self.atk2))

    def funatk_3(self):        # FUNCAO DO TERCEIRO ATAQUE
        self.up_stats1()
        input('Aperte "ENTER" para prosseguir')

        print('\nStatus de VELOCIDADE do usuário AUMENTADO!!')

    def funatk_4(self):        # FUNCAO DO QUARTO ATAQUE
        self.down_stats1()
        input('Aperte "ENTER" para prosseguir')

        print('\nStatus de DEFESA do adversário REDUZIDA!!')

# -======================================================================================================================================================-

    def death(self):   # MORTE
        if self.life < 0:
            self.life = 0

    def cri_1(self):   # ATAQUE 1 CRITICO
        if self.atk1 > 12:
            print('\nATAQUE CRÍTICO!')

    def cri_2(self):   # ATAQUE 2 CRITICO
        if linconl.atk2 > 33:
            print('\nATAQUE CRÍTICO!')

    def advance(self):     # AVANÇAR COM A BATALHA
        print('\nVIDA DO ADVESÁRIO: {:.0f}\n\n'.format(self.life))

        input('Aperte "ENTER" para prosseguir')


# DEFININDO STAUS DO PERSONAGENS
abraham = Feature(200, 80, 60, 25, random.randint(
    5, 15), random.randint(15, 40))

# DEFININDO STAUS DO PERSONAGENS
linconl = Feature(200, 55, 100, 25, random.randint(
    5, 15), random.randint(15, 40))

# -======================================================================================================================================================-

while linconl.life > 0 and abraham.life > 0:
    print('''==========================================
    VEZ DE LINCONL
    ''')
    print('VIDA: {:.0f} | ATAQUE: {:.0f} | DEFESA: {:.0f} | VELOCIDADE: {:.0f} |\n'.format(
        linconl.life, linconl.atk, linconl.defs, linconl.vel))
    print('''    ATAQUE 1 = 1
    ATAQUE 2 = 2
    AUMENTO DE VEL = 3
    REDUÇÃO DE DEF = 4''')
    op = int(input('Escolha seu ataque: '))
    print('==========================================')

    print('''\n\n==========================================
    VEZ DE ABRAHAM
    ''')
    print('VIDA: {:.0f} | ATAQUE: {:.0f} | DEFESA: {:.0f} | VELOCIDADE: {:.0f} |\n\033[m'.format(
        abraham.life, abraham.atk, abraham.defs, abraham.vel))
    print('''    ATAQUE 1 = 1
    ATAQUE 2 = 2
    AUMENTO DE VEL = 3
    REDUÇÃO DE DEF = 4''')
    ip = int(input('Escolha seu ataque: '))
    print('==========================================')

# -======================================================================================================================================================-

    if linconl.vel > abraham.vel:      # SE A VELOCIDADE DE UM FOR MAIOR QUE A DO OUTRO

        if op == 1:
            print('\nLINCONL ATACA...')
            linconl.funatklin_1()
            abraham.death()
            linconl.cri_1()
            abraham.advance()

        elif op == 2:
            print('\nLINCONL ATACA...')
            linconl.funatklin_2()
            abraham.death()
            linconl.cri_2()
            abraham.advance()

        elif op == 3:
            print('\nLINCONL ATACA...')
            linconl.funatk_3()
            abraham.advance()

        elif op == 4:
            print('\nLINCONL ATACA...')
            abraham.funatk_4()
            abraham.advance()

        if ip == 1:
            print('\nABRAHAM ATACA...')
            abraham.funatkabr_1()
            linconl.death()
            abraham.cri_1()
            linconl.advance()

        elif ip == 2:
            print('\nABRAHAM ATACA...')
            abraham.funatkabr_2()
            linconl.death()
            abraham.cri_2()
            linconl.advance()

        elif ip == 3:
            print('\nABRAHAM ATACA...')
            abraham.funatk_3()
            linconl.advance()

        elif ip == 4:
            print('\nABRAHAM ATACA...')
            linconl.funatk_4()
            linconl.advance()

# -======================================================================================================================================================-

    elif abraham.vel > linconl.vel:     # SE A VELOCIDADE DE UM FOR MAIOR QUE A DO OUTRO
        if ip == 1:
            print('\nABRAHAM ATACA...')
            abraham.funatkabr_1()
            linconl.death()
            abraham.cri_1()
            linconl.advance()

        elif ip == 2:
            print('\nABRAHAM ATACA...')
            abraham.funatkabr_2()
            linconl.death()
            abraham.cri_2()
            linconl.advance()

        elif ip == 3:
            print('\nABRAHAM ATACA...')
            abraham.funatk_3()
            linconl.advance()

        elif ip == 4:
            print('\nABRAHAM ATACA...')
            linconl.funatk_4()
            linconl.advance()

        if op == 1:
            print('\nLINCONL ATACA...')
            linconl.funatklin_1()
            abraham.death()
            linconl.cri_1()
            abraham.advance()

        elif op == 2:
            print('\nLINCONL ATACA...')
            linconl.funatklin_2()
            abraham.death()
            linconl.cri_2()
            abraham.advance()

        elif op == 3:
            print('\nLINCONL ATACA...')
            linconl.funatk_3()
            abraham.advance()

        elif op == 4:
            print('\nLINCONL ATACA...')
            abraham.funatk_4()
            abraham.advance()

# -======================================================================================================================================================-

    elif linconl.vel == abraham.vel:        # SE A VELOCIDADE DOS DOIS FOREM IGUAIS
        esc = random.randint(1, 2)       # RANDOMIZAR QUEM ATACA PRIMEIRO

        if esc == 1:
            if op == 1:
                print('\nLINCONL ATACA...')
                linconl.funatklin_1()
                abraham.death()
                linconl.cri_1()
                abraham.advance()

            elif op == 2:
                print('\nLINCONL ATACA...')
                linconl.funatklin_2()
                abraham.death()
                linconl.cri_2()
                abraham.advance()

            elif op == 3:
                print('\nLINCONL ATACA...')
                linconl.funatk_3()
                abraham.advance()

            elif op == 4:
                print('\nLINCONL ATACA...')
                abraham.funatk_4()
                abraham.advance()

            if ip == 1:
                print('\nABRAHAM ATACA...')
                abraham.funatkabr_1()
                linconl.death()
                abraham.cri_1()
                linconl.advance()

            elif ip == 2:
                print('\nABRAHAM ATACA...')
                abraham.funatkabr_2()
                linconl.death()
                abraham.cri_2()
                linconl.advance()

            elif ip == 3:
                print('\nABRAHAM ATACA...')
                abraham.funatk_3()
                linconl.advance()

            elif ip == 4:
                print('\nABRAHAM ATACA...')
                linconl.funatk_4()
                linconl.advance()

# -======================================================================================================================================================-

        elif esc == 2:
            if ip == 1:
                print('\nABRAHAM ATACA...')
                abraham.funatkabr_1()
                linconl.death()
                abraham.cri_1()
                linconl.advance()

            elif ip == 2:
                print('\nABRAHAM ATACA...')
                abraham.funatkabr_2()
                linconl.death()
                abraham.cri_2()
                linconl.advance()

            elif ip == 3:
                print('\nABRAHAM ATACA...')
                abraham.funatk_3()
                linconl.advance()

            elif ip == 4:
                print('\nABRAHAM ATACA...')
                linconl.funatk_4()
                linconl.advance()

            if op == 1:
                print('\nLINCONL ATACA...')
                linconl.funatklin_1()
                abraham.death()
                linconl.cri_1()
                abraham.advance()

            elif op == 2:
                print('\nLINCONL ATACA...')
                linconl.funatklin_2()
                abraham.death()
                linconl.cri_2()
                abraham.advance()

            elif op == 3:
                print('\nLINCONL ATACA...')
                linconl.funatk_3()
                abraham.advance()

            elif op == 4:
                print('\nLINCONL ATACA...')
                abraham.funatk_4()
                abraham.advance()

print('FIM...')
