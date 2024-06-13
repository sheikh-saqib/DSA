def reverseWords(strArr):
    s = 0
    e = 0
    for i in range(0,len(strArr)):
        if strArr[i] == ' ' or i ==len(strArr)-1:
            e = i - 1 if strArr[i] == ' ' else i
            while s<=e:
                strArr[s],strArr[e] = strArr[e],strArr[s]
                s+=1 
                e-=1
            s=i+1
    return strArr










strArr = ['m','y',' ','n','a','m','e',' ','i','s']

print(reverseWords(strArr))