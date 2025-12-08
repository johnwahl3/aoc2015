from operator import add

with open('day3_prob1.txt', 'r') as f:
#with open('day3_sample.txt', 'r') as f:
    moves = f.read().strip()

# replace each instruction with a number and a comma
moves = moves.replace('^', '0|1,').replace('v', '0|-1,').replace('>', '1|0,').replace('<', '-1|0,')


# split and turn to integers (drop last comma)
moves = moves[:-1]
moves = [x.split('|') for x in moves.split(',')]
moves = [[int(x) for x in y] for y in moves]

locs = [[0,0]]
for i, move in enumerate(moves):
    locs.append([sum(x) for x in zip(move, locs[i])])


unique_locs = set(map(tuple, locs))

print(str(len(unique_locs)) + ' unique houses')


