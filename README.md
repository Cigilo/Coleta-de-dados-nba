# 📊 Coleta de Dados da NBA

Este repositório contém um projeto de **coleta e análise de dados de partidas da NBA**, focado em estatísticas detalhadas dos jogos da temporada regular e playoffs.

---

## 📌 Integrantes do Projeto

- VINICIUS FERRAZ DO NASCIMENTO  
- JOÃO PEDRO DE OLIVEIRA RIBAS  
- SAMUEL VICTOR FERNANDES DANTAS VICENTE  

---

## 🎯 Objetivo do Projeto

O objetivo é **coletar eventos importantes** que ocorrem em partidas da NBA, como cestas, assistências, faltas, entre outros, permitindo entender melhor o desempenho das equipes e encontrar padrões para previsões futuras.

---

## 📊 Estrutura dos Dados

As informações extraídas para cada partida incluem:

- **Data e Hora**
- **Mês e Fase** (Temporada Regular ou Playoffs)
- **Times** (Casa e Visitante)
- **Resultado** (Vitória Casa/Visitante/Empate)
- **Período** (Quartos e Overtime)
- **Categoria** (Scoring, Others, Lead)
- **Tipo de Lance** (Assistências, 2 Pontos, 3 Pontos, etc.)
- **Estatísticas Detalhadas** (Tentativas, acertos, porcentagens)

---

### 🕒 Período

Define o momento da partida a que os dados se referem.

Exemplos:  
`ALL` (jogo completo), `1Q` (primeiro quarto), `OT1` (primeira prorrogação).

---

### 🏀 Categoria ("Tipos")

Classifica as jogadas.

Exemplos:  
`Scoring`, `Others`, `Lead`.

---

### 🎯 Lances (Eventos)

Eventos específicos como:

Exemplos:  
`Assists`, `2 pointers`, `3 pointers`, `Blocks`, etc.

---

### 🏠 Time da Casa

Estatísticas de arremessos e aproveitamento.

Exemplos:  
`4/6 (66%)`, `27/51 (52%)`.

---

### ✈️ Time Visitante

Estatísticas semelhantes ao time da casa.

Exemplos:  
`16/17 (94%)`, `23/38 (60%)`.

---

## 🔄 Processo de Coleta dos Dados

### 1️⃣ Coleta de Links

O sistema lê o arquivo `links.txt` que contém URLs das partidas na Sofascore.

### 2️⃣ Extração de Informações Básicas

De cada URL, o sistema extrai:

- Nome dos times
- Data e Hora
- ID do Jogo

### 3️⃣ Coleta dos Dados via API + Selenium

- Utilizamos a API oficial da Sofascore (`/event/{id}` e `/event/{id}/statistics`).
- A coleta de estatísticas é feita extraindo o conteúdo `raw_json` usando Selenium para simular uma requisição humana.

### 4️⃣ Cálculo Inteligente do "Score" por Período

- O placar dos **overtimes (OT)** é calculado manualmente somando:
  - Pontos de Free Throws (cada acerto = 1 ponto)
  - Pontos de 2 Pointers (cada acerto = 2 pontos)
  - Pontos de 3 Pointers (cada acerto = 3 pontos)
- Garante que o Score seja exato mesmo quando não informado diretamente.

### 5️⃣ Organização e Salvamento

- Dados organizados em **DataFrames** (`pandas`) e exportados para arquivos `.xlsx`.
- Cada linha representa um evento específico (ex: 2PT convertidos no 3º quarto).

### 6️⃣ Execução Final

- O script processa todos os jogos automaticamente.
- Exibe mensagens de progresso e salva as tabelas prontas.

---

## 📅 Atualizações

Os dados serão coletados e atualizados regularmente para refletir novos jogos e eventos.

Link para acompanhamento de arquivos:  
📁 [Google Drive do Projeto](https://drive.google.com/drive/u/0/folders/18mdXnj1M1j0o1QACMp34M_SenbCSwUt8)

---

## 🔗 Tecnologias Utilizadas

- Python 🐍
- Pandas
- Selenium
- Requests
- BeautifulSoup

---

