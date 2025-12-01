with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f]

dial = 50
ans = 0
for x in lines:
    direction = x[0]
    clicks = int(x[1:])
    temp = dial
    if direction == "R":
        dial = (dial + clicks)%100
        ans+= (temp+clicks)//100
    else:
        dial = (dial - clicks)%100

        if((temp-clicks)<=0):
            offset = temp if temp > 0 else 100
            passes = 1 + (clicks - offset) // 100
            ans += passes       
    

    


print(ans)        
