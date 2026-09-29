print("Select Pizza Flavor:")
print("1. Hawaiian")
print("2. Oreo")
Guirreflavor_choice = input("Enter flavor number (1-2): ")

match Guirreflavor_choice:
    case "1":
        Guirreflavor = "hawaiian"
        print("\nSelect Size:")
        print("1. Small")
        print("2. Medium")
        print("3. Large")
        size_choice = input("Enter size number (1-3): ")

        match size_choice:
            case "1":
                Guirreprice = 250
            case "2":
                Guirreprice = 500
            case "3":
                Guirreprice = 1000
            case _:
                Guirreprice = 0
                print("Invalid size selection.")

    case "2":
        Guirreflavor = "oreo"
        print("\nYou selected oreo pizza")
        print("Select Size:")
        print("1. Small")
        print("2. Medium")
        print("3. Large")
        size_choice = input("Enter size number (1-3): ")

        match size_choice:
            case "1":
                Guirreprice = 250
            case "2":
                Guirreprice = 500
            case "3":
                Guirreprice = 1000
            case _:
                Guirreprice = 0
                print("Invalid size selection.")

    case _:
        Guirreflavor = "unknown"
        Guirreprice = 0
        print("Invalid flavor selection.")

print("\n--- Receipt ---")
print("Flavor:", Guirreflavor.title())
print("Total amount: PHP", Guirreprice)
