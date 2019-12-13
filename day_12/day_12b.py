import copy

class Coord:
    def __init__(self, posx, speedx, posy, speedy, posz, speedz, posw, speedw):
        self.posx = posx
        self.speedx = speedx
        self.posy = posy
        self.speedy = speedy
        self.posz = posz
        self.speedz = speedz
        self.posw = posw
        self.speedw = speedw

    def __hash__(self):
        return 10000 * (self.posx + self.speedx) + 100 * (self.posy + self.speedy) + \
               10 * (self.posz + self.speedz) + (self.posw + self.speedw)

    def __eq__(self, other):
        return self.posx == other.posx and self.speedx == other.speedx and \
               self.posy == other.posy and self.speedy == other.speedy and \
               self.posz == other.posz and self.speedz == other.speedz and \
               self.posw == other.posw and self.speedw == other.speedw

class Moons:
    def __init__(self, list_planets):
        self.planets = list_planets

    def __hash__(self):
        hashval = 0
        for elem in self.planets:
            hashval += elem.energy()
        return hashval

    def __eq__(self, other):
        all_equals = True
        for index, elem in enumerate(self.planets):
            if elem != other.planets[index]:
                all_equals = False
                break
        return all_equals


class Planet:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

        self.vx = 0
        self.vy = 0
        self.vz = 0

    def __str__(self):
        return "[{:>4} {:>4} {:>4}    v {:>4} {:>4} {:>4}]".format(self.x, self.y, self.z, self.vx, self.vy, self.vz)

    def __repr__(self):
        return self.__str__()

    def __copy__(self):
        new_planet = Planet(self.x, self.y, self.z)
        new_planet.vx = self.vx
        new_planet.vy = self.vy
        new_planet.vz = self.vz
        return new_planet

    def energy(self):
        pot = abs(self.x) + abs(self.y) + abs(self.z)
        kin = abs(self.vx) + abs(self.vy) + abs(self.vz)
        return pot * kin

    def __hash__(self):
        return self.energy()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and \
               self.vx == other.vx and self.vy == other.vy and self.vz == other.vz


def step(planets):
    next_step = []
    for planet in planets:
        next_p = copy.copy(planet)
        diff_x, diff_y, diff_z = 0, 0, 0
        for other_planet in planets:
            if planet != other_planet:
                if planet.x < other_planet.x:
                    diff_x += 1
                elif planet.x > other_planet.x:
                    diff_x -= 1
                if planet.y < other_planet.y:
                    diff_y += 1
                elif planet.y > other_planet.y:
                    diff_y -= 1
                if planet.z < other_planet.z:
                    diff_z += 1
                elif planet.z > other_planet.z:
                    diff_z -= 1
        next_p.vx += diff_x
        next_p.vy += diff_y
        next_p.vz += diff_z
        next_p.x += next_p.vx
        next_p.y += next_p.vy
        next_p.z += next_p.vz
        next_step.append(next_p)
    return next_step


io = Planet(13, 9, 5)
europa = Planet(8, 14, -2)
ganymede = Planet(-5, 4, 11)
callisto = Planet(2, -6, 1)
"""
io = Planet(-1, 0, 2)
europa = Planet(2, -10, -7)
ganymede = Planet(4, -8, 8)
callisto = Planet(3, 5, -1)
"""

jm = [io, europa, ganymede, callisto]
set_states_x_planet = [set(), set(), set()]
set_states = set()

set_states_x_planet[0].add(Coord(io.x, io.vx, europa.x, europa.vx, ganymede.x, ganymede.vx, callisto.x, callisto.vx))
set_states_x_planet[1].add(Coord(io.y, io.vy, europa.y, europa.vy, ganymede.y, ganymede.vy, callisto.y, callisto.vy))
set_states_x_planet[2].add(Coord(io.z, io.vz, europa.z, europa.vz, ganymede.z, ganymede.vz, callisto.z, callisto.vz))

repetitions = [[], [], []]
counter = 1

while True:
    if counter % 10000 == 0: print(jm)
    jm = step(jm)
    coordx = Coord(jm[0].x, jm[0].vx, jm[1].x, jm[1].vx, jm[2].x, jm[2].vx, jm[3].x, jm[3].vx)
    coordy = Coord(jm[0].y, jm[0].vy, jm[1].y, jm[1].vy, jm[2].y, jm[2].vy, jm[3].y, jm[3].vy)
    coordz = Coord(jm[0].z, jm[0].vz, jm[1].z, jm[1].vz, jm[2].z, jm[2].vz, jm[3].z, jm[3].vz)

    if coordx in set_states_x_planet[0]:
        repetitions[0].append(counter)
    else:
        set_states_x_planet[0].add(coordx)

    if coordy in set_states_x_planet[1]:
        repetitions[1].append(counter)
    else:
        set_states_x_planet[1].add(coordy)

    if coordz in set_states_x_planet[2]:
        repetitions[2].append(counter)
    else:
        set_states_x_planet[2].add(coordz)

    state = Moons(jm)
    if state in set_states:
        print(counter)
        break
    else:
        set_states.add(state)

    counter += 1
    if counter > 1000000:
        break

print(jm)
print(counter)
for index, elem in enumerate(repetitions):
    if elem == []:
        print("coordinate empty? ", index)
    print("x:", index, elem[0])


#running up to a million reps I get cycles at x:268296, y: 161428, z: 102356
#LCM: 277068010964808