import re
import operator as op

with open('day6_prob1.txt', 'r') as f:
#with open('day6_sample.txt', 'r') as f:
    instructions = f.read().splitlines()
    
# search through the naughty or nice list
lights = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in instructions:
    match = re.search(r'.*?(\d+),(\d+) through (\d+),(\d+)', instruction)
    xrange = [int(match[1]), int(match[3])+1]
    yrange = [int(match[2]), int(match[4])+1]
    if 'turn on' in instruction:
        oper = op.add
        val = 1
    elif 'turn off' in instruction:
        oper = op.add
        val = -1
    elif 'toggle' in instruction:
        oper = op.add
        val = 2

    for row in range(yrange[0],yrange[1]):
        lights[row][xrange[0]:xrange[1]] = [max(0,oper(x,val)) for x in lights[row][xrange[0]:xrange[1]]]

total = sum(sum(row) for row in lights)

print(str(total) + ' total brightness')
