import re
import operator as op

def parse_instructions(instructions):
    # first assign all the wires to properties
    for instruction in instructions:
        match_assign = re.search(r_assign, instruction)
        match_assign_string = re.search(r_assign_string, instruction)
        match_op = re.search(r_op, instruction)
        match_not = re.search(r_not, instruction)
        if match_not:
            wires[match_not[2]] = (lambda x: ~(int(x) & 0xFFFF), match_not[1])
        elif match_assign:
            wires[match_assign[2]] = int(match_assign[1]) & 0xFFFF
        elif match_assign_string:
            wires[match_assign_string[2]] = (lambda x: int(x) & 0xFFFF, match_assign_string[1])
        elif match_op:
            if match_op[2]=='OR':
                oper = lambda x,y: op.__or__(x,y) & 0xFFFF
                try:
                    val1 = int(match_op[1])
                except:
                    val1 = match_op[1]
                try:   
                    val2 = int(match_op[3])
                except:
                    val2 = match_op[3]
            elif match_op[2]=='AND':
                oper = lambda x,y: op.__and__(x,y) & 0xFFFF
                try:
                    val1 = int(match_op[1])
                except:
                    val1 = match_op[1]
                try:   
                    val2 = int(match_op[3])
                except:
                    val2 = match_op[3]
            elif match_op[2]=='LSHIFT':
                oper = lambda x,y: op.__lshift__(x,y) & 0xFFFF
                val1 = match_op[1]
                val2 = int(match_op[3])
            elif match_op[2]=='RSHIFT':
                oper = lambda x,y: op.__rshift__(x,y) & 0xFFFF
                val1 = match_op[1]
                val2 = int(match_op[3])
            else:
                print('Should not happen!!!!')
                print(instruction)
            wires[match_op[4]] = (oper, val1, val2)
    return wires

def get_value(wires, target):
    val = wires[target]
    if type(val) is int:
        return val
    elif type(val) is tuple:
        if len(val) == 3:
            func, arg1, arg2 = val
            if type(arg1) is str:
                arg1 = get_value(wires, arg1)
            if type(arg2) is str:
                arg2 = get_value(wires, arg2)
            result = func(arg1, arg2) & 0xFFFF
            wires[target] = result
            return result
        else:
            func, arg = val
            if type(arg) is str:
                arg = get_value(wires, arg)
            result = func(arg) & 0xFFFF
            wires[target] = result
            return result
    else:
        print('Should not happen!!!!')
        print(target)
        return None


with open('day7_prob1.txt', 'r') as f:
#with open('day7_sample.txt', 'r') as f:
    instructions = f.read().splitlines()

r_assign = r'^(\d+) -> ([a-z]+)$'
r_assign_string = r'^([a-z\d]+) -> ([a-z]+)$'
r_op = r'^([a-z\d]+) ([A-Z]+) ([a-z\d]+) -> ([a-z]+)$'
r_not = r'^NOT ([a-z]+) -> ([a-z]+)$'

# store wire states
wires = {}

wires = parse_instructions(instructions)

# print(wires)

# now recursively fill in all the wires
# wire_loop = [wire for wire in wires]
# for wire in wire_loop:
#     if type(wire) is not int:
#         wires[wire] = get_value(wires, wire)

print('For part 1:')
print(str(get_value(wires, 'a')) + ' value on wire a')

save_a = wires['a']

wires = parse_instructions(instructions)

wires['b'] = save_a

print('For part 2:')
print(str(get_value(wires,'a')) + ' value on wire a')
