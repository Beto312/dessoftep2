def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes
def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota
def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else: 
        tabuleiro[linha][coluna] = "-"
    return tabuleiro
def posiciona_frota (frota):
    # montar um tabuleiro vazio
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    # montar todas as linhas
    # posicionar os navios no lugar    for chave, valor in frota.items():
    for chave, valor in frota.items():
        for i in range(len(valor)):
            for j in range(len(valor[i])):
                x = valor[i][j][0]
                y = valor[i][j][1] 

                tabuleiro[x][y] = 1
    return tabuleiro