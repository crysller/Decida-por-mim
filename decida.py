from random import randrange
from time import sleep
lista = ['Sim', 
        'Não', 
        'Certeza? Pense direito antes', 
        'Ok', 
        'Melhor começar agora',
        'Vai na fé',
        'Eu confio',
        'Deixa para amanhã',
        'To ocupado, sai fora',
        'Já devia ta fazendo']

def linha():
    print('=~'*20)


continuar = 'Ss'
while continuar in 'Ss':
    escolha = randrange(0, 11)
    linha()
    print('\033[0;32mManda uma pergunta ae!')
    str(input('Pergunta: '))
    linha()
    sleep(0.5)
    print(f'\033[1;34mResposta: {lista[escolha]}.')
    linha()
    continuar = input('Deseja continar? S ou N?')
linha()
print('Até outra hora! o/')