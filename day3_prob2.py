from itertools import count

with open('day3_prob1.txt', 'r') as f:
#with open('day3_sample.txt', 'r') as f:
    moves = f.read().strip()

# replace each instruction with a number and a comma
moves = moves.replace('^', '0|1,').replace('v', '0|-1,').replace('>', '1|0,').replace('<', '-1|0,')


# split and turn to integers (drop last comma)
moves = moves[:-1]
moves = [x.split('|') for x in moves.split(',')]
moves = [[int(x) for x in y] for y in moves]

moves_iter = iter(moves)

locs_s = [[0,0]]
locs_r = [[0,0]]
for i, (move_s, move_r) in zip(count(), zip(moves_iter, moves_iter)):
    locs_s.append([sum(x) for x in zip(move_s, locs_s[i])])
    locs_r.append([sum(x) for x in zip(move_r, locs_r[i])])

unique_locs = set(map(tuple, locs_s+locs_r))

print(str(len(unique_locs)) + ' unique houses')


