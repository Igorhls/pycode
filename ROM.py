import matplotlib.pyplot as plt
import numpy as np

# Dados das peneiras
peneiras = ["3/4\"", "1/2\"", "3/8\"", "#4", "#8", "#14", "#32", "#48", "#100", "Fundo"]
aberturas_mm = [19.0, 12.5, 9.5, 4.75, 2.36, 1.18, 0.6, 0.3, 0.15, 0.075]  # mm
peso_retido_g = [0, 0, 0, 0, 1.8, 47, 358, 42, 32, 480]

# Cálculo do total de amostra
peso_total = sum(peso_retido_g)

# Cálculo do % retido e % passante acumulado
percentual_retido = [(peso / peso_total) * 100 for peso in peso_retido_g]
percentual_passante = [100 - sum(percentual_retido[:i+1]) for i in range(len(percentual_retido))]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(aberturas_mm, percentual_passante, marker='o', linestyle='-', color='blue', label='% Passante Acumulado')
plt.xscale('log')
plt.gca().invert_xaxis()
plt.xlabel('Abertura da Peneira (mm) - Escala Logarítmica')
plt.ylabel('% Passante Acumulado')
plt.title('Curva Granulométrica da Amostra')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()