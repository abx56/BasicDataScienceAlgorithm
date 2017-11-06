def firstUniqChar(string):
    NO_OF_CHARS = 256
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)] += 1
    for i in string:
        if count[ord(i)]==1:
            return (i)
    return(-1)

string = "geeksforgeeks"
print(firstUniqChar(string))
