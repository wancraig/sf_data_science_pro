from collections import Counter

# create empty object Counter
c = Counter()

# for example we want to count the number of red cars that pass by
c["red"] += 1
print (c)

# next example, we have a list of car and colors passed by
cars = ["red","blue","black","black","black","red","blue","red","white"]

for car in cars:
    c[car] += 1

print (c) # pay attention, that we have result of 4 red cars, because of the 1st example in this file

# can we do it easier without for loop? yes

c1 = Counter(cars) # we pass the variable list countent directly to our counter variable
print (c1) # Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})

# if we want to find out, how many times existing object was counted
print(c1["black"]) # 3
print (c1["purple"]) # 0, we get no errors, because it means that purple was met and counted 0 times

# if we want to count the amount of all cars
print (sum(c1.values())) # 9


# what if we have two different lists

cars_vienna = ["red","blue","black","black","black","red","blue","red","white"]
cars_graz = ["blue","blue","black","black","white","purple","purple","red","white"]

counter_vienna = Counter(cars_vienna)
counter_graz = Counter(cars_graz)

# we cant add both lists
print (counter_vienna + counter_graz)
# result Counter({'black': 5, 'red': 4, 'blue': 4, 'white': 3, 'purple': 2})

# for subtraction we need additional function .subtract
counter_vienna.subtract(counter_graz)
print (counter_vienna)

# NB! If we just subtract two counters, we will get result without negative numbers (if any)

# we can also get a list in a-bet order of all elements
print(*counter_vienna.elements())

# we can get a list of unique items in the counter
print(list(counter_graz)) # ['blue', 'black', 'white', 'purple', 'red']

# we can transform our counter into dict
print (dict(counter_graz))

# most common elements in the list
print(counter_graz.most_common(2))

# last thing what we can do is to clear the counter
counter_vienna.clear()
print(counter_vienna) # Counter()

#####################################################

# create a list with tuple, students with their group number
students = [("Ivanov",1),("Smirnov",4),("Petrov",3),("Kuznetsova",1),("Nikitina",2),("Markov",3),("Pavlov",2),]

# how do we solve the issue by standard way to get a list as follows: {1: ["Ivanov","Kuznetsova"]....}
groups = dict()

for student, group in students:
    # NB! Check if the group is already in dict. Otherwise we get KeyError
    if group not in groups:
        # if group is not in dict, create empty list
        groups[group] = list()
    groups[group].append(student)

print(groups)
# {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']}

# Easier way? Use defaultdict
from collections import defaultdict

groups = defaultdict(list)

for student, group in students:
    groups[group].append(student)
    
print (groups)
# defaultdict(<class 'list'>, {1: ['Ivanov', 'Kuznetsova'], 4: ['Smirnov'], 
# 3: ['Petrov', 'Markov'], 2: ['Nikitina', 'Pavlov']})


# now that we got our dict, we can use it as usual
# for ex we can get the value by key

print(groups[3]) # ['Petrov', 'Markov']


# TASK 2.5 using len to count unique cards in clients
#from collections import Counter
#from hidden import *
#client = Counter (clients)

#print(client.most_common(2))

#print(len(list(client)))