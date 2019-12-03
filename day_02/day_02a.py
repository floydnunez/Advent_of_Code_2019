import math

filename = "input_02.txt"

with open(filename) as f:
    content = f.readline() #only read THE FIRST LINE

data = content.split(",")
#clean the data, and make it ints
data = [int(x.strip()) for x in data]

#first, replace initial values
data[1] = 12
data[2] = 2

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

print("result:", data[0])
#answer: 3058646