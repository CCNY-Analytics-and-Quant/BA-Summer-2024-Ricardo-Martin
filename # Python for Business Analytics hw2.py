'''
Python for Business Analytics HW2
Name: Ricardo Martin
ECO 32500 S'2024
'''

# Task 1: Add returns to the for-loop (how much for retirement at 65)
initial_balance = -10000 # student loans lol
annual_contribution = 5000 # Attauined a good job post college
annual_return = 0.07
years_until_retirement = 42  # Assuming starting age is 23, retirement at 65

balance = initial_balance

for year in range(1, years_until_retirement + 1):
    balance += annual_contribution
    balance += balance * annual_return

print(f"Balance after {years_until_retirement} years: ${balance:.2f}")

# Task 2: Calculate how much you need to retire on
annual_expenses = 40000
withdrawal_rate = 0.03

target_retirement_savings = annual_expenses / withdrawal_rate

print(f"Target retirement savings: ${target_retirement_savings:.2f}")

# Task 3: Create a while loop that shows at what age you can retire, how much money you'd have, and what the expenses are
balance = initial_balance
current_age = 23
retirement_age = current_age

while balance < target_retirement_savings:
    balance += annual_contribution
    balance += balance * annual_return
    retirement_age += 1

print(f"Based on your contributions. You can retire at age: {retirement_age}")
print(f"Your retirement savings at age {retirement_age}: ${balance:.2f}")
print(f"The annual expenses at retirement are: ${annual_expenses:.2f}")