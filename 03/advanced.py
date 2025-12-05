filename = 'input.txt'
with open(filename, 'r') as handle:
    banks = []
    for line in handle:
        banks.append([int(char) for char in line.strip()])

def do_step(bank, ordinal):
    if ordinal == 1:
        return max(bank)
    options = len(bank) - ordinal + 1
    if options < 1:
        return do_step(bank, ordinal - 1)
    highest = 0
    highest_i = 0
    for idx, val in enumerate(bank[:options]):
        if val > highest:
            highest = val
            highest_i = idx
    return highest * (10**(ordinal-1)) + do_step(bank[(highest_i+1):], ordinal - 1)

total = 0
for bank in banks:
    outcome = do_step(bank, 12)
    total += outcome
print(str(total))