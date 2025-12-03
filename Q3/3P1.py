with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

total = 0

for x in lines:
    best = 0
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            a = int(x[i])
            b = int(x[j])
            num = a*10 + b
            if num > best:
                best = num

    total += best

print(total)
    
          