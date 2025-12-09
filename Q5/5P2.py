with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

ranges = []
ans=[]

for line in lines:
    if line.strip() == "":
        continue  
    if "-" in line:
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
        
ranges = sorted(ranges)#sorts the ranges using start value

for start, end in ranges:
    if not ans or int(start) > ans[-1][1]:#checks if the current range overlaps with the last range in ans
        ans.append([int(start), int(end)])
    else:
        ans[-1][1] = max(ans[-1][1], int(end))#merges overlapping ranges by updating the end value of the last range in ans



sum = 0

for start, end in ans:        #calculates the total length covered by the merged ranges for the answer   
    sum+= end - start+1

print(sum)



