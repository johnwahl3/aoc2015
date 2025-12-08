with open('day1_prob1.txt', 'r') as f:
#with open('day1_sample.txt', 'r') as f:
    instructions = f.read().strip()

# replace each instruction with a number and a comma
instructions = instructions.replace('(', '1,').replace(')', '-1,')

# split and turn to integers (drop last comma)
instructions = instructions[:-1]
instructions = [int(x) for x in instructions.split(',')]

floor = 0
i = 0
while floor>=0:
    floor = floor + instructions[i]
    i = i + 1
    
print('Enter basement at instruction #' + str(i))

