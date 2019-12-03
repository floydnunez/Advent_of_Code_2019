import math

filename = "day_01/input_01.txt"

with open(filename) as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

total_weight = 0
total = 0
for weight in content:
    total_weight += weight
    fuel = math.floor(int(weight) / 3) - 2
    print(fuel)
    total += fuel

print("total =",total)
print("total weight =", total_weight)
print("fuel approx = ", total_weight/2)

#correct answer: 3267638
