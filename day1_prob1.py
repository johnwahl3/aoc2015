with open('day1_prob1.txt', 'r') as f:
#with open('day1_sample.txt', 'r') as f:
    instructions = f.read().strip()

# replace each instruction with a number and a comma
instructions = instructions.replace('(', '1,').replace(')', '-1,')

# split and turn to integers (drop last comma)
instructions = instructions[:-1]
instructions = [int(x) for x in instructions.split(',')]

print('final floor = ' + str(sum(instructions)))


