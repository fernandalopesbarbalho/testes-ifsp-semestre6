def converte(numeroEmRomano):

    tabela = {}
    tabela['I'] = 1
    tabela['V'] = 5
    tabela['X'] = 10
    tabela['L'] = 50
    tabela['C'] = 100
    tabela['D'] = 500
    tabela['M'] = 1000

    acumulador = 0
    ultimovizinhodireita = 0
    for i in reversed(range(len(numeroEmRomano))):
        numCorrente = numeroEmRomano[i]
        atual = tabela.get(numCorrente, 0)
        
        if atual < ultimovizinhodireita:
            acumulador -= atual
        else:
            acumulador += atual

        ultimovizinhodireita = atual

    return acumulador