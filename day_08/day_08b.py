filename = "input_08.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

image_data = content[0]
print("image length:", len(image_data))
layers = []

#image_data, layer_length, layer_count, columns, rows = "0222112222120000", 4, 4, 2, 2

layer_length, layer_count, columns, rows = 150, 100, 25, 6

for index in range(0, layer_count):
    layers.append(image_data[layer_length * index : layer_length * (index + 1) ])

print(layers)

image = ['2'] * rows * columns

print('len image', len(image))

for layer in layers:
    for index, char in enumerate(layer):
        if image[index] == '2':
            image[index] = char

for row in range(0, rows):
#    print("from:", columns * row, "to:", columns * (row + 1))
    line = image[columns * row : columns * (row + 1)]
#    line.reverse()
    line_str = ''
    for char in line:
        if char == '0':
            line_str += ' '
        elif char == '1':
            line_str += '#'
        else:
            line_str += '#'
    print(line_str)

#answer GKCKH
