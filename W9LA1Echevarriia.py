from W9LA1Echevarria import ECHEVARRIA1

print("=== CALCULATION MENU ===")
print("1. Power")
print("2. Voltage")
print("3. Current")

ECHEVARRIA1 = int(input("Enter your choice: "))

if ECHEVARRIA1 == 1:
    ECHEVARRIAvoltage = int(input("Enter your voltage: (V) "))
    ECHEVARRIAcurrent = int(input("Enter your current: (C) "))
    ECHEVARRIApower = ECHEVARRIAvoltage * ECHEVARRIAcurrent
    print = ("Power = ", ECHEVARRIApower, "W")

elif ECHEVARRIA1 == 2:
    ECHEVARRIApower = int(input("Enter your power: (W) "))
    ECHEVARRIAcurrent = int(input("Enter your voltage: (V) "))
