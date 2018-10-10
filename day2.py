# Intializing some variables
value = []
checksum = 0
# Reading in a text file of out input
with open("input.txt") as f:
    for line in f:
        value.append(line)

# Part 1 Day 2
# Calculate the checksm by finding the sum of the differences between the largest and smallest value per row
for row in value:
    temp = []
    row_difference = 0
    temp = row.split()
    temp = list(map(int, temp))
    row_difference = max(temp) - min(temp)
    checksum += row_difference
print(checksum)

# Part 2 Day 2
# Calculate the checksum by finding the the 2 numbers in the row that divide evenly and summing each
checksum = 0
for row in value:
    temp = []
    temp = row.split()
    temp = list(map(int, temp))
    for i in temp:
        for j in temp:
            if(j%i==0 and (j != i)):
                checksum += int(j/i)
print(checksum)
