with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

total=0 
K=12 #digits to keep

for x in lines:
    stack = []
    removeable = len(x) - K #digits we can remove

    for ch in x:
        d = int(ch)

        
        while stack and stack[-1] < d and removeable > 0:# take away smaller digits if possible
            stack.pop()
            removeable -= 1

        stack.append(d)

    
    bestDig = stack[:K] # final result is the first k digits
    bestDig = int("".join(map(str, bestDig)))

    total += bestDig

print(total)