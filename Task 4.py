def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kilometers_to_miles(km):
    return km * 0.621371

def miles_to_kilometers(mi):
    return mi / 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kilograms(lb):
    return lb / 2.20462

conversion_functions = {
    'Temperature': {
        '1': ('Celsius to Fahrenheit', celsius_to_fahrenheit, '°C', '°F'),
        '2': ('Fahrenheit to Celsius', fahrenheit_to_celsius, '°F', '°C'),
    },
    'Distance': {
        '1': ('Kilometers to Miles', kilometers_to_miles, 'km', 'mi'),
        '2': ('Miles to Kilometers', miles_to_kilometers, 'mi', 'km'),
    },
    'Weight': {
        '1': ('Kilograms to Pounds', kilograms_to_pounds, 'kg', 'lb'),
        '2': ('Pounds to Kilograms', pounds_to_kilograms, 'lb', 'kg'),
    }
}

def display_menu():
    print("\nUnit Converter Menu")
    print("-------------------")
    print("Choose a conversion category:")
    print("1. Temperature")
    print("2. Distance")
    print("3. Weight")
    print("4. Exit")

def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            val = float(user_input)
            return val
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    while True:
        display_menu()
        choice = input("Enter the number of your choice: ").strip()
        if choice == '4':
            print("Exiting Unit Converter. Goodbye!")
            break
        elif choice in ['1','2','3']:
            if choice == '1':
                category = 'Temperature'
            elif choice == '2':
                category = 'Distance'
            else:
                category = 'Weight'
            print(f"\n{category} conversions:")
            for key, (desc, _, from_unit, to_unit) in conversion_functions[category].items():
                print(f"{key}. {desc} ({from_unit} → {to_unit})")
            conv_choice = input("Choose conversion: ").strip()
            if conv_choice in conversion_functions[category]:
                desc, func, from_unit, to_unit = conversion_functions[category][conv_choice]
                val = get_float_input(f"Enter value in {from_unit}: ")
                result = func(val)
                print(f"{val:.2f} {from_unit} is {result:.2f} {to_unit}.")
            else:
                print("Invalid conversion choice. Try again.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

