def average_max(input):
    n = len(input)
    maxmean= -float("inf")
    for i in range(n):
        numsum = 0
        count = 0
        for j in range(n):
            if input[i][0]==input[j][0]:
                numsum += float(input[j][1])
                count += 1
        if numsum/count > maxmean:
            maxmean = int(numsum/count)
    return (maxmean)


#
#
# student = [['bob', '8'], ['ted', '10'], ['ted', '-20'], ['ttg', '-20'], ['bob', '-10']]
# print(student[1][0]==student[2][0])
# print(float(student[1][1])+float(student[2][1]))
# print(average_max(student))
# print(2 > -float("inf"))
