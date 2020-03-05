"""
Jogo da velha

campos do tabuleiro
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
"""


class JogoDaVelha:
    def __init__(self):
        # inicializa tabuleiro
        self._inicializa_tabuleiro()

        # sequencia de possibilidades para se ganhar o jogo
        self.possibilidades = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

        # valores dos jogadores
        self.jogador_x = 1
        self.jogador_o = -1

        # sempre vou começar com o jogador X
        self.jogador_atual = self.jogador_x

        # indica o numero de jogadas em andamento
        self.jogadas = 0

    """
    campos do tabuleiro iniciam com valor 0 (zero)
    """
    def _inicializa_tabuleiro(self):
        self.tabuleiro = {x + 1: 0 for x in range(9)}

    """
    Marca a casa jogada
    """
    def _executa_jogada(self, casa):
        if casa > 9:
            raise()
        self.tabuleiro[casa] = self.jogador_atual
        self.jogadas += 1

    """
    Faz a alternancia dos jogadores
    """
    def _troca_jogador(self):
        if self.jogador_atual == self.jogador_x:
            self.jogador_atual = self.jogador_o
        else:
            self.jogador_atual = self.jogador_x

    """
    verifica se o jogador atual ganhou o jogo
    """
    def _verifica_ganhador(self):
        for i in self.possibilidades:
            ganhou = 0
            for n in i:
                if self.tabuleiro[n] == self.jogador_atual:
                    ganhou += 1
            if ganhou == 3:
                return True
        return False

    """
    Verifica se houve empate
    """
    def _verifica_empate(self):
        if self.jogadas >= 9:
            return True
        else:
            return False

    """
    Indica qual jogador deve iniciar o jogo
    Se o jogo já iniciou retorna False
    """
    def set_jogador(self, jogador='X'):
        if self.jogadas == 0:
            if jogador.upper() == 'O':
                self.jogador_atual = self.jogador_o
            else:
                self.jogador_atual = self.jogador_x
            return True
        else:
            return False

    """
    Retorna o rótulo do jogador
    """
    def get_jogador(self):
        if self.jogador_atual == self.jogador_x:
            return 'X'
        else:
            return 'O'
    """
    Exibe estado atual do tabuleiro
    X ou O em casas já jogadas ou o numero da casa em casas vazias
    """
    def exibe_tabuleiro(self):
        t = {}

        for k in self.tabuleiro.keys():
            if self.tabuleiro[k] == self.jogador_x:
                t[k] = 'X'
            elif self.tabuleiro[k] == self.jogador_o:
                t[k] = 'O'
            else:
                t[k] = k

        print('''
             {} | {} | {}
            -----------
             {} | {} | {}
            -----------
             {} | {} | {}
        '''.format(t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9]))

    """
    Logica principal do jogo
    """
    def jogar(self):
        while not self._verifica_ganhador() and not self._verifica_empate():
            try:
                self.exibe_tabuleiro()
                casa = int(input(f'Jogador {self.get_jogador()}, selecione um campo: '))
                self._executa_jogada(casa)
                if not self._verifica_ganhador():
                    self._troca_jogador()

            except Exception:
                print('Jogada inválida, informe o numero de uma casa não jogada!')



        # exibe informação de vitpria
        if self._verifica_ganhador():
            self.exibe_tabuleiro()
            print(f'Jogador {self.get_jogador()} GANHOU o jogo')

        # exibe informação de empate
        if self._verifica_empate():
            self.exibe_tabuleiro()
            print('O jogo acabou EMPATADO')



v = JogoDaVelha()
v.jogar()
