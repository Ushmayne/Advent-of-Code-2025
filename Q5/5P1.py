with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

ranges = []
singles = []

for line in lines:
    if line.strip() == "":
        continue  
    if "-" in line:
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    else:
        singles.append(int(line))

count = 0

for x in singles:
    for start, end in ranges:
        if start <= x <= end:
            count+=1
            break
    
print(count)

