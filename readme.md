A Mega Calculadora da Fórmula E em Python é uma aplicação interativa que permite calcular diferentes métricas relacionadas a corridas de Fórmula E. Esta ferramenta é ideal para aficionados por corridas que desejam analisar o desempenho dos pilotos em termos de tempo médio das voltas, velocidade média por volta e número total de voltas de uma pista.

Funcionalidades
Calcular o tempo médio das voltas dos pilotos: Insira o número de voltas e o tempo de cada volta para obter o tempo médio de cada corror em ordem crescente.
Calcular a velocidade média do piloto em cada volta: Insira o número de voltas e a distância da pista para calcular a velocidade média em km/h de cada corredor em ordem decrescente.
Calcular o número de voltas de uma pista: Insira a distância total da corrida e o comprimento da pista para calcular o número total de voltas, incluindo a última volta parcial, se aplicável.
Retornar ao menu principal: Após a execução de qualquer funcionalidade, o usuário pode optar por voltar ao menu principal ou sair do programa.
Observações
O programa valida todas as entradas do usuário, assegurando que nomes não sejam vazios e números não sejam zero.
As entradas numéricas são convertidas para float, e qualquer valor inválido é rejeitado com uma mensagem de erro.
Após cada cálculo, o usuário é perguntado se deseja retornar ao menu principal.


Colaboradores
Felipe Nascimento - RM: 554598
Henrique Ignacio - RM: 555274
Gustavo Martins - RM: 556956


Tecnologias Utilizadas
Python: Linguagem de programação principal usada para desenvolver a aplicação.
PEP8: Guia de estilo para Python, seguido para assegurar a legibilidade e manutenção do código.
Biblioteca Padrão math: Utilizada para funções matemáticas avançadas.
Biblioteca csv: Os dados de tempo médio e velocidade média são salvos.
Biblioteca matplotlib: Adicionamos uma função para criar gráficos de barras (bar plot) que mostram o desempenho dos corredores.
    Esse gráfico é gerado usando os dados salvos no arquivo CSV e visualizado diretamente na interface.