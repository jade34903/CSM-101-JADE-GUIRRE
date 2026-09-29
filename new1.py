guirre_name = input("Enter Employee Name: ")
guirre_position = input("Enter Job Position (janitor, clerk, cashier, manager): ").lower()
guirre_hours = float(input("Enter Actual Hours Worked: "))

if guirre_position == "janitor":
    guirre_monthly = 18000
elif guirre_position == "clerk":
    guirre_monthly = 22000
elif guirre_position == "cashier":
    guirre_monthly = 24000
elif guirre_position == "manager":
    guirre_monthly = 40000
else:
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

    print("HALF MONTH PAYROLL")
    print("Employee Name:", guirre_name)
    print("Job Position:", guirre_position)
    print("Job Hours:", guirre_hours)
    print("Monthly Pay:", guirre_monthly)
    print("Basic half month salary:", guirre_basic)
    print("Hourly salary:", guirre_hourly)
    print("Absence hours:", guirre_absent)
    print("Absence deduction:", guirre_absence_deduction)
    print("Overtime hours:", guirre_overtime)
    print("Overtime pay:", guirre_overtime_pay)
    print("Half month salary:", guirre_net)

else:
    print("Invalid job position")
