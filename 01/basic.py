filename = 'input.txt'
with open(filename, 'r') as handle:
    rotations = []
    for line in handle:
        prefix = line[0]
        if prefix == 'L':
            direction = -1
        else:
            direction = 1
        rotations.append(direction * int(line[1:-1]))

hits = 0
current = 50
for rotation in rotations:
    if rotation == 0:
        continue
    current = (current + rotation) % 100
    if current == 0:
        progress = []
        hits += 1

print(str(hits))