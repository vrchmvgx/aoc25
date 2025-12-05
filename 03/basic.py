filename = 'input.txt'
with open(filename, 'r') as handle:
    banks = []
    for line in handle:
        banks.append([int(char) for char in line if char != '\n'])

total = 0
for bank in banks:
    bank_length = len(bank)
    if bank_length < 2:
        if bank_length == 1:
            total += bank[0]
        continue
    highest = 0
    second = 0
    for idx, i in enumerate(bank):
        if idx < (bank_length - 1):
            if i > highest:
                highest = i
                second = 0
                continue
        if i > second:
            second = i
    total += highest * 10 + second
print(str(total))