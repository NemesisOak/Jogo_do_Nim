def computador_escolhe_jogada(n, m): #jogada do computador
    if n % (m + 1) == 0:
        print(f'o computador tirou {m} peças')
        return m
    else:
        peças_tiradas = 1
        while (n - peças_tiradas) % (m + 1) != 0 and peças_tiradas <= m:    
            peças_tiradas += 1
        return peças_tiradas
    
def usuario_escolhe_jogada(n, m): #jogada do usuário
    valido = True
    while valido:
        peças_tiradas = int(input('Quantas peças deseja tirar? \n'))
        if peças_tiradas > m or peças_tiradas <= 0:
            print("\njogada não válida, tente novamente\n")
        else:
            valido = False
    return peças_tiradas

def partida(): #define a partida
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))
    while m < 1:
        print('A quantidade de peças por jogadas devem ser menor ou igual as peças totais')
        m = int(input('Limite de peças por jogada?'))
    
    valor = 0
    jogada = 0
    if (n %(m+1)) == 0:
        print('\nVocê começa!')
        jogada = 1 #vez do usuario
        while n > 0:
            if jogada == 1:
                valor = usuario_escolhe_jogada(n, m)
                print(f'\nVocê tirou {valor} peças no tabuleiro')
                n = n - valor
                print(f'Agora restam {n} peças no tabuleiro')
                jogada = 2
            else:
                valor = computador_escolhe_jogada(n, m)
                print(f'\nO computador tirou {valor} peças no tabuleiro')
                n = n - valor
                print(f'Agora restam {n} peças no tabuleiro')
                jogada = 1
        if jogada == 1:
            print('Fim do jogo! O computador ganhou!\n')
            return 2 #ponto para o computador
        else:
            print('Fim do jogo! Você ganhou!\n')
            return 1 #ponto do usuário
    else: #vez do computador
        print('Computador começa!')
        jogada = 2
        while n > 0:
            if jogada == 2:
                valor = computador_escolhe_jogada(n, m)
                print(f'\nO computador tirou {valor} peças no tabuleiro')
                n = n - valor
                print(f'Agora restam {n} peças no tabuleiro')
                jogada = 1
            else:
                valor = usuario_escolhe_jogada(n, m)
                print(f'\nVocê tirou {valor} peças no tabuleiro')
                n = n - valor
                print(f'Agora restam {n} peças no tabuleiro')
                jogada = 2
        if jogada == 1:
            print('Fim do jogo! O computador ganhou!\n')
            return 2 #ponto para o computador
        else:
            print('Fim do jogo! Você ganhou!\n')
            return 1 #ponto do usuário

def campeonato():
    partidas = 1
    placar_humano = placar_máquina = 0
    while partidas < 4:
        print(f'**** Rodada {partidas} ****\n')
        if partida() == 1:
            placar_humano = placar_humano + 1
        else:
            placar_máquina = placar_máquina + 1
        partidas = partidas + 1

    print('**** Final do campeonato! ****\n')
    print(f'Placar: Você {placar_humano} X {placar_máquina}')
    

def main(): #Opcões iniciais da partida
    print('Bem vindo ao jogo do NIM! Escolha:\n')
    print('1 - Partida individual')
    escolha = int(input('2 - Campeonato\n'))
    while escolha != 1 and escolha != 2:
        print('Favor, escolher uma das duas opções abaixo')
        print('1 - Partida individual')
        escolha = int(input('2 - Campeonato\n'))
    if escolha == 1:
        print('Você escolheu uma partida individual')
        partida()
    else:
        print('Você escolheu um campeonato')
        campeonato()
main()

    