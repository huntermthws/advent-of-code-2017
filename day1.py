#reading in input
data = open('input.txt', 'r').read().strip()

# Part 1
# Needed to account for wrap around. % len(data) resets the index back to 0 once reaching the end.
total_sum = 0
for i in range(len(data)):
    if(data[i] == data[(i+1) % len(data)]):
        total_sum += int(data[i])
print(total_sum)

#Part 2
half = int(len(data)/2)
total_sum = 0
for i in range(len(data)):
    if(data[i] == data[(i+half) % len(data)]):
        total_sum += int(data[i])
print(total_sum)


