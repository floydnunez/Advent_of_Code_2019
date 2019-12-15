
import cProfile

def all(mult):
    debug = False
    use_print = False

    filename = "input_14.txt"

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    def add_results(amounts, element, used, obtained):
#        if element == 'FUEL': print('whaaat?')
        if use_print: print('adding', result, used)
        amounts[element] += obtained - used
        return amounts


    def apply_rules(rules, reverse_rules, needed, ore_used, amounts):
        rule_to_apply = reverse_rules[needed[1]]
        if use_print: print('to get', needed, ' we use rule:', rule_to_apply, 'stored:', amounts)
        obtained = 0
        already_got = amounts[needed[1]]
        if already_got >= needed[0]:
            if use_print: print('using the stored amount:', amounts[needed[1]])
            amounts[needed[1]] = already_got - needed[0]
            return ore_used, amounts
        while obtained < needed[0] - already_got:
            for reagent in rule_to_apply:
                if use_print: print('reagent:', reagent)
                if reagent[1] == 'ORE':
                    if use_print: print('------------------------using ore:', reagent[0])
                    ore_used += reagent[0]
                else:
                    ore_used, amounts = apply_rules(rules, reverse_rules, reagent, ore_used, amounts)
            result = rules[rule_to_apply]
            obtained += result[0]
        amounts = add_results(amounts, needed[1], needed[0], obtained)
        return ore_used, amounts


    def parse_content(content, multiplier):
        rules = {}
        necessaries = []
        necessaries_length = []
        for line in content:
            necessary, result = line.split('=>')
            necessary_list = []
            ingredients = necessary.split(',')
            for ingredient in ingredients:
                amount, element = ingredient.strip().split(' ')
                necessary_list.append((int(amount) * multiplier, element))
            amount_result, result_element = result.strip().split(' ')
            result_list = (int(amount_result) * multiplier, result_element)
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


    rules, ordered_rules, final_rule = parse_content(content, 1)
    rulesxx, ordered_rulesxx, final_rule = parse_content(content, mult)

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
    reverse_rulesxx = {v[1]: k for k, v in rulesxx.items()}


    print(reverse_rules)
    print('\n\n-----\n\n')
    print(rules)

    count = 0
    trillion = 1000000000000
    while ore_used < trillion:
        if trillion - ore_used < trillion / 1000:
            ore_used, amounts = apply_rules(rules, reverse_rules, (1, 'FUEL'), ore_used, amounts)
        else:
            ore_used, amounts = apply_rules(rulesxx, reverse_rulesxx, (1, 'FUEL'), ore_used, amounts)
        count += 1
        if count % 1000 == 0: print(count, ore_used, flush=True)

    print(amounts)
    print('ore_used', ore_used, 'count:', count - 1)

all(99)
#wrong: 1259237 too high
#wrong: 553102 too high
#wrong 3566565 too low

#right 3566577
#part b: 1915595 too low
#multiplier 20     3566561
#multiplier 100:   3566501
#multiplier 1000:  3565001
#multiplier 10000: 3565001

#scale: 199: 3566561
#scale: 200, 250: 3566577
