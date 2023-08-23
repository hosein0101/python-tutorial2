number = int(input("Enter the pattern number: "))
pattern=[]
for i in range(number):
    print(("*"*(2 * i + 1)).center(2*number-1))

for i in range(n-2, -1, -1):
    print(("*"*(2 * i + 1)).center(2*number-1))
