with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

total=0
grid=[]

for line in lines[:-1]:
    nums = list(map(int, line.split()))
    grid.append(nums)

operation = lines[-1].split()


for c in range(len(grid[0])):
    op = operation[c]
    nums = [grid[r][c] for r in range(len(grid))] 
    result = 0
    if op == '+':
        result = sum(nums)
    elif op == '*':
        result = 1
        for n in nums:
            result *= n
    total += result        



print(total)