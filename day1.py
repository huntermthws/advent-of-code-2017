total_sum = 0
input = open("input.txt", "r").read()

for i in range(0, len(input)):
    if input[i]==input[(i+1) % (len(input))]:
        total_sum += int(input[i])
print(total_sum)

total_sum = 0
offset = int(len(input)/2)
for i in range(0, len(input)):
    if input[i]==input[(i+offset) % (len(input))]:
        total_sum += int(input[i])
print(total_sum)
