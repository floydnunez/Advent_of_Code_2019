lowend = 347312
highend = 805915

solutions = []

def check_adjacent_digits(number):
    if "11" in str_num or "22" in str_num or "33" in str_num or "44" in str_num \
        or "55" in str_num or "66" in str_num or "77" in str_num or "88" in str_num \
        or "99" in str_num or "00" in str_num:
        return True
    return False

def never_decrease_digits(number):
    last = 0
    for char in number:
        if ord(char) >= last:
            last = ord(char)
        else:
            return False
    return True

for number in range(lowend, highend + 1):
    str_num = str(number)
    if check_adjacent_digits(str_num) and never_decrease_digits(str_num):
        solutions.append(number)

#print("sols:", solutions)
print("size:", len(solutions))
#answer: 594