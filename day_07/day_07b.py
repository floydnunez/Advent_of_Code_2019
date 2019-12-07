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

def process(data, input, index):
    if debug: print("input:", input)
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
            if debug: print("add:", arg1, arg2, resu, input_mode_1, input_mode_2, "index:", index, "result:", data[resu])
        elif oper == 2:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            resu = data[index + 3]
            data[resu] = (data[arg1] if input_mode_1 == 0 else arg1) * (data[arg2] if input_mode_2 == 0 else arg2)
            index += 4
            if debug: print("mul:", arg1, arg2, resu, input_mode_1, input_mode_2, "index:", index, "result:", data[resu])
        elif oper == 3:
            read_input = input[input_index]
            input_index += 1
            data[data[index + 1]] = read_input
            index += 2
            print("read: ", read_input)
            if debug: print("rea:", read_input, "to:", data[index + 1], "index:", index)
        elif oper == 4:
            write_output = data[index + 1] if input_mode_1 == 1 else data[data[index+1]] #careful
            index += 2
            last_evaluated_output = write_output
            print("wri:", write_output, "index:", index)
            return last_evaluated_output, data, index
        elif oper == 5:
            arg1 = data[index + 1] if input_mode_1 == 1 else data[data[index + 1]]
            arg2 = data[index + 2] if input_mode_2 == 1 else data[data[index + 2]]
            if arg1 != 0:
                index = arg2
            else:
                index += 3
            if debug: print("jiT:", arg1, arg2, "index:", index)
        elif oper == 6:
            arg1 = data[index + 1] if input_mode_1 == 1 else data[data[index + 1]]
            arg2 = data[index + 2] if input_mode_2 == 1 else data[data[index + 2]]
            if arg1 == 0:
                index = arg2
            else:
                index += 3
            if debug: print("jiF:", arg1, arg2, "index:", index)
        elif oper == 7:
            arg1 = data[index + 1] if input_mode_1 == 1 else data[data[index + 1]]
            arg2 = data[index + 2] if input_mode_2 == 1 else data[data[index + 2]]
            if arg1 < arg2:
                data[data[index + 3]] = 1
            else:
                data[data[index + 3]] = 0
            index += 4
            if debug: print("let:", arg1, arg2, "to:", data[index + 3], "index:", index)
        elif oper == 8:
            arg1 = data[index + 1] if input_mode_1 == 1 else data[data[index + 1]]
            arg2 = data[index + 2] if input_mode_2 == 1 else data[data[index + 2]]
            if arg1 == arg2:
                data[data[index + 3]] = 1
            else:
                data[data[index + 3]] = 0
            index += 4
            if debug: print("equ:", arg1, arg2, "to:", data[index + 3], "index:", index)
        elif oper == 99:
            index = 9999
            print("returning:", last_evaluated_output)
            return last_evaluated_output, [], -1
        if debug: print("end if")

#data = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
#amplifiers = [1,0,4,3,2]

list_of_amplifiers_lists = []

for aa in range(5, 10):
    for bb in range(5, 10):
        for cc in range(5, 10):
            for dd in range(5, 10):
                for ee in range(5, 10):
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

#data = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
#list_of_amplifiers_lists = [[9,7,8,5,6]]

#data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#list_of_amplifiers_lists = [[9,8,7,6,5]]


for amplifiers in list_of_amplifiers_lists:
    output = 0
    keep_iterating = True
    first = True
    states = [data.copy(), data.copy(), data.copy(), data.copy(), data.copy()]
    indexes = [0, 0, 0, 0, 0]
    while keep_iterating:
        new_data = []
        for index, elem in enumerate(amplifiers):
            if first:
                input = [elem, output]
            else:
                input = [output]
            print("calling amp[", index, "] with input:", input, "and index:", indexes[index])
            #print("old state[", index,"] =", states[index])
            try:
                output, new_data, old_index = process(states[index], input, indexes[index])
                states[index] = new_data
            #print("new state[", index,"] =", new_data)
                indexes[index] = old_index
            except:
                break
        first = False
        if max_result < output:
            max_result = output
            max_amplifiers = amplifiers
        if new_data == []:
            keep_iterating = False
            break

print("final result:", max_result, "with", max_amplifiers)


print("all:", len(list_of_amplifiers_lists))
#wrong answer:  9020032 (too low)
#right answer: 35961106 (the try catch was necessary

