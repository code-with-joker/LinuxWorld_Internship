balance = 5000
pin  = 1234
count = 0

while True:
    user_pin = int(input("Enter your pin : "))

    if user_pin == pin:
        print("Your balance is ", balance)
        amount = int(input("Enter your amount to withdraw : "))
        balance = balance - amount
        print(f'Your {amount} successfully deducted from your account and now your balance is ', balance)

    else:
        print("Incorrect Pin")
        count += 1

        if count == 3:
            print("You entered incorrect PIN 3 times. ATM Blocked!")
            break
