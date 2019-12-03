import math

filename = "input_02.txt"

with open(filename) as f:
    content = f.readline() #only read THE FIRST LINE

data = content.split(",")
#clean the data, and make it ints
data = [int(x.strip()) for x in data]

def process(data, noun, verb):
    #first, replace initial values
    data[1] = noun
    data[2] = verb

    #process four by four
    index = 0
    size = len(data)

    while(index < size):
        oper = data[index]
        arg1 = data[index + 1]
        arg2 = data[index + 2]
        resu = data[index + 3]

        if oper == 1:
            data[resu] = data[arg1] + data[arg2]
        if oper == 2:
            data[resu] = data[arg1] * data[arg2]
        if oper == 99:
            index = 9999
        index += 4
    return data[0]

for noun in range(0,100):
    for verb in range(0,100):
        result = process(data.copy(), noun, verb)
        if result == 19690720:
            print("noun", noun, "verb", verb)

#answer noun 89 verb 76

