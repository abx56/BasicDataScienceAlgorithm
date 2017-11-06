def isAnagram(s, t):
    NO_OF_CHARS = 256
    count_s = [0] * NO_OF_CHARS
    count_t = [0] * NO_OF_CHARS
    for i in s:
        if ord(i)<=122 and ord(i) >= 65:
            count_s[ord(i)] += 1
    for i in t:
        if ord(i)<=122 and ord(i) >= 65:
            count_t[ord(i)] += 1
    if count_t==count_s:
        return(True)
    else:
        return(False)

s = "anagrma"
t = "nagaram"
print(isAnagram(s,t))

print(chr(56))
print(ord('A'),ord('a'),ord('Z'),ord('z'))


print(ord('I'),ord(' '),ord('l'),ord('o'),ord('v'),ord('e'),ord(' '),ord('y'),ord('o'),ord('u'))
print(chr(73),chr(32),chr(108),chr(111),chr(118),chr(101),chr(32),chr(121),chr(111),chr(117))
print(ord('A'),ord('z'))


