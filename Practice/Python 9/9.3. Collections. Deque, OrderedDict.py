from collections import OrderedDict

# Let create a dict with list of typles by standard means

data = [("Ivan", 19), ("Mark", 25), ("Andrey", 23), ("Maria", 20)]

client_ages = dict(data)
print(client_ages) # {'Ivan': 19, 'Mark': 25, 'Andrey': 23, 'Maria': 20}

# in some cases (maybe older verions?) the order will change after running the program
# to avoid that we use OrderedDict

ordered_client_ages = OrderedDict(data)

print (ordered_client_ages) # OrderedDict([('Ivan', 19), ('Mark', 25), ('Andrey', 23), ('Maria', 20)])

# we can sort now by age for example
ordered_client_ages = OrderedDict(sorted(data, key = lambda x: x[1]))
print (ordered_client_ages) # OrderedDict([('Ivan', 19), ('Maria', 20), ('Andrey', 23), ('Mark', 25)])

###############################################################

# Deque