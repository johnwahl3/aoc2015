import re
import html

def find_path(curr_loc, curr_dist, visited, dist, all_locs, max_dist):
    #print('At ' + curr_loc + ' with distance ' + str(curr_dist))
    if all(visited.values()):
        print('All visited with distance ' + str(curr_dist))
        if curr_dist > max_dist:
            max_dist = curr_dist
        return max_dist, visited

    for loc in all_locs:
        if not visited[loc]:
            # print('Visiting ' + loc + ' from ' + curr_loc)
            visited[loc] = True
            if (curr_loc, loc) in dist:
                step_dist = dist[(curr_loc, loc)]
            else:
                step_dist = dist[(loc, curr_loc)]
            max_dist, visited = find_path(loc, curr_dist + step_dist, visited, dist, all_locs, max_dist)
            visited[loc] = False

    return max_dist, visited

with open('day9_prob1.txt', 'r') as f:
#with open('day9_sample.txt', 'r') as f:
    distances = strings = f.read().splitlines()
    
rdist = r'(\w+) to (\w+) = (\d+)'

dist = {}
all_locs = set()
for distance in distances:
    match = re.search(rdist, distance)
    frm = match[1]
    to = match[2]
    all_locs.add(frm)
    all_locs.add(to)
    dist[(frm, to)] = int(match[3])


print(all_locs)
print(dist)

visited = {loc: False for loc in all_locs}

print(visited)

max_dist = -9e99
for loc in all_locs:
    visited[loc] = True

    max_dist, visited = find_path(loc, 0, visited, dist, all_locs, max_dist)
 
    visited = {loc: False for loc in all_locs}

print(max_dist)