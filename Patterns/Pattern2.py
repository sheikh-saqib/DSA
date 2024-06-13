# 1 2 3 4 
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

def numeric_pattern1(n):
    row = 1

    while row<=n:
        col = 1
        while col<=n:
            print(col,end=" ")
            col+=1
        print()
        row+=1


numeric_pattern1(4)


# 3 2 1
# 3 2 1
# 3 2 1

def numeric_pattern2(n):
    row =1
    while row<=n:
        col = 1
        while col<=n:
            print(n-col+1,end=" ")
            col+=1

        print()
        row +=1
print("\n")
numeric_pattern2(3)

# 1 2 3
# 4 5 6
# 7 8 9

def numeric_pattern3(n):
    row =1
    count = 1
    while row<=n:
        col = 1
        while col<=n:
            print(count,end=" ")
            col+=1
            count+=1

        print()
        row +=1
print("\n")
numeric_pattern3(3)