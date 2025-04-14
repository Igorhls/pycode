import matplotlib.pyplot as plt
import numpy as np

# Dados das amostras
parametros = ['Cloro Residual', 'Condutividade Elétrica', 'Turbidez', 'pH', 'DBO₅']
amostra_1 = [0.05, 1395.00, 56.545, 6.49, 36.00]  # Valores para Amostra 1
amostra_2 = [0.05, 1420.00, 52.300, 6.55, 38.20]  # Valores para Amostra 2
unidades = ['mg/L Cl₂', 'µS/cm', 'NTU', 'ND', 'mg/L O₂']  # Unidades de medição

# Definindo a largura das barras
largura = 0.3  # Largura das barras

# Para cada parâmetro, vamos criar um gráfico de colunas separado
for i, parametro in enumerate(parametros):
    # Definindo a posição das barras no eixo X
    posicoes = np.arange(2)  # Duas barras (uma para cada amostra)
    
    # Criando o gráfico de colunas
    plt.figure(figsize=(8, 6))

    # Plotando a coluna para a Amostra 1 (vermelho)
    plt.bar(posicoes[0] - largura/2, amostra_1[i], largura, color='red', label=f'Amostra 1: {amostra_1[i]} {unidades[i]}')

    # Plotando a coluna para a Amostra 2 (verde claro)
    plt.bar(posicoes[1] + largura/2, amostra_2[i], largura, color='lightgreen', label=f'Amostra 2: {amostra_2[i]} {unidades[i]}')

    # Configurando o gráfico
    plt.title(f'Comparação de {parametro}')
    plt.xlabel(f'{parametro} ({unidades[i]})')
    plt.ylabel('Valor')
    plt.xticks(posicoes, ['Amostra 1', 'Amostra 2'])
    plt.legend()

    # Exibindo o gráfico
    plt.tight_layout()
    plt.show()
