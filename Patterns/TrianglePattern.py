# *
# **
# ***
# ****

def triangle_pattern1(n):
    row = 1
    while row<=n:
        col = 1
        while col <= row:
            print("*", end="")
            col+=1
        print()
        row+=1
print("\n")
triangle_pattern1(4)


# 1
# 22
# 333
# 4444

def triangle_pattern2(n):
    row = 1

    while row<=n:
        col = 1
        while col<=row:
            print(row,end="")
            col+=1
        print()

        row+=1
print("\n")
triangle_pattern2(4)

#  1
#  2 3
#  4 5 6
#  7 8 9 10

def triangle_pattern3(n):
    row = 1
    count = 1
    while row<=n:
        col = 1
        while col<=row:
            print(count,end=" ")
            col+=1
            count+=1
        print()

        row+=1
print("\n")
triangle_pattern3(4)

#  1
#  2 3
#  3 4 5
#  4 5 6 7

def triangle_pattern4(n):
    row = 1
    while row<=n:
        count = row
        col = 1
        while col<=row:
            print(count,end=" ")
            col+=1
            count+=1
        print()

        row+=1
print("\n")
triangle_pattern4(4)

#  1
#  2 3
#  3 4 5
#  4 5 6 7

def triangle_pattern5(n):
    row = 1
    while row<=n:
        col = 1
        while col<=row:
            print(row+col-1,end=" ")
            col+=1
        print()

        row+=1
print("\n")
triangle_pattern5(4)

#  1
#  2 1
#  3 2 1 
#  4 3 2 1 

def triangle_pattern5(n):
    row = 1
    while row<=n:
        col = 1
        count = 0
        while col<=row:
            print(row-count,end=" ")
            col+=1
            count+=1
        print()
        row+=1

print("\n")
triangle_pattern5(4)


#  1
#  2 1
#  3 2 1 
#  4 3 2 1 

def triangle_pattern6(n):
    row = 1
    while row<=n:
        col = 1
        while col<=row:
            print(row-col+1,end=" ")
            col+=1
        print()
        row+=1

print("\n")
triangle_pattern6(4)

