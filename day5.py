# Day 5 of Advent of Code
# Example from adventofcode.com

# For example, consider the following list of jump offsets:

# 0
# 3
# 0
# 1
# -3

# Positive jumps ("forward") move downward; negative jumps move upward. For legibility in this example,
# these offset values will be written all on one line, with the current instruction marked in parentheses.
# The following steps would be taken before an exit is found:

# (0) 3  0  1  -3  - before we have taken any steps.
# (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). The instruction is incremented by 1
# 2 (3) 0  1  -3  - step forward because of the instruction we just modified. The instruction is incremented by 1, to 2
# 2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
# 2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
# 2  5  0  1  -2  - jump 4 steps forward, escaping the maze.

# Calculate part 1 as per instructions above
def part1(l):
    youAreHere = 0
    time = 0
    while (youAreHere < len(l)):
        temp = youAreHere
        youAreHere += l[youAreHere]
        l[temp] += 1
        time += 1
    print(time)
    return;

# Calculate part 2, with a slight change to the rules:
# If the value is 3 or greater, decrement the instruction by 1
def part2(l):
    youAreHere = 0
    time = 0
    while (youAreHere < len(l)):
        temp = youAreHere
        youAreHere += l[youAreHere]
        if (l[temp] >= 3):
            l[temp] -= 1
        else:
            l[temp] += 1
        time += 1
    print(time)
    return;


# Main
if __name__ == "__main__":
    # Declaring maze variables
    maze1 = []
    maze2 = []
    # Reading in text file for input
    with open("input.txt") as f:
        for line in f:
            maze1.append(line)
    # Creating the mazes to be ints and not strings
    maze1 = list(map(int, maze1))
    maze2 = list(maze1)
    # Running the calculations
    part1(maze1)
    part2(maze2)
