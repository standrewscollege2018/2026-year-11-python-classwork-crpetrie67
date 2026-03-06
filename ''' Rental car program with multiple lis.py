''' Rental car program with multiple lists '''

# Set up lists for car names, seats and availability
cars = ["Suzuki Van", "Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtek", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"]
seats = [2, 4, 4, 4, 4, 4, 7, 12, 12]
availability = [True, True, True, True, True, True, True, True, True]
renters = ["John Smith", "Shannon Johnson", "", "", "", "", "", "", ""]

# Run the program in a loop so user can keep making changes
run_program = True
while run_program == True:
    # Display title and list of vehicles
    print("Welcome to the University vehicle rental system")
    print("The vehicles are:")
    # Display cars in a numbered list
    for i in range(len(cars)):
        

        print(f"{i+1}. {cars[i]} ({seats[i]})")

    # Ask user what vehicle they want to book
    # Error catching stops them entering invalid inputs like a string or a number outside the range of the number of cars
    
    
    
    selection = int(input("What vehicle would you like to book? "))
    # If user enters 0 as their selection then the program stops asking them for a vehicle to book
    if selection == 0:
    
        run_program = False
    
    elif availability[selection-1] == False:
        print("*** This vehicle is already booked. Please book another ***")
    else:
        # Get their name for the booking
    
            name = input("Enter your name: ")

            renters[selection-1] = name
            get_name = False
        
            availability[selection-1] = False
    

