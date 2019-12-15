
debug = True
use_print = False

import functools
print = functools.partial(print, flush=True)

filename = "input_14.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

def add_results(amounts, element, used, obtained):
    print('adding', result, used)
    amounts[element] += obtained - used
    return amounts


def apply_rules(rules, reverse_rules, needed, ore_used, amounts):
    rule_to_apply = reverse_rules[needed[1]]
    print('to get', needed, ' we use rule:', rule_to_apply, 'stored:', amounts)
    obtained = 0
    if amounts[needed[1]] >= needed[0]:
        print('using the stored amount:', amounts[needed[1]])
        amounts[needed[1]] -= needed[0]
        return ore_used, amounts
    already_got = amounts[needed[1]]
    while obtained < needed[0] - already_got:
        for reagent in rule_to_apply:
            print('reagent:', reagent)
            if reagent[1] == 'ORE':
                print('------------------------using ore:', reagent[0])
                ore_used += reagent[0]
            else:
                ore_used, amounts = apply_rules(rules, reverse_rules, reagent, ore_used, amounts)
        result = rules[rule_to_apply]
        obtained += result[0]
    amounts = add_results(amounts, needed[1], needed[0], obtained)
    return ore_used, amounts

def parse_content(content):
    rules = {}
    necessaries = []
    necessaries_length = []
    for line in content:
        necessary, result = line.split('=>')
        necessary_list = []
        ingredients = necessary.split(',')
        for ingredient in ingredients:
            amount, element = ingredient.strip().split(' ')
            necessary_list.append((int(amount), element))
        amount_result, result_element = result.strip().split(' ')
        result_list = (int(amount_result), result_element)
        necessary_tuple = tuple(necessary_list)
        rules[necessary_tuple] = result_list
        if result_element == 'FUEL':
            final_rule = necessary_tuple
        else:
            necessaries.append(necessary_tuple)
            necessaries_length.append(len(necessary_tuple))

    if debug: print('final rule:', final_rule)

    if debug: print('necessaries:', necessaries)
    if debug: print('necessaries_length:', necessaries_length)
    for elem in zip(necessaries_length, necessaries):
        if debug: print('elem', elem)
    ordered_rules = [x for _,x in sorted(zip(necessaries_length, necessaries))]
    ordered_rules.reverse()

    return rules, ordered_rules, final_rule


def get_unique_elements(rules):
    uniques = set()
    amounts = {}
    for rule in rules:
        for pair in rule:
            uniques.add(pair[1])
    for elem in uniques:
        if elem == 'ORE':
            amounts[elem] = 9999999
        else:
            amounts[elem] = 0
    return uniques, amounts


rules, ordered_rules, final_rule = parse_content(content)

unique_elems, amounts = get_unique_elements(rules)
amounts['FUEL'] = 0
amounts['ORE'] = 100

print(amounts)
print(unique_elems)


for rule in ordered_rules:
    result = rules[rule]
    print('rule:', rule, '->', result)


count = 0
ore_used = 0

reverse_rules = {v[1]: k for k, v in rules.items()}


print(reverse_rules)
print('\n\n-----\n\n')
print(rules)
ore_used, amounts = apply_rules(rules, reverse_rules, (1, 'FUEL'), ore_used, amounts)

print(amounts)
print('ore_used', ore_used)

#wrong: 1259237 too high
#wrong: 553102 too high

#right 522031