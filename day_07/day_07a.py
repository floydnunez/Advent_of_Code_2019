import math

debug = False

filename = "input_07.txt"

with open(filename) as f:
    content = f.readline() #only read THE FIRST LINE

data = content.split(",")
#clean the data, and make it ints
data = [int(x.strip()) for x in data]

#data = [3,9,8,9,10,9,4,9,99,-1,8]

def val_at(number, at):
    str_num = str(number)
    length = len(str_num)
    if at >= length:
        return 0
    return int(str_num[length - at - 1])

def process(data, input):
    if debug: print("input:", input)
    index = 0
    input_index = 0
    size = len(data)

    last_evaluated_output = 0

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
            if debug: print("rea:", read_input, "to:", data[index + 1])
        elif oper == 4:
            write_output = data[index + 1] if input_mode_1 == 1 else data[data[index+1]] #careful
            index += 2
            last_evaluated_output = write_output
            print("wri:", write_output)
        elif oper == 5:
            arg1 = data[index + 1] if input_mode_1 == 1 else data[data[index + 1]]
            arg2 = data[index + 2] if input_mode_2 == 1 else data[data[index + 2]]
            if arg1 != 0:
                index = arg2
            else:
                index += 3
            if debug: print("jiT:", arg1, arg2)
        elif oper == 6:
            arg1 = data[index + 1] if input_mode_1 == 1 else data[data[index + 1]]
            arg2 = data[index + 2] if input_mode_2 == 1 else data[data[index + 2]]
            if arg1 == 0:
                index = arg2
            else:
                index += 3
            if debug: print("jiF:", arg1, arg2)
        elif oper == 7:
            arg1 = data[index + 1] if input_mode_1 == 1 else data[data[index + 1]]
            arg2 = data[index + 2] if input_mode_2 == 1 else data[data[index + 2]]
            if arg1 < arg2:
                data[data[index + 3]] = 1
            else:
                data[data[index + 3]] = 0
            index += 4
            if debug: print("let:", arg1, arg2, "to:", data[index + 3])
        elif oper == 8:
            arg1 = data[index + 1] if input_mode_1 == 1 else data[data[index + 1]]
            arg2 = data[index + 2] if input_mode_2 == 1 else data[data[index + 2]]
            if arg1 == arg2:
                data[data[index + 3]] = 1
            else:
                data[data[index + 3]] = 0
            index += 4
            if debug: print("equ:", arg1, arg2, "to:", data[index + 3])
        elif oper == 99:
            index = 9999
            if debug: print("returning:", last_evaluated_output)
            return last_evaluated_output
        if debug: print("end if")

#data = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
#amplifiers = [1,0,4,3,2]

list_of_amplifiers_lists = []

for aa in range(0,5):
    for bb in range(0, 5):
        for cc in range(0, 5):
            for dd in range(0, 5):
                for ee in range(0, 5):
                    potential_list = [aa,bb,cc,dd,ee]
                    #ugh, ugly if. It didn't work at first with "count" but now that I know
                    #the cause won't rewrite it
                    if aa != bb and aa != cc and aa != dd and aa != ee and \
                        bb != cc and bb != dd and bb != ee and \
                        cc != dd and cc != ee and dd != ee:
                        list_of_amplifiers_lists.append(potential_list)

print(list_of_amplifiers_lists)

max_result = 0
max_amplifiers = []

for amplifiers in list_of_amplifiers_lists:
    output = 0
    for elem in amplifiers:
        output = process(data, [elem, output])
    if max_result < output:
        max_result = output
        max_amplifiers = amplifiers

print("final result:", max_result, "with", max_amplifiers)


print("all:", len(list_of_amplifiers_lists))
#wrong answer: 1085808, 33693 (too high)
#answer: 19650 with [2, 0, 1, 4, 3]


