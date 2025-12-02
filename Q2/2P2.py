import re


def findRepeatingPattern(num_str):
    n = len(num_str) #gets length of string
    for length in range(1, n // 2 + 1):#checks for all possible lengths of patterns, max it can be is half the length of string  
        pattern = num_str[:length]#gets tje portion of string to check
        if num_str == pattern * (n // length):#the pattern repeats it would have to be n//length times to complete
            return True
    return False


with open("input.txt") as f:
    lines = f.read()


parts = lines.split(",")

ans=0

for x in parts:
    rng = x.split("-")
    for i in range(int(rng[0]),int(rng[1])+1):
        if(findRepeatingPattern(str(i))):#check if it has a repeat
            ans+=i#adds tp answer if it has repeats 

        

print(ans)


