def reverseWords(s):
    splitstr = s.split(" ")
    while '' in splitstr:
        splitstr.remove('')
    n = len(splitstr)
    if n == 0:
        return ('')
    elif n == 1:
        return (splitstr[0])
    newstring = ''
    for index in range(n - 1):
        newstring += splitstr[n - index - 1]
        newstring += " "
    newstring += splitstr[0]
    return (newstring)

string = "   a   b "
print(reverseWords(string))

################################
def reverseSentence(s):
    splitstr = s.split(" ")
    n = len(splitstr)
    for i in range(n):
        str = ''
        ni=len(splitstr[i])
        for index in range(ni):
            str += splitstr[i][ni - index - 1]
        splitstr[i] = str
    output = ' '.join(splitstr)
    return (output)

string = "hello world"
print(reverseSentence(string))