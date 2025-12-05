#This one was done for Harrison Scarfone


with open("input.txt") as f:
    grid = [line.rstrip('\n') for line in f]

rows = len(grid)#just to get number of rows and columns to use later
cols = len(grid[0])

g = [list(row) for row in grid]

neighbors = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0), (1, 1)]#all possible neighbours possible to check

ans = 0
for x in range(100):  # Repeat the process 100 times
    for r in range(rows):
        for c in range(cols):

            # Only check rolls of paper
            if g[r][c] == '@':
                arolls = 0
                for dr, dc in neighbors:
                    nr = r + dr#checks the neighbors of the rolls one by one and adds to arolls which counts all the adjacent rolls
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:#makes sure what we are checking is in bounds
                        if g[nr][nc] == '@':
                            arolls += 1

                if arolls < 4:
                    g[r][c]= '.'  # Mark as accessible
                    ans += 1


print(ans)