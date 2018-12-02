# Program to reverse a string with special characters
# To reverse the string without affecting special characters

# Reverses the list of characters without affecting special characters
def toReverse(l):
    loop1=0;
    loop2=-1
    while loop1 - loop2 <= len(l):
        if not ((ord(l[loop1]) >= 65 and ord(l[loop1]) <= 90) or (ord(l[loop1]) >= 97 and ord(l[loop1]) <= 122)):
            loop1 = loop1 + 1

        elif not ((ord(l[loop2]) >= 65 and ord(l[loop2]) <= 90) or (ord(l[loop2]) >= 97 and ord(l[loop2]) <= 122)):
            loop2 = loop2 - 1

        else:
            var = l[loop1]
            l[loop1] = l[loop2]
            l[loop2] = var
            loop2 = loop2 - 1
            loop1 = loop1 + 1
    return ''.join(l)

# Converts the string to list of characters
def toList(inpget):
    return list(str(inpget))

# Driver Code
inp=input("Input:  ")
var=toList(inp)
print("Output:",toReverse(var))
