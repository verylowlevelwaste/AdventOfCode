import time

input = open('input.txt', 'r+')
inputline = input.readlines()

directions = inputline[0]

floor = 0
int_count = 0
position = 0
trigger_check = 0

for i in directions:

    if i == '(':
        floor += 1

    elif i == ')':
        floor -= 1

    if floor == -1 and trigger_check == 0:
        position = int_count + 1
        trigger_check = 1

    int_count += 1

print(floor)
print(position)