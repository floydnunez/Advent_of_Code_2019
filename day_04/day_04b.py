lowend = 347312
highend = 805915

solutions = []

def never_decrease_digits(number):
    last = 0
    for char in number:
        if ord(char) >= last:
            last = ord(char)
        else:
            return False
    return True

def group_of_two(number):
    repeat = []
    for digit in range(0, 10):
        str_dig = str(digit)
        repeat.append(number.count(str_dig))
    if 2 in repeat:
        return True
    return False

for number in range(lowend, highend + 1):
    str_num = str(number)
    if never_decrease_digits(str_num) \
            and group_of_two(str_num):
        solutions.append(number)

#print("sols:", solutions)
print("size:", len(solutions))
#answer: 364