while True:
        choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 for exit: "))
        if choice == 5:
            break
        print("Exiting")
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))
        match choice:
            case 1:
                print("The sum is: ", n1+n2)
            case 2:
	            print("The difference is: ", n1-n2)
            case 3:
                print("The multiplication is: ", n1*n2)
            case 4:
	            print("The division is: ", n1/n2)
            case _:
                print("invalid input")