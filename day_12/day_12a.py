import copy

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

jupiter_moons = [io, europa, ganymede, callisto]

for index in range(0, 1000):
    print(jupiter_moons)
    jupiter_moons = step(jupiter_moons)

print(jupiter_moons)
total_energy = 0

for elem in jupiter_moons:
    total_energy += elem.energy()

print(total_energy)
