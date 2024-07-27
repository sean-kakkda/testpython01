print("==========Welcom to the Tip Calculator ==========")
bill = float(input("What was the total bill?$\n"))
tip = float(input("How much tip would you like to give? 10, 12, 15?\n"))
people =float(input("How many people to split the bill?\n"))
tip_amount=bill*tip/100
pay=bill+tip_amount
each_pay=pay/people

print(f'Each Person should pay: {each_pay}$')