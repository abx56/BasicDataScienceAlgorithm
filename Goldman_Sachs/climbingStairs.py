def climbingStairs(n):
    if n == 0:
        return(0)
    elif n == 1:
        return(1)
    elif n == 2:
        return(2)
    return (climbingStairs(n-1) + climbingStairs(n-2))

def climbingStairs2(n):
    if n == 0:
        return(0)
    elif n == 1:
        return(1)
    elif n == 2:
        return(2)
    step_num=[0,1,2]
    for i in range(3, n+1):
        step_num.append(step_num[i-1]+ step_num[i-2])
    return (step_num[-1])

print(climbingStairs2(35))
