import math

filename = "input_01.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

def total_weight(ini_weight):
    fuel = math.floor(int(ini_weight) / 3) - 2
    if fuel <= 0:
        return ini_weight
    return ini_weight + total_weight(fuel)

total = 0
for weight in content:
    partial = total_weight(int(weight))
    print(partial)
    total += partial - int(weight)

print("total =",total)

print("ejemplo:", total_weight(1969))

#correct answer: 4898585

