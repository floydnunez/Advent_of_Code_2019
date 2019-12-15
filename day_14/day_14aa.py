
debug = True
use_print = False

import functools
print = functools.partial(print, flush=True)

filename = "input_14.txt"

with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

def apply_rules(rules, ordered_rules, amounts, ore_used):
    for rule in ordered_rules:
        do_we_have_the_elements = True
        for pair in rule:
            if amounts[pair[1]] < pair[0]:
                do_we_have_the_elements = False
                break
        if do_we_have_the_elements:
            new_elements = rules[rule]
            #take away elements used
            for elem in rule:
                if use_print: print('using', elem)
                old_val = amounts[elem[1]]
                amounts[elem[1]] = old_val - elem[0]
                if elem[1] == 'ORE':
                    ore_used += elem[0]
            #add the elements to the amounts
            if use_print: print('applying: rule:', rule, 'new_elements:', new_elements)
            for result in new_elements:
                old_val = amounts[result[1]]
                amounts[result[1]] = old_val + result[0]
            break
    return amounts, ore_used

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
        rules[necessary_tuple] = [result_list]
        if result_element == 'FUEL':
            final_rule = necessary_tuple
        else:
            necessaries.append(necessary_tuple)
            necessaries_length.append(len(necessary_tuple))

    if debug: print('final rule:', final_rule)

    return rules, final_rule


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


def consolidate_rules(rules, unique_elems):
    #add up the rules that are made of a single element
    consolidated_rules = {}
    necessaries = []
    necessaries_length = []
    for elem in unique_elems:
        amount = 0
        result = []
        for key in rules.keys():
            if elem == key[0][1]:
                if debug: print('key:', key, len(key))
                if len(key) == 1:
                    temp_list = rules[key]
                    result.append(temp_list[0])
                    amount += key[0][0]
                    if debug: print(amount, elem)
        if amount > 0:
            new_key = tuple([tuple([amount, elem])])
            if debug: print('adding', new_key, '=', result)
            consolidated_rules[new_key] = result
            necessaries.append(new_key)
            necessaries_length.append(len(new_key))

    for key, val in rules.items():
        if len(key) > 1:
            consolidated_rules[key] = val
            necessaries.append(key)
            necessaries_length.append(len(key))
        if val[0][1] == 'FUEL':
            final_rule = key

    if debug: print('necessaries:', necessaries)
    if debug: print('necessaries_length:', necessaries_length)
    for elem in zip(necessaries_length, necessaries):
        if debug: print('elem', elem)
    ordered_rules = [x for _,x in sorted(zip(necessaries_length, necessaries))]
    ordered_rules.reverse()

    if debug: print("conso rules:", consolidated_rules)
    return consolidated_rules, ordered_rules

rules, final_rule = parse_content(content)

unique_elems, amounts = get_unique_elements(rules)
amounts['FUEL'] = 0

print(amounts)
print(unique_elems)

rules, ordered_rules = consolidate_rules(rules, unique_elems)

for rule in ordered_rules:
    result = rules[rule]
    print('rule:', rule, '->', result)

count = 0
ore_used = 0
while amounts['FUEL'] <= 0:
    amounts, ore_used = apply_rules(rules, ordered_rules, amounts, ore_used)
    if count % 100000 == 0 or use_print: print(amounts, 'ore:', ore_used)
    count += 1

print('ore_used', ore_used)

