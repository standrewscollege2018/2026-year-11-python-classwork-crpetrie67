change = True
while change == True:

    print("Student driver status")
    print("="* 23)
    for i in range(len(names)):
        print(f"{i+1} {name[i]:15} {status[i]}")

    ask = True
    while ask == True:
        try:
            driver = int(input("Select student to update"))
            if driver < 0 or driver > len(names):
                print("Driver does not exsist")
            else:

            except ValueError:
                print("Please enter a number")
            
        if driver == 0:
            change = False