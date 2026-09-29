while True:
        guirre_name = input("Enter Employee Name: ")
        guirre_position = input("Enter Job Position (janitor, clerk, cashier, manager): ").lower()
        guirre_hours = float(input("Enter Actual Hours Worked: "))

        match guirre_position:
            case "janitor":
                guirre_monthly = 18000
            case "clerk":
                guirre_monthly = 22000
            case "cashier":
                guirre_monthly = 24000
            case "manager":
                guirre_monthly = 40000
            case _:
                guirre_monthly = 0

        if guirre_monthly > 0:
            guirre_basic = guirre_monthly / 2
            guirre_hourly = guirre_monthly / 88

            if guirre_hours < 88:
                guirre_absent = 88 - guirre_hours
                guirre_absence_deduction = guirre_absent * guirre_hourly
                guirre_overtime = 0
                guirre_overtime_pay = 0
            else:
                guirre_absent = 0
                guirre_absence_deduction = 0
                guirre_overtime = guirre_hours - 88
                guirre_overtime_rate = guirre_hourly * 1.25
                guirre_overtime_pay = guirre_overtime * guirre_overtime_rate



            guirre_net = guirre_basic - guirre_absence_deduction + guirre_overtime_pay

            print("\n--- HALF MONTH PAYROLL ---")
            print("Employee Name:", guirre_name)
            print("Job Position:", guirre_position.capitalize())
            print("Job Hours:", guirre_hours)
            print("Monthly Pay:", guirre_monthly)
            print("Basic half month salary:", guirre_basic)
            print("Hourly salary:", round(guirre_hourly, 2))
            print("Absence hours:", guirre_absent)
            print("Absence deduction:", round(guirre_absence_deduction, 2))
            print("Overtime hours:", guirre_overtime)
            print("Overtime pay:", round(guirre_overtime_pay, 2))
            print("Half month salary:", round(guirre_net, 2))
        else:
            print("Invalid job position")




        again = input("Would you like to continue (y/n)? ")
        if again.upper() != "Y":
            print("Thank you for your time!")
            break


