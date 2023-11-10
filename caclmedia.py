def convert_to_float_list(string):
    numbers = [float(part.replace(',', '.')) for part in string.split('+')]
    return numbers

with open('media.txt', 'r') as f:
    lines = f.readlines()

data = []
for line in lines:
    numbers = convert_to_float_list(line.strip())
    data.extend(numbers)

average = sum(data) / len(data)

print("A soma é:", sum(data))
print("A média é:", average)