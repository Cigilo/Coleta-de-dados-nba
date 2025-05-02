from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
import json
import pandas as pd
from os import system as st
import datetime
    
def iniciar_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    
    return webdriver.Chrome(options=options)

################################################
################################################
################################################
################################################

def extract_team_stats(data, team_key: str, score_key: str):
    team_info = {
        'name': data.get('event', {}).get(team_key, {}).get('name', ''),
        'ALL': data.get('event', {}).get(score_key, {}).get('current', ''),
    }
    
    # Extrair os períodos que realmente existem
    score_info = data.get('event', {}).get(score_key, {})
    for key, value in score_info.items():
        if key.startswith('period') and value is not None:
            # Exemplo: 'period1' vira '1Q'
            period_number = key.replace('period', '')
            team_info[f'{period_number}Q'] = value
        elif key.startswith('overtime') and value is not None:
            # Exemplo: 'overtime1' vira 'OT1'
            overtime_number = key.replace('overtime', '')
            team_info[f'OT{overtime_number}'] = value

    return team_info


def coletor_nomes_pontos_data_hora(id):
    
    # ===========| variaveis | ========== #
    
    fase = []
    data_hora = []
    times = []
    api_url = f"https://www.sofascore.com/api/v1/event/{id}"
    
    # ===========| padrao | ========== #
    
    driver = iniciar_driver()
    driver.get(api_url)
    sleep(1)
    
        # Extrai o JSON que está dentro da tag <pre>
        
    pre = driver.find_element("tag name", "pre")
    raw_json = pre.text
    driver.quit()
    
    
    # ===========| CODIGO | ========== #
    
    data = json.loads(raw_json)
    
    for team, score in [('homeTeam', 'homeScore'), ('awayTeam', 'awayScore')]:
        times.append(extract_team_stats(data,team, score))
        
    timestamp = data['event']['startTimestamp']

    data_jogo = datetime.datetime.fromtimestamp(timestamp)

    data_formatada = data_jogo.strftime('%d/%m/%Y')
    hora_formatada = data_jogo.strftime('%H:%M')
    
    data_hora.append(data_formatada)
    data_hora.append(hora_formatada)
    
    
    fase2 = data.get('event',{}).get('seasonStatisticsType','')
    fase.append(fase2)
    fase2 = data.get('event', {}).get('roundInfo',{}).get('name','')
    fase.append(fase2)
    
    
    
    

    return times , data_hora, fase
    

################################################
################################################
################################################
################################################
    
def principal(id, lista_nomes_pontos, lista_data_hora, fase):
    import re
    
    # ===========| variaveis | ========== #
    time_casa = lista_nomes_pontos[0]['name']
    time_visitante = lista_nomes_pontos[1]['name']
    
    placar_casa = lista_nomes_pontos[0]['ALL']
    placar_visitante = lista_nomes_pontos[1]['ALL']
    
    data_bruta = lista_data_hora[0]
    mes = data_bruta.split('/')[1]
    
    meses_nome = {
        '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril',
        '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto',
        '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'
    }
    
    all_data = []
    
    api_url = f"https://www.sofascore.com/api/v1/event/{id}/statistics"
    
    # ===========| padrao | ========== #
    driver = iniciar_driver()
    driver.get(api_url)
    sleep(2)
    
    pre = driver.find_element("tag name", "pre")
    raw_json = pre.text
    driver.quit()
    
    # ===========| CODIGO | ========== #
    data = json.loads(raw_json)

    nome_mes = meses_nome.get(mes, 'Mês desconhecido')
    
    if placar_casa > placar_visitante:
        resultado = 'Vitória Casa'
    elif placar_casa < placar_visitante:
        resultado = 'Vitória Visitante'
    else:
        resultado = 'Empate'

    for match_stat in data.get('statistics', []):
        period = match_stat.get('period', '')

        # Inicializa as variáveis
        free_throws_home = two_pointers_home = three_pointers_home = 0
        free_throws_away = two_pointers_away = three_pointers_away = 0

        for group in match_stat.get('groups', []):
            group_name = group.get('groupName', '')
            for item in group.get('statisticsItems', []):
                item_name = item.get('name', '')
                
                # Pega os acertos (número antes da barra)
                if item_name == 'Free throws':
                    home = item.get('home', '0/0')
                    away = item.get('away', '0/0')
                    free_throws_home = int(re.search(r'(\d+)/', home).group(1)) if re.search(r'(\d+)/', home) else 0
                    free_throws_away = int(re.search(r'(\d+)/', away).group(1)) if re.search(r'(\d+)/', away) else 0

                if item_name == '2 pointers':
                    home = item.get('home', '0/0')
                    away = item.get('away', '0/0')
                    two_pointers_home = int(re.search(r'(\d+)/', home).group(1)) if re.search(r'(\d+)/', home) else 0
                    two_pointers_away = int(re.search(r'(\d+)/', away).group(1)) if re.search(r'(\d+)/', away) else 0

                if item_name == '3 pointers':
                    home = item.get('home', '0/0')
                    away = item.get('away', '0/0')
                    three_pointers_home = int(re.search(r'(\d+)/', home).group(1)) if re.search(r'(\d+)/', home) else 0
                    three_pointers_away = int(re.search(r'(\d+)/', away).group(1)) if re.search(r'(\d+)/', away) else 0
        
        # Faz o cálculo correto
        score_home = (free_throws_home * 1) + (two_pointers_home * 2) + (three_pointers_home * 3)
        score_away = (free_throws_away * 1) + (two_pointers_away * 2) + (three_pointers_away * 3)

        # Primeiro append (Score)
        all_data.append({
            'Data': lista_data_hora[0],
            'Hora': lista_data_hora[1],
            'Mês': nome_mes,
            'Tipo fase': fase[0],
            'Fase': fase[1],
            'Time Casa': time_casa,
            'Time Visitante': time_visitante,
            'Resultado': resultado,
            'Periodo': period,
            'Categoria': 'Scoring',
            'Lance': 'Score',
            'Dados da Casa': score_home,
            'Dados do Visitante': score_away,
        })

        # Agora append dos outros lances
        for group in match_stat.get('groups', []):
            group_name = group.get('groupName', '')
            for item in group.get('statisticsItems', []):
                all_data.append({
                    'Data': lista_data_hora[0],
                    'Hora': lista_data_hora[1],
                    'Mês': nome_mes,
                    'Tipo fase': fase[0],
                    'Fase': fase[1],
                    'Time Casa': time_casa,
                    'Time Visitante': time_visitante,
                    'Resultado': resultado,
                    'Periodo': period,
                    'Categoria': group_name,
                    'Lance': item.get('name', ''),
                    'Dados da Casa': item.get('home', ''),
                    'Dados do Visitante': item.get('away', ''),
                })

    return all_data



    