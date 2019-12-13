import math

debug = False

filename = "input_11.txt"

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
            put(data, resu, get(data, arg1, input_mode_1)
                + get(data, arg2, input_mode_2), resul_mode)
            index += 4
            if debug: print("add:", arg1, arg2, resu, input_mode_1, input_mode_2, resul_mode)
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
            if debug: print("**************  wri:", write_output, index)
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

cells = [[0, 0]]

#up, right, down, left
heading_direction = 0

color_per_cell = {}

def move_robot(diff_x, diff_y):
    curr_cell = cells[-1]
    cells.append([curr_cell[0] + diff_x, curr_cell[1] + diff_y])


def get_color(x,y):
    hashval = str(x) + '_' + str(y)
    if hashval not in color_per_cell:
        color_per_cell[hashval] = 0
    return color_per_cell[hashval]


def get_curr_color():
    curr_cell = cells[-1]
    #print("get curr color:", curr_cell)
    curr_color = get_color(curr_cell[0], curr_cell[1])
    if curr_color <= 0:
        return 0
    else:
        return  1


def paint_map(color, x, y):
    hashval = str(x) + '_' + str(y)
    color_per_cell[hashval] = color


def move(order, direction):
    if order == 0:
        direction -= 1
    if order == 1:
        direction += 1
    while direction < 0:
        direction += 4
    direction = direction % 4
    if direction == 0:
        return direction, 0, -1
    if direction == 1:
        return direction, 1, 0
    if direction == 2:
        return direction, 0, 1
    if direction == 3:
        return direction, -1, 0


index = 0

relative_base = 0
while True:
    paint_color, data, index, relative_base = process(data, [get_curr_color()], index, relative_base)
    if index == -1:
        print("paint: ", paint_color)
        paint_map(paint_color, cells[-1][0], cells[-1][1])
        break
    turn, data, index, relative_base = process(data, [], index, relative_base)
    if index == -1:
        print("turn: ", turn)
        heading_direction, plus_x, plus_y = move(turn, heading_direction)
        break
    print(paint_color, heading_direction)
    paint_map(paint_color, cells[-1][0], cells[-1][1])
    heading_direction, plus_x, plus_y = move(turn, heading_direction)
    move_robot(plus_x, plus_y)

print(color_per_cell)
print(len(color_per_cell))
#wrong: 16, 17
#right 2184
print("finished")


