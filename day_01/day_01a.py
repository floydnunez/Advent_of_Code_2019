import math

filename = "input_01.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

total = 0
for weight in content:
    fuel = math.floor(int(weight) / 3) - 2
    print(fuel)
    total += fuel

print("total =",total)

#correct answer: 3267638