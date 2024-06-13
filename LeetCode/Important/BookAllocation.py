def allocate_books(arr,m):
    s= 0
    e = sum(arr)
    ans = -1
    while s<=e:
        mid = (s+e)//2
        if(is_possible_solution(arr,m,mid)):
            ans = mid
            e = mid-1
        else:
            s = mid+1
    return ans



def is_possible_solution(arr,m,mid):
    studentCount =1
    pagesSum = 0
    
    for book in arr:
        if pagesSum + book <=mid:
            pagesSum+=book
        else:
            # going to next student
            studentCount+=1
            #check if case not possible
            if(studentCount>m or book>mid):
                return False
            else:
                # allocate current book to next student 
                pagesSum = book
    return True

arr = [10,20,30,40]

m = 2

print(allocate_books(arr,m))