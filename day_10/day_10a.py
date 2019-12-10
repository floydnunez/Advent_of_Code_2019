debug = False

filename = "input_10.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

asteroids = []

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "[" + str(self.x) +" "+ str(self.y) + "]"
    def __repr__(self):
        return self.__str__()

yy = 0
for row in content:
    for xx, char in enumerate(row):
        if char == '#':
            asteroids.append(Point(xx, yy))
    yy += 1

print(asteroids)

#now, per asteroid, draw a line to _every_ other asteroid
lines_from_asteroid = {}
for aster1 in asteroids:
    list_of_lines = []
    for aster2 in asteroids:
        if aster1 != aster2:
            list_of_lines.append([aster1, aster2])
    lines_from_asteroid[aster1] = list_of_lines

print(len(lines_from_asteroid))
#print(lines_from_asteroid)

def isBetween(a, b, c):
    crossproduct = (c.y - a.y) * (b.x - a.x) - (c.x - a.x) * (b.y - a.y)
    epsilon = 0.00001
    # compare versus epsilon for floating point values, or != 0 if using integers
    if abs(crossproduct) > epsilon:
        return False

    dotproduct = (c.x - a.x) * (b.x - a.x) + (c.y - a.y)*(b.y - a.y)
    if dotproduct < 0:
        return False

    squaredlengthba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
    if dotproduct > squaredlengthba:
        return False

    return True

visible_asteroids = {}
max_total = 0
max_asteroid = None
#check intersections for every line and other asteroid
for start, lines in lines_from_asteroid.items():
    print("processing:", start)
    total = 0
    for cc in asteroids:
        if start != cc:
            does_cc_not_collide = True
            for line in lines:
                aa = line[0]
                bb = line[1]
                if aa != cc and bb != cc:
                    if isBetween(aa, bb, cc):
                        if debug: print(cc, "is between", aa, bb)
                        does_cc_not_collide = False
                    else:
                        if debug: print(cc, "DOES NOT INTERSECT", aa, bb)
            if does_cc_not_collide:
                total += 1
    visible_asteroids[start] = total
    if total > max_total:
        max_total = total
        max_asteroid = start
#print(visible_asteroids)
print("max visibles:", max_total, "from", max_asteroid)

#answer 314 from [27 19]

