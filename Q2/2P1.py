import re

with open("input.txt") as f:
    lines = f.read()


parts = lines.split(",")

ans=0

for x in parts:
    rng = x.split("-")
    for i in range(int(rng[0]),int(rng[1])+1):
        midpoint = len(str(i))//2
        si = str(i)
        if(si[:midpoint]==si[midpoint:]):
            ans+= i

print(ans)