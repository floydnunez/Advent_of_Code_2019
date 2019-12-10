import math

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
    def __hash__(self):
        return self.x * 100 + self.y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

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

def calc_angle(a, b):
    dx = a.x - b.x
    dy = a.y - b.y
    angle = math.degrees(math.atan2(dy, dx)) - 90
    if (angle < 0):
        angle += 360
    #round a little
#    angle = math.floor(angle * 10000) / 10000
#    print("for ", b, "=", angle)
    return angle

def calc_distance(a, b):
    squaredlengthba = (b.x - a.x)*(b.x - a.x) + (b.y - a.y)*(b.y - a.y)
    return squaredlengthba

win_point = Point(27, 19) #winner from last time

list_dist = []
list_asteroids = []

for line in lines_from_asteroid[win_point]:
    dist = calc_distance(line[0], line[1])
    list_dist.append(dist)
    list_asteroids.append(line[1])

asteroids_by_distance = [x for _,x in sorted(zip(list_dist, list_asteroids), key=lambda pair: pair[0])]

#print(asteroids_by_distance)

list_angles = []

for aster in asteroids_by_distance:
    angle = calc_angle(win_point, aster)
    list_angles.append(angle)
#print(list_angles)

asteroids_by_angle = [x for _,x in sorted(zip(list_angles, asteroids_by_distance), key=lambda pair: pair[0])]

print(asteroids_by_angle)

