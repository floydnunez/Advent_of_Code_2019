filename = "input_08.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

image_data = content[0]
print("image length:", len(image_data))
layers = []

for index in range(0, 100):
    layers.append(image_data[150 * index : 150 * (index + 1) ])

layer_char_count = []
layer_with_less_zeros = 0
zeros = 9999999
for index, layer in enumerate(layers):
    print("layer length:", len(layer))
    char_count = []
    for char in range(ord('0'), ord('9') + 1):
        char_count.append(layer.count(chr(char)))
    print(char_count)
    layer_char_count.append(char_count)
    if zeros > char_count[0]:
        zeros = char_count[0]
        layer_with_less_zeros = index

print("which layer?", layer_with_less_zeros)
print("result:", layer_char_count[layer_with_less_zeros][1] * layer_char_count[layer_with_less_zeros][2])

#answer: 1463