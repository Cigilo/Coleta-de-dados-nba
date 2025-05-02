
from os import system as st
from time import sleep
import pandas as pd

import engine
import utils
import engine as escolher_nome

def main():
    
    tabela_final = []
    
    erro = []
    
    links_txt = utils.coletor_links()
    q_links = len(links_txt)
    st('cls')
    utils.menu(q_links)
    
      
    
    for i, link in enumerate(links_txt, 1):
        st('cls')

        print(f"Processando {i}/{q_links}: {link}")
        
        id = utils.pegar_id(link)
        
        lista_nomes_pontos, lista_data_hora,fase = escolher_nome.coletor_nomes_pontos_data_hora(id)
        
        dados_jogo = engine.principal(id, lista_nomes_pontos, lista_data_hora ,fase )
        
        tabela_final.extend(dados_jogo)  

            
            
        
    df_final = pd.DataFrame(tabela_final)
    df_final.to_excel("NBA_Temporada_2024.xlsx", index=False)
    st('cls')
    print(f"Planilha geral gerada: NBA_Temporada_2024.xlsx")

if __name__ == "__main__":
    main()
