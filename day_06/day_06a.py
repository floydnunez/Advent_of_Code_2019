

filename = "input_06.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]


direct_orbits = len(content)
print("direct orbits:", direct_orbits)

orbits = {}
bodies = set()
centers = set()

for line in content:
    orbitee, satelite = line.split(")")
    #print(orbitee, satelite)
    orbits[satelite] = orbitee
    bodies.add(satelite)
    centers.add(orbitee)

#print("bodies:", bodies)

#sanity check: should just say "COM"
for elem in centers:
    if not elem in bodies:
        print("not in bodies:", elem)

#now to get the distance from all satelites to COM
indirect_orbits = 0
for body in bodies:
    while True:
        center = orbits[body]
        if center != 'COM':
            indirect_orbits += 1
            body = center
        else:
            break

print("indirect orbits:", indirect_orbits)

print("grand total: ", direct_orbits + indirect_orbits)

#answer 247089



