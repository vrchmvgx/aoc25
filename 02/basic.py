import re

filename = 'input.txt'
with open(filename, 'r') as handle:
    rotations = []
    regeng = re.compile(r'^(.+)\1$')
    total = 0
    for line in handle:
        split = line.strip().split(',')
        for id_range in split:
            start, stop = [int(node) for node in id_range.split('-')]
            for i in range(stop - start + 1):
                curr = start + i
                curr_str = str(curr)
                if regeng.match(curr_str):
                    total += curr
print(str(total))