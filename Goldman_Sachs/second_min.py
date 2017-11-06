def second_min(num):
    n= len(num)
    if n < 2:
        return -1
    if num[0] > num[1]:
        min = num[1]
        second = num[0]
    else:
        min = num[0]
        second = num[1]
    for i in range(2,n):
        if num[i] < min:
            second = min
            min = num[i]
        elif num[i] < second:
            second = num[i]
    return(second)




vec1=[5,6,2,6,9,2,65,65,95,6,2,1,26,-2.1,-6,62,-2,1]
print(second_min(vec1))