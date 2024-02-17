number = int(input("Enter number: "))
i = 0
res = 0
while res < number :
    res =  1<<i
    if res == number:
        print("True!: 2 Power",i)
        break
    i = i + 1
else:
        print("False")
        
 
