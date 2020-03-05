
def mostra_tabuleiro(t):

    print(f'''
     {t[1]} | {t[2]} | {t[3]}
    -----------
     {t[4]} | {t[5]} | {t[6]}
    -----------
     {t[7]} | {t[8]} | {t[9]}
    ''')

def verifica_tabuleiro(campo, t):
    if t[campo] != 'X' and t[campo] != 'O':
        return True
    else:
        return False

def muda_jogador(j):
    if j == 'X':
        return 'O'
    else:
        return 'X'

def verifica_ganhador(t, j):
    possibilidades = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for i in possibilidades:
        ganhou = 0
        for n in i:
            if t[n] == j:
                ganhou += 1
        if ganhou == 3:
            return True
    return False

def jogo():
    tabuleiro = {x+1:x+1 for x in range(9)}
    jogador = 'X'
    vencedor = ''
    jogadas = 1

    while vencedor == '':
        try:
            mostra_tabuleiro(tabuleiro)
            if jogadas > 9:
                print('jogo empatou')
                exit()

            campo = int(input(f'Jogador {jogador}, selecione um campo: '))

            if verifica_tabuleiro(campo, tabuleiro):
                tabuleiro[campo] = jogador
                if verifica_ganhador(tabuleiro, jogador):
                    vencedor = jogador
                else:
                    jogador = muda_jogador(jogador)
                    jogadas += 1
            else:
                print('Jogada inválida')
        except Exception:
            print('Jogada inválida')

    print(f'O jogador {jogador} é o vencedor')
    mostra_tabuleiro(tabuleiro)

jogo()
