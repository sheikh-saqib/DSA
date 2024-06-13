def linear_search(arr,key):

    for i in range(0,len(arr)):
        if(arr[i] == key):
            return True
    return False 




arr = [1, 3, -5, 3, 5, 1]
key =1 
print(linear_search(arr,key))



