# num = int(input("enter your number:"))

for j in range(1,100):
    count = 0
    for i in range(1,j):
        if (j%i == 0):
            count = count + 1
    if (count > 2):
        print(j," is not prime")
    else:
        print(j," is prime")