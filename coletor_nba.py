import requests as rs
import pandas as pd 
from bs4 import BeautifulSoup as bs
from os import system as st
from time import sleep


def coletor_links():
    
    with open("links.txt", "r") as arquivo:
        links = arquivo.read().splitlines()  


    
    return links
        
        

def pegar_nomes(link):
    
    resposta = rs.get(link)
    sopa = bs(resposta.text, "html.parser")
    vazio = []

    elemento = sopa.find("bdi", class_="Text cPEaJF")

    if elemento:
        jogo = elemento.text.strip().split("-")  

        for i in jogo:
            vazio.append(i.strip())  
    else:
        print("Elemento não encontrado")
    
    return vazio

def pegar_id(link):
    inicio = link.find("id") + 3 
    final = len(link)
    id = link[inicio : final]

    return id 


def principal(id , nomes):
    
    api = f'https://www.sofascore.com/api/v1/event/{id}/statistics'
    
    headers = {
        
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        
    }
    
    response = rs.get(api , headers= headers)
    
    if response.status_code == 200 :
        data = response.json()
        
        all_data = []
        
        for match_stat in data['statistics']:
            period = match_stat['period']
            
            for group in match_stat['groups']:
                group_name = group['groupName']
                
                for item in group['statisticsItems']:
                    stat_name = item.get('name')
                    stat_home = item.get('home')
                    stat_away = item.get('away')
                    
                    all_data.append({
                        
                        'Periodo' : period , 
                        'Tipos' : group_name , 
                        'Lances' : stat_name , 
                        f'Time da casa : {nomes[0]}' : stat_home ,
                        f'Time visitante : {nomes[1]}' : stat_away ,
                        
                    })
        
        df = pd.DataFrame(all_data)
        
        excel_file = f"{nomes[0]} X {nomes[1]} .xlsx"
        
        df.to_excel(excel_file, index = False)
        
    




def main():
    links = coletor_links()
    n_tb = len(links) + 1
    print(f'Serão {n_tb - 1} tabelas')
    
    for link in links :
        id = pegar_id(link)
        nomes = pegar_nomes(link)
        principal(id , nomes)
        n_tb = n_tb - 1
        st('cls')
        print(f"Tabela numero ({n_tb}) concluida")
    
    
    
    

if __name__ == "__main__":
    main()