num = int(input("Enter number:"))
i = 0
res = 0
whileres < num :
    res = 1<<i
    if res == num:
        print("True",i)
        break
    i = i+1
    else:
        print("False")

