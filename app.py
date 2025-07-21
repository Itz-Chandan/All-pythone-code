from bank import withdraw

# Initial balance
balance = 100

# Simulate withdrawal
try:
    print(f"Current balance: ${balance}")
    amount = 200 # Trying to withdraw more than balance
    print(f"withdrawing ${amount}...")
    balance = withdraw(amount, balance)
    print(f"New balance: ${balance}")
except ValueError as e:
    print(f"Error: {e}")
