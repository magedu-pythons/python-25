for i in range(4):
    for k in range(3-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*", end=" ")
    print()
for i in range(3):
    for a in range(i+1):
        print(" ", end=" ")
    for m in range((5-3*i)+i):
        print("*",end=" ")
    print()

