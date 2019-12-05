import math

debug = False

filename = "input_05.txt"

with open(filename) as f:
    content = f.readline() #only read THE FIRST LINE

data = content.split(",")
#clean the data, and make it ints
data = [int(x.strip()) for x in data]

def val_at(number, at):
    str_num = str(number)
    length = len(str_num)
    if at >= length:
        return 0
    return int(str_num[length - at - 1])

def process(data, input):

    index = 0
    input_index = 0
    size = len(data)

    while(index < size):
        operation = data[index]
        oper = operation % 100
        input_mode_1 = val_at(operation, 2)
        input_mode_2 = val_at(operation, 3)
        #resul_mode = operation % 100000 #not used right now
        if debug: print("index:", index, "operation:", operation)
        if oper == 1:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            resu = data[index + 3]
            data[resu] = (data[arg1] if input_mode_1 == 0 else arg1) + (data[arg2] if input_mode_2 == 0 else arg2)
            index += 4
            if debug: print("add:", arg1, arg2, resu, input_mode_1, input_mode_2)
        elif oper == 2:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            resu = data[index + 3]
            data[resu] = (data[arg1] if input_mode_1 == 0 else arg1) * (data[arg2] if input_mode_2 == 0 else arg2)
            index += 4
            if debug: print("mul:", arg1, arg2, resu, input_mode_1, input_mode_2)
        elif oper == 3:
            read_input = input[input_index]
            input_index += 1
            data[data[index + 1]] = read_input
            index += 2
            if debug: ("rea:", read_input, "to:", data[index + 1])
        elif oper == 4:
            write_output = data[index + 1] if input_mode_1 == 1 else data[data[index+1]] #careful
            index += 2
            print("wri:", write_output)
        elif oper == 99:
            index = 9999
            return

process(data, [1])

#answer: 12440243
