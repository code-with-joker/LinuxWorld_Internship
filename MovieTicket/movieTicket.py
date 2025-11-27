age = int(input("Enter your age: "))

ticket_input = input("Do you have a ticket? (yes/no): ").lower()
ticket = ticket_input == "yes"

# Main Logic
if age >= 18:
    if ticket:
        print("You are allowed to watch the movie.")
        print("You may go inside the hall.")
    else:
        print("You need a ticket to enter.")
elif 15 <= age < 18:
    if ticket:
        print("You can watch the movie but only with a guardian.")
    else:
        print("You must bring a guardian AND a ticket.")
else:
    print("You are under 15. You can watch only with parents and a valid ticket.")
