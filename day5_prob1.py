import re

with open('day5_prob1.txt', 'r') as f:
#with open('day5_sample.txt', 'r') as f:
    norn_list = f.read().splitlines()
    
# search through the naughty or nice list
nice = 0
for child in norn_list:
    nvowels = len(re.findall(r'[aeiou]', child))
    nrep = len(re.findall(r'([a-zA-Z])\1+', child))
    nbad = len(re.findall(r'ab|cd|pq|xy', child))
#    print(f'{nvowels}, {nrep}, {nbad}')
    nice = nice + (nvowels>2 and nrep>0 and nbad==0)
    
print(str(nice) + ' nice children')
