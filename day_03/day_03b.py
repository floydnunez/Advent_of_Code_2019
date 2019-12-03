import math

filename = "input_03.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

data1 = content[0].split(",")
data2 = content[1].split(",")

wire1 = []
wire2 = []

def walk_wire(data, wire):
    ini = [0,0]
    last = ini.copy()
    for elem in data:
        direction = elem[0:1]
        length = int(elem[1:])
        if direction == 'R':
            for index in range(0, length):
                last = last.copy()
                last[1] += 1
                wire.append(last)
        if direction == 'L':
            for index in range(0, length):
                last = last.copy()
                last[1] -= 1
                wire.append(last)
        if direction == 'U':
            for index in range(0, length):
                last = last.copy()
                last[0] += 1
                wire.append(last)
        if direction == 'D':
            for index in range(0, length):
                last = last.copy()
                last[0] -= 1
                wire.append(last)

walk_wire(data1, wire1)
walk_wire(data2, wire2)

cross = []

print("len wire1:", len(wire1))
print("len wire2:", len(wire2))

chain1 = []
chain2 = []

for elem in wire1:
    chain1.append(str(elem[0]) + "_" + str(elem[1]))
for elem in wire2:
    chain2.append(str(elem[0]) + "_" + str(elem[1]))

set1 = set(chain1)
set2 = set(chain2)

cross = set1.intersection(set2)

print("cross:",len(cross))

intersections = []
minimum = 99999999999999
for elem in cross:
    parts = elem.split("_")
    manhattan = abs(int(parts[0])) + abs(int(parts[1]))
    intersections.append([int(parts[0]), int(parts[1])])
    if minimum > manhattan:
        minimum = manhattan

print("minimum: ", minimum)

minimum = 99999999999999
for elem in intersections:
    steps1 = wire1.index(elem) + 1 #+1 due to obiwan
    steps2 = wire2.index(elem) + 1
    total = steps1 + steps2
    if total < minimum:
        minimum = total

print("minimum b:", minimum)
#answer: 15612
