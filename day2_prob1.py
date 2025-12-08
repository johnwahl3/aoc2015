with open('day2_prob1.txt', 'r') as f:
#with open('day2_sample.txt', 'r') as f:
    box_sizes = [row.split('x') for row in f.read().splitlines()]

box_sides = [[int(x)*int(y),int(y)*int(z),int(x)*int(z)] for x,y,z in box_sizes]

box_areas = map(lambda box: 2*sum(box)+min(box), box_sides)

total_area = sum(box_areas)

print(str(total_area) + ' ft^2 of paper needed')
