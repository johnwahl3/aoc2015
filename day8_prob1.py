import re
import html

with open('day8_prob1.txt', 'rb') as f:
#with open('day8_sample.txt', 'rb') as f:
    bstrings = f.read().splitlines()

len_raw = 0
len_mem = 0
for bs in bstrings:
    len_raw += len(bs)
    len_mem += len(bs.decode('unicode_escape')[1:-1])
    
print('For Part 1:')
print('Difference:', len_raw - len_mem)


len_raw2 = 0
len_mem2 = 0
for bs in bstrings:
    len_mem2 += len(bs)
    len_raw2 += len(bs.replace(b'\\', b'\\\\').replace(b'"', b'\\"'))+2
    
print('For Part 2:')
print('Difference:', len_raw2 - len_mem2)

