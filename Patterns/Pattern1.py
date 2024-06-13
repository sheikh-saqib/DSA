def star_pattern(n):
    row=0
    while row<n:
        col = 0
        while col<n+1:
            print("*",end=" ")
            col+=1
        print()
        row+=1

print("\n")
star_pattern(3)
def numeric_pattern(n):
    row=0
    while row<n:
        col = 0
        while col<n+1:
            print(row,end=" ")
            col+=1
        print()
        row+=1

print("\n")
numeric_pattern(3)

#Main Logic - Get the mathametical relation between rows and columns

