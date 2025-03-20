Coleta de Dados da NBA

Este repositório contém um projeto de análise de dados da NBA, focado na coleta e processamento de estatísticas dos jogos da temporada regular.

📌 Integrantes do Projeto

VINICIUS FERRAZ DO NASCIMENTO

JOÃO PEDRO DE OLIVEIRA RIBAS

SAMUEL VICTOR FERNANDES DANTAS VICENTE

🎯 Objetivo do Projeto

O objetivo deste projeto é coletar e analisar eventos importantes que ocorrem em um jogo de basquete da NBA. A partir dos dados, é possível entender melhor o desempenho das equipes ao longo da partida e prever padrões para futuros jogos.

📊 Estrutura dos Dados

Os dados coletados incluem diversas informações sobre cada jogo, permitindo uma análise aprofundada das estatísticas de cada equipe.

🕒 Período

Define o momento da partida a que os dados se referem. Pode representar o jogo inteiro ou um quarto específico.

Exemplos: ALL (Jogo todo), 1Q (Primeiro quarto), 2Q (Segundo quarto), etc.

🏀 Tipos

Categoria que facilita a interpretação das jogadas registradas. As jogadas podem estar relacionadas a pontos, eventos diversos ou liderança no jogo.

Exemplos: Scoring, Others, Lead.

🎯 Lances

Especificação dos eventos do jogo, como assistências, cestas e bloqueios.

Exemplos: Assistences, 2 pointers, 3 pointers, Blocks.

🏠 Time da Casa

Refere-se ao time que joga em casa na partida. Apresenta estatísticas detalhadas do desempenho, incluindo tentativas e acertos de arremessos, além de porcentagens de conversão.

Exemplos: 4/6 (66%), 27/51 (52%).

✈️ Time Visitante

Refere-se ao time que joga fora de casa na partida. Assim como o time da casa, exibe estatísticas detalhadas de arremessos e aproveitamento.

Exemplos: 16/17 (94%), 23/38 (60%).

🔄 Processo de Coleta dos Dados

1️⃣ Coleta de Links

O script lê um arquivo chamado links.txt e coleta uma lista de links, que são URLs de partidas da NBA. Esses links serão usados para acessar as páginas com os dados do jogo.

2️⃣ Extração de Detalhes

A partir de cada URL, o script obtém os nomes dos times envolvidos na partida e a data do jogo.

3️⃣ ID da Partida

O identificador exclusivo de cada partida é extraído diretamente da URL.

4️⃣ Coleta de Estatísticas

Uma requisição é feita para uma API que retorna estatísticas detalhadas da partida, incluindo eventos como assistências, bloqueios e arremessos convertidos.

5️⃣ Organização e Salvamento

Os dados coletados são armazenados em um DataFrame do Pandas e salvos em um arquivo Excel (.xlsx), estruturando as informações por período, tipo de jogada e times.

6️⃣ Execução Final

O sistema processa todas as partidas automaticamente, limpando a tela e informando a conclusão de cada tabela gerada.

🚀 Como Contribuir

Se você deseja contribuir com o projeto, pode abrir um pull request ou uma issue com sugestões, melhorias ou correções.

📅 Atualizações

Os dados serão coletados e atualizados regularmente para garantir informações sempre atualizadas sobre os jogos da NBA.

🔗 Tecnologias Utilizadas: Python, Pandas, Requests, BeautifulSoup

📌 Licença: MIT License

