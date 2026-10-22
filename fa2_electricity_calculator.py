# Electricity Bill Calculator
RATE = 12.90
name = input("Enter customer name: ")

if name == "":
    print("Please restart and enter your name.")
    name = input("Enter customer name: ")
    
previous = float(input("Enter previous meter reading: "))

if previous < 0:
    print("Meter reading invalid. Please re-enter your previous meter reading.")
    previous = float(input("Enter previous meter reading: "))

current = float(input("Enter current meter reading: "))

if current < previous:
    print("Current meter reading invalid. Please re-enter your current meter reading.")
    current = float(input("Enter current meter reading: "))

consumption = current - previous
total_bill = consumption * RATE

print("\nCustomer:", name)
print("Electricity Consumption:", consumption, "kWh")
print("Total Bill: PHP", round(total_bill, 2))
