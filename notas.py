# programa de notas
def notas(*n , show=False):
    """
    -> Função que analisa notas e mostra sua situação com base na média dos valores!
    :param n: valores das notas do aluno.
    :param show: mostra a situação ou não.
    """
    comp = len(n)
    print(f'Total: {comp}')
    soma = sum(n)
    print(f'Soma: {soma}')
    media = sum(n)/len(n)
    print(f'Média: {media}')
    if show:
        if media == 6:
            print('\033[1;33mSituação: RAZÓAVEL')
        elif media < 6:
            print('\033[1;31mSituação: PÉSSIMA!')
        else:
            print('\033[1;32mSituação: ÓTIMA, PARABÉNS :)')




# programa principal
notas(9.3,9,8.2,8.1, show=True)