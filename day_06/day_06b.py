

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

def get_orbit_list(body):
    result = []
    current_body = body
    while True:
        current_body = orbits[current_body]
        result.append(current_body)
        if current_body == 'COM':
            break
    return result

santa_2_com = get_orbit_list('SAN')
you_2_com = get_orbit_list('YOU')

santa_2_com.reverse()
you_2_com.reverse()

print(santa_2_com)
print(you_2_com)

common_elements = 0
#now, we walk the lists until they differ
for index, elem in enumerate(santa_2_com):
    equivalent_elem = you_2_com[index]
    if equivalent_elem != elem:
        break
    else:
        common_elements += 1

print("common elements", common_elements, "santa:", len(santa_2_com), "you:", len(you_2_com))
print("result =", len(santa_2_com) - common_elements + len(you_2_com) - common_elements)
#answer: 442