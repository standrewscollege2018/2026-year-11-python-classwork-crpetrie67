

cars = ["Suzuki Van (2)", "Toyota Corolla (4)", "Honda CRV (4)", "Suzuki Swift (4)", "Mitsubishi Airtrek (4)", "Nissan DC Ute (4)", "Toyota Previa (7)",  "Toyota Hi Ace (12)", "Toyota Hi Ace (12)"]


print("Welcome to the university vehicle rental system!")
print()
print("The vehicles: ")
for i in range(len(cars)):
    print(f"{i+1} {cars[i]}")