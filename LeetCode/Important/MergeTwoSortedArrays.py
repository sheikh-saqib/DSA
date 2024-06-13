def merge(nums1,nums2):
    l1=len(nums1)-1
    l2=len(nums2)-1
    arr3 = []
    i = 0
    j = 0

    while i<=l1 and j<=l2:
        if nums1[i]<nums2[j]:
            arr3.append(nums1[i])
            i+=1
        else:
            arr3.append(nums2[j])
            j+=1

        
    
    while i<=l1:
        arr3.append(nums1[i])
        i+=1


    while j<=l2:
        arr3.append(nums2[j])
        j+=1

    return arr3






nums1 = [1,2,3]
nums2 = [4,5,6]

print(merge(nums1,nums2))