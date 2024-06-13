#       *
#     * *  
#   * * *
# * * * *

def pattern1(n):
    row = 1
    while row <= n:
        spaces = n - row
        while spaces !=0:
            print(" ",end="")
            spaces-=1
        col = 1
        while col<=row:
            print("*",end="")
            col +=1
        row+=1
        print()

#pattern1(4)


# * * * *
# * * *  
# * *
# * 

def pattern2(n):
    row = 1 
    while row<=n:
        col=1
        while col<= n-row+1:
            print("*",end="")
            col+=1
        print()
        row+=1
   
print("\n")
#pattern2(4)


# * * * *
#   * * *  
#     * *
#       * 

def pattern3(n):
    row = 1 
    while row<=n:
        spaces = 1
        col=1

        while spaces <=row-1:
            print(" ",end="")
            spaces+=1

        while col<= n-row+1:
            print("*",end="")
            col+=1

        print()
        row+=1
   
print("\n")
#pattern3(4)


# 1 1 1 1
#   2 2 2  
#     3 3
#       4 

def pattern4(n):
    row = 1 
    while row<=n:
        spaces = 1
        col=1

        while spaces <=row-1:
            print(" ",end="")
            spaces+=1

        while col<= n-row+1:
            print(row,end="")
            col+=1

        print()
        row+=1
   
print("\n")
#pattern4(4)


#___1
#__121
#_12321
#1234321


def pattern5(n):
    row = 1
    while row<=n:
        spaces = 1
        while spaces<=n-row:
            print(" ",end="")
            spaces+=1

        col = 1
        while col<=row:
            print(col,end="")
            col+=1

        start = row - 1
        while start>0:
            print(start,end="")
            start-=1

        print()
        row+=1
    
print("\n")
pattern5(4)


# 1 2 3 4 5 5 4 3 2 1
# 1 2 3 4 * * 4 3 2 1
# 1 2 3 * * * * 3 2 1 
# 1 2 * * * * * * 2 1 
# 1 * * * * * * * * 1
    

    
def pattern6(n):
    row = 1
    while row<=n:
        col = 1
        while col<=n-row+1:
            print(col,end="")
            col+=1

        start = row-1
        while start >0:
            print("**",end="")
            start-=1

        start = n - row +1
        while start!=0:
            print(start,end="")
            start-=1

        row+=1
        print()

print("\n")

pattern6(5)



 

