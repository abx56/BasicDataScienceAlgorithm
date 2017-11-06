def String_Compression(string):
    output = ""
    count = 1
    for i in range(1, len(string)):
        if string[i]!=string[i-1]:
            if count == 1:
                output += string[i-1]
            else:
                output += string[i-1]
                output += str(count)
            count = 1
        else:
            count += 1
    if count == 1:
        output += string[-1]
    else:
        output += string[-1]
        output += str(count)
    return (output)

string = "aaabaaaaccaaaaba"
print(String_Compression(string))