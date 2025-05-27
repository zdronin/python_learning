bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15%?: "))
tip = bill * (tip_percentage / 100)
print(f"For a ${bill:.2f} bill with a {tip_percentage}% tip, the tip amount is ${tip:.2f}")