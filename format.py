import copy

def print_tree(tree, current="current"):
    print(current, tree.value)
    if tree.left is not None:
        print_tree(tree.left, "left")
    if tree.right is not None:
        print_tree(tree.right, "right")

def get_facts(facts, queries):
	facts.remove("=")
	queries.remove("?")
	f = {}
	for fact in facts:
		f[fact] = True
	return f, queries

def fill_dict(tree, values):
	if tree.value.isupper():
		values.append(tree.value)
		return values
	if tree.left and tree.left.value in ['+', '|', '^', '!']:
		values = fill_dict(tree.left, values)
	elif tree.left:
		values.append(tree.left.value)
	if tree.right and tree.right.value in ['+', '|', '^', '!']:
		values = fill_dict(tree.right, values)
	elif tree.right:
		values.append(tree.right.value)
	return values

def check_right(tree, values, signe=''):
	if signe == '+':
		signe = ''
	if tree.value.isupper():
		values.append(tree.value)
		return values

	if tree.left and tree.left.value in ['+', '!']:
		values = check_right(tree.left, values, tree.left.value)
	elif tree.left and tree.left.value in ['|', '^']:
		return values
	elif tree.left:
		values.append(signe + tree.left.value)

	if tree.right and tree.right.value in ['+', '!']:
		values = check_right(tree.right, values, tree.right.value)
	elif tree.right and tree.right.value in ['|', '^']:
		return values
	elif tree.right:
		values.append(signe + tree.right.value)
	
	return values

def split_rules(rules):
	new_rules = []
	for rule in rules:
		concerned_letter = check_right(rule.right, [])
		for x in concerned_letter:
			new_rule = copy.deepcopy(rule)
			if '!' in x:
				new_rule.right.value = '!'
				new_rule.right.left.value = x[1]
			else:			
				new_rule.right.value = x
				new_rule.right.left = None
			new_rule.right.right = None
			new_rules.append(new_rule)
	return new_rules

def get_dict(rules, initial_facts, queries):
	dictionnaire = {}
	facts, queries = get_facts(initial_facts, queries)
	rules = split_rules(rules)
	for rule in rules:
		values = []
		values = fill_dict(rule.right, values)
		for value in values:
			try:
				dictionnaire[value].append({"règle": rule, "faite": False})
				#dictionnaire[value].append(rule)
			except:
				dictionnaire[value] = []
				dictionnaire[value].append({"règle": rule, "faite": False})
				#dictionnaire[value].append(rule)
	return dictionnaire, facts, queries, initial_facts