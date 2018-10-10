import collections
value = []

with open("input.txt") as f:
    for line in f:
        value.append(line)

total = 0

#Part 1
for spot in value:
    temp = []
    temp = spot.split()
    test = set(temp)
    print(temp)
    if(len(temp) == len(test)):
        total+=1
print(total)

