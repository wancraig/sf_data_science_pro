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
from collections import deque

dq = deque()
print(dq) # deque([])

# Imagine a waiting line to Support 

clients = deque()

clients.append("Ivanov")
clients.append("Petrov")
clients.append("Smirnov")
clients.append("Tikhomirova")

print(clients) # deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhomirova'])
print(clients[2]) # Smirnov

first_client = clients.popleft() # We extract first client from deque
second_client = clients.popleft() # We extract second client from deque

print("First client: ", first_client)
print("Second client: ", second_client)
print (clients) # deque(['Smirnov', 'Tikhomirova']) the ones left in the que

# Imagine we have a VIP client that has to be served first, before the rest of que

clients.appendleft("Vip-client")
print (clients) # deque(['Vip-client', 'Smirnov', 'Tikhomirova'])

tired_client = clients.pop() # deletes from right of que
print (clients) # deque(['Vip-client', 'Smirnov'])

# In brackets we can add list
shop = deque ([1,2,3,4,5])
print(shop) # deque([1, 2, 3, 4, 5])

shop.extend([11,12,13,14,15,16,17])
print(shop) # deque([1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17])

shop.extendleft([11,12,13,14,15,16,17])
print(shop) # deque([17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 17])

# we can create deque with max lenght

limited = deque (maxlen = 3)
print(limited) # deque([], maxlen=3)

limited_from_list = deque([1,2,3,4,5,6,7], maxlen = 3)
print (limited_from_list) # deque([5, 6, 7], maxlen=3); first elements are getting erased


# Imagine we have a list of temp for July
temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]

# Now we want to get a Moving Average for 7 days

days = deque(maxlen = 7)

for temp in temps:
    # adding temp into que
    days.append(temp)
    # if que length = 7, print MA for 7 days
    if len(days) == days.maxlen:
        print(round(sum(days)/len(days),2), end=" ; ")
    
  # 20.77 ; 21.27 ; 22.16 ; 23.3 ; 24.44 ; 24.94 ; 25.56 ; 26.2 ; 25.97 ; 25.94 ; 25.57 ; 25.1 ; 
  # 24.81 ; 24.21 ; 23.23 ; 22.57 ; 21.41 ; 20.4 ; 19.6 ; 19.1 ; 19.04 ; 18.96 ; 19.44 ; 20.01 ; 20.67 ;

# we can reverse decks
print("")
dq = deque([1,2,3,4,5])
dq.reverse()
print(dq) # deque([5, 4, 3, 2, 1])

# rotate transfers elements from end to begining
dq = deque([1,2,3,4,5])
dq.rotate(2) # if negative number is used, we put them from beg to end
print(dq) # deque([4, 5, 1, 2, 3]), last two elements were put into begining

# deques have the same functions as lists
dq = deque([1,2,3,4,5,4,4,4,4,3,1])
print(dq.index(4)) # 3 rd place we find the first entrance of 4 in the deck
print(dq.count(4)) # 5 total amount we meet 4 in deque

dq.clear() # finally clear the deck

##################################################
# Practice
##################################################

# OrderDict
temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

def check(temps):
   return print(OrderedDict(sorted(temps, key = lambda x: -x[1])))

check(temps)

# Deque
# Напишите функцию brackets(line), которая определяет, является ли последовательность из круглых скобок правильной.
brackets1 = ("(","(",")")

def brackets(line):
    stack = deque()
    for i in line:
      if i == "(":
        stack.append(i)
      elif i == ")":
        if len(stack) == 0:
          return False
        stack.pop()
    if len(stack) == 0:
      return True
    return False
      
print(brackets(brackets1))
      
      