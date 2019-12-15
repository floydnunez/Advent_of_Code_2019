
import cProfile

def all(multiplier):
    debug = False
    use_print = False

    filename = "input_14.txt"

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    def add_results(amounts, element, used, obtained):
        amounts[element] += obtained - used
        return amounts


    def apply_rules(rules, reverse_rules, needed, ore_used, amounts):
        already_got = amounts[needed[1]]
        rule_to_apply = reverse_rules[needed[1]]
        obtained = 0
        if already_got >= needed[0]:
            amounts[needed[1]] = already_got - needed[0]
            return ore_used, amounts
        while obtained < needed[0] - already_got:
            for reagent in rule_to_apply:
                if reagent[1] == 'ORE':
                    ore_used += reagent[0]
                else:
                    ore_used, amounts = apply_rules(rules, reverse_rules, reagent, ore_used, amounts)
            result = rules[rule_to_apply]
            obtained += result[0]
        amounts = add_results(amounts, needed[1], needed[0], obtained)
        return ore_used, amounts


    def parse_content(content):
        rules = {}
        rulesx = {}
        necessaries = []
        necessaries_length = []
        for line in content:
            necessary, result = line.split('=>')
            necessary_list = []
            necessary_list_mult = []
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


    rules, ordered_rules, final_rule = parse_content(content)

    unique_elems, amounts = get_unique_elements(rules)
    amounts['FUEL'] = 0
    amounts['ORE'] = 0
    amounts = {'DQRM': 1, 'DVHQD': 2, 'SWBRL': 5, 'SCXQ': 0, 'XLNR': 0, 'RCNV': 0, 'CQRWX': 0, 'CFKF': 4, 'QFBZN': 1, 'JBRG': 4, 'GBJC': 2, 'NBVPR': 5, 'DNXHG': 3, 'FXBZT': 2, 'LSLQW': 3, 'QZNXC': 0, 'ZFBTC': 0, 'MLPH': 0, 'LWBQL': 5, 'NQXZM': 2, 'QXWFM': 1, 'TFMNM': 0, 'RCKS': 2, 'XKXPK': 1, 'LJCR': 3, 'DXDTM': 4, 'QKCQW': 2, 'ZGVC': 2, 'DZXGB': 2, 'TWBN': 3, 'LGXK': 0, 'NLJH': 0, 'DMLM': 1, 'HGNW': 6, 'JMVG': 1, 'MBXSW': 0, 'WZSH': 0, 'MSXF': 1, 'GBNH': 4, 'TSMCQ': 2, 'FZVM': 0, 'LKTZ': 2, 'JCSDM': 2, 'LJQGC': 0, 'SDQK': 0, 'FKPL': 0, 'ORE': 0, 'QBVQ': 1, 'LMPH': 0, 'VRZND': 3, 'MWQTH': 0, 'PLWS': 0, 'WCHD': 1, 'JMCQ': 0, 'BGKJ': 8, 'BXPB': 0, 'XPGX': 0, 'TDFGK': 7, 'FUEL': 0}

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

    count = 0
    trillion = 714286000
    amounts
    while ore_used < 333100000:
        ore_used, amounts = apply_rules(rules, reverse_rules, (1, 'FUEL'), ore_used, amounts)
        count += 1
        if count % 1000 == 0: print(count, ore_used)

    print(amounts)
    print('ore_used', ore_used, 'count:', count - 1) #off by one
    print(amounts)

multiplier = 1
all(multiplier)
print('multiplier:', multiplier)
#wrong: 1259237 too high
#wrong: 553102 too high

#right 522031
#part b: 1915595 too low

#3566579
#the running on the terminal is 23

# base: 10 3566571 - 1 = 3566570 + 54
#wrong: too high:   3566624
#right              3566577
#multiplier 5:
#multiplier 7:
#multiplier 10:     3566571
#multiplier 17:
#multiplier 19:     3566567
#multiplier 20:     3566561
#multiplier 23:
#multiplier 100:    3566501
#multiplier 1000:   3565001
#multiplier 10000:  3565001
#multiplier 100000: 3500001
