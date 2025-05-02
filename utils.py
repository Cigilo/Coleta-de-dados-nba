def coletor_links():
    with open("links.txt", "r") as arquivo:
        return arquivo.read().splitlines()


def pegar_id(link):    
    indice = link.find('id:')
    id = link[indice+3:]
    
    return id 


def menu(q_links):
    print('<==========| Quantidade de links|==========>\n')
    print(f'\t\tSerão processados {q_links} jogos\n')
    print('<==========================================>')
    input("\n\nAPERTE QUALQUER TECLA PARA CONTINUAR: ")


