
def getMax(arr):
    max_val = arr[0]
    for i in range(1,len(arr)):
        if(arr[i] > max_val):
            max = arr[i]

    print(max)

def getMin(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if(arr[i] < min):
            min = arr[i]

    print(min)

size = 100
arr=[]
for i in range(1,size+1):
    arr.append(i)

getMax(arr)
getMin(arr)

print(max(arr))
print(min(arr))

