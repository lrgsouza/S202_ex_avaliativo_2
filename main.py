
from crud import *

def print_results(list_r):
    for r in list_r:
        if r[1] == None:
            print(f'  - {r[0]}')
        else:
            print(f'  - {r[1]}')

if __name__ == '__main__':

    famila = FamiliaDB()

    # respondendo as perguntas

    # quem da familia é aposentado
    print(f'Aposentados da familia:')
    print_results(famila.get_aposentado())

    # quem da familia é estudante
    print(f'Estudantes da familia:')
    print_results(famila.get_estudantes())

    # quem da familia é falecido
    print(f'Falecidos da familia:')
    print_results(famila.get_falecidos())

    # quem da familia é trabalhador
    print(f'Trabalhadores da familia:')
    print_results(famila.get_trabalhador())

    # quais os animais de estimação do "fulano"
    fulano = 'Lucas Ribeiro'
    print(f'São Pets de {fulano}:')
    print_results(famila.get_pets(fulano))

    # quais os filhos do fulano
    fulano = 'João Filho'
    print(f'São filhos de {fulano}:')
    print_results(famila.get_sons(fulano))

    # quais os avós do fulano
    fulano = 'Lucas Ribeiro'
    print(f'São avós de {fulano}:')
    print_results(famila.get_AVOS(fulano))

    #fulano é casado a quanto tempo
    fulano = 'Lucas Ribeiro'
    conjuge = famila.get_casado(fulano)[0][0]
    print(f'{fulano} é casado a quanto tempo com {conjuge}')
    print_results(famila.get_casado(fulano))




