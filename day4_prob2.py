import hashlib as hl

#with open('day4_prob1.txt', 'r') as f:
#with open('day4_sample.txt', 'r') as f:
#    moves = f.read().strip()

#secret = 'abcdef'
secret = 'ckczppom'

h = ''
i = -1
while not h.startswith('000000'):
    i = i + 1
    h = hl.md5((secret + str(i)).encode('utf-8')).hexdigest()
    
print(str(i) + ' is the first number with hash ' + h)
