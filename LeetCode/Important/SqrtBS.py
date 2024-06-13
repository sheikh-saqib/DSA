def sqrt_BS_int(n):
    s = 0
    e = n
    mid = 0
    ans = -1
    while s<=e:
        mid = (s+e)//2
        square = mid*mid
        if square == n:
            return mid
        
        elif square > n:
            e = mid-1

        else:
            ans=mid
            s = mid+1
        
    return ans


def sqrt_BS_decimal(ans_int,precision,n):
    factor = 1.0
    ans = ans_int
    i=0
    while i<precision:
        factor = factor/10 #get 0.1
        j=ans
        while j*j<n:
            ans = j
            j+=factor
        i+=1
    return round(ans,precision)



ans_int = sqrt_BS_int(37)
print(sqrt_BS_decimal(ans_int,3,37))



    
