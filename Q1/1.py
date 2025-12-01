with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

dial = 50
ans = 0
for x in lines:
    direction = x[0]
    clicks = int(x[1:])
    temp = dial
    if direction == "R":# for the right side, just checks how many times it passes 100
        dial = (dial + clicks)%100
        ans+= (temp+clicks)//100
    else:#for the left side
        dial = (dial - clicks)%100

        if((temp-clicks)<=0):#checks if we are passing 0 because that is why we count
            offset = temp if temp > 0 else 100 #setting the offset to how many clicks we need to reach 0
            passes = 1 + (clicks - offset) // 100 #1 for the first pass and then how many more 100s we pass
            ans += passes       


print(ans)        
