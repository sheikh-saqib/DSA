def agressive_cows(arr,k):
    
    def is_possible_solution(arr,k,mid):
        cow_count = 1
        last_pos = arr[0]

        for pos in arr:
            # moving postions of next cow
            if pos - last_pos >= mid:
                cow_count+=1
                if cow_count==k:
                    return True
                last_pos = pos

        return False

    arr.sort()
    s = 0
    e = max(arr)
    ans = -1
    while s<=e:
        mid =(s+e)//2
        if is_possible_solution(arr,k,mid):
            ans = mid
            #go to right part because we need the largest distance
            s = mid+1
        else:
            e = mid - 1

    return ans


            