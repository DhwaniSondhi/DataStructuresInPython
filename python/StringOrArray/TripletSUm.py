def tripletSum(l,sum):
    loop1=0
    count=0
    while loop1<len(l):
        loop2=loop1+1
        while loop2<len(l):
            loop3=loop2+1
            while loop3<len(l):
                if (l[loop1]+l[loop2]+l[loop3])<sum:
                    count=count+1
                loop3=loop3+1
            loop2=loop2+1
        loop1=loop1+1
    return count



def convertListOrSum(l):
    varReturn=list()
    if '[' in l:
        l=l.replace("[","")
        l=l.replace("]","")
        l=l.split(',')
        for var in l:
            varReturn.append(int(var))
        return varReturn
    else:
       return int(l)


#Driver Code
inpList=input("Enter the list: ")
inpList=convertListOrSum(inpList)
inpSum=input("Enter the sum: ")
inpSum=convertListOrSum(inpSum)
print("Output: ",tripletSum(inpList,inpSum))


