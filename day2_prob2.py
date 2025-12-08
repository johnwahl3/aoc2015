import math

with open('day2_prob1.txt', 'r') as f:
#with open('day2_sample.txt', 'r') as f:
    box_sizes = [row.split('x') for row in f.read().splitlines()]

box_sides = [[int(x),int(y),int(z)] for x,y,z in box_sizes]

box_rib = map(lambda box: 2*(sum(box)-max(box)) + math.prod(box), box_sides)

total_len = sum(box_rib)

print(str(total_len) + ' ft of ribbon')
