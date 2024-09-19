import csv
import math
import matplotlib.pyplot as plt

# Exibe uma mensagem de boas-vindas ao usuario
print('*' * 60)
print('* SEJA BEM-VINDO A MEGA CALCULADORA DA FORMULA E EM PYTHON *')
print('*' * 60)


# Funcao para validar a entrada do usuario
def validar_input(tipo, mensagem):
    while True:
        entrada = input(mensagem)
        if tipo == 'nome':
            if entrada.strip() == '':
                print("O nome nao pode ser vazio. Por favor, tente novamente.")
            else:
                return entrada
        elif tipo == 'numero':
            try:
                valor = float(entrada)
                if valor == 0:
                    print("O numero nao pode ser zero. Por favor, tente novamente.")
                else:
                    return valor
            except ValueError:
                print("Entrada invalida. Por favor, digite um numero.")


# Funcao para exibir o menu de opcoes
def exibir_menu():
    while True:
        try:
            print('1 - Calcular o tempo medio das voltas dos pilotos')
            print('2 - Calcular a velocidade media do piloto em cada volta')
            print('3 - Exibir grafico de desempenho')
            print('4 - Sair')
            opcao = int(input('Digite a opcao desejada: '))


            match opcao:
                case 1:
                    print('----- Calculadora de Tempo Medio do Corredor -----')
                    calc_media_tempo_corredor()
                case 2:
                    print('2 - Calcular a velocidade media do piloto em cada volta')
                    calc_velocidade_media()
                case 3:
                    exibir_grafico_desempenho()
                case 4:
                    print('Saindo do programa...')
                    break
                case _:
                    print('Opcao indisponivel! Digite uma opcao valida: ')
        except ValueError:
            print('Opcao invalida! Por favor, digite um numero.')


# Funcao para salvar dados em um arquivo CSV
def salvar_csv(dados, nome_arquivo):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        for piloto, valores in dados.items():
            escritor.writerow([piloto] + valores)
    print(f"Dados salvos em {nome_arquivo}")


# Funcao para calcular a media de tempo das voltas dos corredores e salvar em um CSV
def calc_media_tempo_corredor():
    corredores_dict = {}
    numero_voltas = int(validar_input('numero', 'Digite o numero de voltas da corrida: '))
    while True:
        nome_corredor = validar_input('nome', 'Nome do Corredor: ')
        tempos_voltas = []
        for i in range(numero_voltas):
            tempo_volta = validar_input('numero', f'Digite o tempo da {i + 1}ª volta (em segundos): ')
            tempos_voltas.append(tempo_volta)

        media_tempo = sum(tempos_voltas) / numero_voltas
        corredores_dict[nome_corredor] = [media_tempo]  # Adiciona o tempo medio ao dicionario
        continuar = input('Deseja adicionar outro corredor? (s/n): ').strip().lower()
        if continuar != 's':
            break

    salvar_csv(corredores_dict, 'tempos_medios_corredores.csv')

    voltar_ao_menu()


# Funcao para calcular a velocidade media dos corredores e salvar em um CSV
def calc_velocidade_media():
    corredores_dict = {}
    numero_voltas = int(validar_input('numero', 'Digite o numero de voltas: '))
    dist_pista = int(validar_input('numero', 'Digite a distancia da pista (em metros): '))

    while True:
        nome_corredor = validar_input('nome', 'Nome do Corredor: ')
        velocidades_voltas = []
        for i in range(numero_voltas):
            volta = i + 1
            tempo_volta = validar_input('numero', f'Digite o tempo da {volta}ª volta (em segundos): ')
            velocidade_media = dist_pista / tempo_volta
            velocidade_media_convertida = velocidade_media * 3.6  # Convertendo de m/s para km/h
            velocidades_voltas.append(velocidade_media_convertida)

        velocidade_media_total = sum(velocidades_voltas) / numero_voltas
        corredores_dict[nome_corredor] = [velocidade_media_total]  # Adiciona a velocidade media ao dicionario

        continuar = input('Deseja adicionar outro corredor? (s/n): ').strip().lower()
        if continuar != 's':
            break

    salvar_csv(corredores_dict, 'velocidades_medias.csv')

    voltar_ao_menu()


# Funcao para exibir graficos de desempenho dos pilotos
def exibir_grafico_desempenho():
    corredores = []
    tempos = []

    # Lendo dados do arquivo CSV
    with open('tempos_medios_corredores.csv', newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            corredores.append(linha[0])
            tempos.append(float(linha[1]))

    # Criando grafico com matplotlib
    plt.bar(corredores, tempos, color='blue')
    plt.xlabel('Corredores')
    plt.ylabel('Tempo Medio (s)')
    plt.title('Desempenho dos Pilotos - Tempo Medio')
    plt.show()

    voltar_ao_menu()


# Funcao para voltar ao menu principal
def voltar_ao_menu():
    opcao = input('Deseja voltar ao menu principal? (s/n): ').strip().lower()
    if opcao == 's':
        exibir_menu()
    else:
        print('Saindo do programa...')


# Inicializa o programa exibindo o menu principal
exibir_menu()