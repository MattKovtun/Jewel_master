input_dat = open("10676.dat", encoding='WINDOWS-1251')
data = []

space = 1
for line in input_dat:
    if len(line) == 1:
        print("he")
        space = 0
    space += 1
    if space == 3:
        line = line.strip()
        data.append(line)

print(data)
