import math
import sys

debug = False

filename = "input_13.txt"

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
    if debug: print("val at (", at, ") =", int(str_num[length - at - 1]), " for ", number)
    return int(str_num[length - at - 1])


def process(data, input, index, relative_base):
    if debug: print("input:", input)
    input_index = 0
    size = len(data)

    last_evaluated_output = 0

    def get(array, address, input_mode):
        if input_mode == 1:
            return address
        curr_size = len(array)
        if input_mode == 2:
            address += relative_base
            if debug: print("get, relative mode: base:", relative_base, "address:", address)
        #let's duplicate the length
        while address >= curr_size:
            array += [0] * curr_size * 4
            curr_size = len(array)
        return array[address]

    def put(array, address, value, input_mode):
        curr_size = len(array)
        if input_mode == 2:
            address += relative_base
        #let's duplicate the length
        while address >= curr_size:
            array += [0] * curr_size
            curr_size = len(array)
        if debug: print("put at", address, "value:", value, "input_mode", input_mode, relative_base)
        array[address] = value

    while(index < size):
        try:
            operation = data[index]
        except:
            print("index:", index)
            return
        oper = operation % 100
        input_mode_1 = val_at(operation, 2)
        input_mode_2 = val_at(operation, 3)
        resul_mode = val_at(operation, 4)#not used right now
        if debug: print("index:", index, "operation:", operation)
        if oper == 1:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            resu = data[index + 3]
            value = get(data, arg1, input_mode_1) + get(data, arg2, input_mode_2)
            put(data, resu, value, resul_mode)
            index += 4
            if debug: print("add:", arg1, arg2, resu, input_mode_1, input_mode_2, resul_mode, value)
        elif oper == 2:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            resu = data[index + 3]
            put(data, resu, get(data, arg1, input_mode_1)
                * get(data, arg2, input_mode_2), resul_mode)
            index += 4
            if debug: print("mul:", arg1, arg2, resu, input_mode_1, input_mode_2)
        elif oper == 3:
            if debug: print("operacion: read:", operation, "input_index", input_index, "input[input_index]", input[input_index], "arg:", data[index+1])
            read_input = input[input_index]
            input_index += 1
            arg = data[index + 1]
            put(data, arg, read_input, input_mode_1)
            index += 2
            if debug: print("rea:", read_input, "to:", arg + relative_base, relative_base, arg)
        elif oper == 4:
            write_param = data[index + 1]
            write_output = get(data, write_param, input_mode_1)
            index += 2
            last_evaluated_output = write_output
            if debug: print("**************  wri:", write_output, index, input_mode_1, "val:", get(data, write_param, input_mode_1))
            return last_evaluated_output, data, index, relative_base
        elif oper == 5:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            arg1 = get(data, arg1, input_mode_1)
            arg2 = get(data, arg2, input_mode_2)
            if arg1 != 0:
                index = arg2
            else:
                index += 3
            if debug: print("jiT:", arg1, arg2)
        elif oper == 6:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            arg1 = get(data, arg1, input_mode_1)
            arg2 = get(data, arg2, input_mode_2)
            if arg1 == 0:
                index = arg2
            else:
                index += 3
            if debug: print("jiF:", arg1, arg2)
        elif oper == 7:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            arg1 = get(data, arg1, input_mode_1)
            arg2 = get(data, arg2, input_mode_2)
            resu = data[index + 3]
            if arg1 < arg2:
                put(data, resu, 1, resul_mode)
            else:
                put(data, resu, 0, resul_mode)
            index += 4
            if debug: print("let:", arg1, arg2, "to:", data[index + 3])
        elif oper == 8:
            arg1 = data[index + 1]
            arg2 = data[index + 2]
            arg1 = get(data, arg1, input_mode_1)
            arg2 = get(data, arg2, input_mode_2)
            resu = data[index + 3]
            if arg1 == arg2:
                put(data, resu, 1, resul_mode)
            else:
                put(data, resu, 0, resul_mode)
            index += 4
            if debug: print("equ:", arg1, arg2, "to:", data[index + 3])
        elif oper == 9:
            arg = data[index + 1]
            if debug: print("adjust relative base: ", arg, " input mode:", input_mode_1)
            relative_base += get(data, arg, input_mode_1)
            if debug: print("rel: ", relative_base)
            index += 2
        elif oper == 99:
            index = 9999
            if debug: print("returning:", last_evaluated_output)
            return last_evaluated_output, [], -1, 0
        if debug: print("end if")


index = 0

counter = 0

screen = {}

x_res = 1000
relative_base = 0

data[0] = 2 #number of quarters
next_input = 0
last_ball_pos_x = -1
last_padl_pos_x = -1
while True:
    if index == -1:
        break
    coord_x, data, index, relative_base = process(data, [next_input], index, relative_base)
    if index == -1:
        break
    coord_y, data, index, relative_base = process(data, [next_input], index, relative_base)
    if index == -1:
        break
    tile, data, index, relative_base = process(data, [next_input], index, relative_base)
    if index == -1:
        break
    counter += 1
    if tile == 4:
        print("counter:", counter, "ball pos:", coord_x, coord_y)
        last_ball_pos_x = coord_x
    if tile == 3:
        print("counter:", counter, "padl pos:", coord_x, coord_y)
        last_padl_pos_x = coord_x
    if coord_x < 0:
        print("score: ", tile)
    if last_ball_pos_x >= 0 and last_padl_pos_x >= 0:
        if last_ball_pos_x > last_padl_pos_x:
            next_input = 1
        elif last_ball_pos_x < last_padl_pos_x:
            next_input = -1
        else:
            next_input = 0

print("blocks on screen: ", len(screen.keys()))


#wrong: 1040, 390, 975 (too high)
#right: 298



