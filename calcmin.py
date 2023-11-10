# Função para converter uma string em uma lista de números float
def convert_to_float_list(string):
    numbers = [float(part.replace(',', '.')) for part in string.split('+')]
    return numbers

# Ler os números do arquivo
with open('media.txt', 'r') as f:
    lines = f.readlines()

data = []
for line in lines:
    numbers = convert_to_float_list(line.strip())
    data.extend(numbers)

# Calcular a média
average = sum(data) / len(data)

# Calcular o valor mínimo
minimum = min(data)

print("A média é:", average)
print("O valor mínimo é:", minimum)
