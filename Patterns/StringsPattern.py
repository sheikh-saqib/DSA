# A A A
# B B B 
# C C C 

def pattern1(n):
    row = 1
    while row<= n:
        col = 1
        while col<=n:
            print(chr(ord('A')+ row -1),end=" ")
            col+=1
        print()
        row+=1
print("\n")
pattern1(3)


# A B C
# A B C
# A B C

def pattern2(n):
    row = 1
    while row<= n:
        col = 1
        while col<=n:
            print(chr(ord('A')+ col -1),end=" ")
            col+=1
        print()
        row+=1
print("\n")
pattern2(3)



# A B C
# D E F
# G H I

def pattern3(n):
    row = 1
    count=0
    while row<= n:
        col = 1
        while col<=n:
            print(chr(ord('A')+count),end=" ")
            col+=1
            count+=1
        print()
        row+=1
print("\n")
pattern3(3)


# A B C
# B C D 
# C D E

def pattern4(n):
    row =1
    while row<=n:
        col=1
        while col<=n:
            print(chr(ord('A')+row+col-2),end=" ")
            col+=1
        row+=1
        print()

print("\n")

pattern4(3)


# A
# B B 
# C C C

def pattern5(n):
    row =1
    while row<=n:
        col=1
        while col<=row:
            print(chr(ord('A')+row-1),end=" ")
            col+=1
        row+=1
        print()

print("\n")

pattern5(3)


# A
# B C 
# D E F
# G H I J

def pattern6(n):
    row =1
    start = 'A'
    while row<=n:
        col=1
        while col<=row:
            print(chr(ord(start)),end=" ")
            col+=1
            start=chr(ord(start)+1)
        row+=1
        print()

print("\n")

pattern6(3)

# A
# B C 
# D E F
# G H I J

def pattern7(n):
    row =1
    while row<=n:
        col=1
        while col<=row:
            print(chr(ord('A')+row+col-2),end=" ")
            col+=1
        row+=1
        print()

print("\n")

pattern7(4)


# D
# C D
# B C D
# A B C D

def pattern8(n):
    row =1
    while row<=n:
        col=1
        while col<=row:
            print(chr(ord('A')+ n - row+col-1),end=" ")
            col+=1

        row+=1
        print()

print("\n")
pattern8(4)