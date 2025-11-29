import time
import random
import pywhatkit

# Read contacts
def load_contacts():
    contacts = []
    with open("contacts.txt", "r") as f:
        for line in f:
            line = line.strip()

            if not line or "," not in line:
                continue

            name, number = line.split(",", 1)
            contacts.append((name.strip(), number.strip()))
    return contacts


# suru
contacts = load_contacts()

if not contacts:
    print("No contacts found! Check contacts.txt")
    exit()

print("Contacts Loaded:", contacts)

print("\n------------ BULK WHATSAPP SENDER ---------------\n")
message = input("Enter message: ")
count = int(input("How many messages to send?: "))

for i in range(count):
    name, number = random.choice(contacts)

    now = time.localtime()
    hour = now.tm_hour
    minute = now.tm_min + 1

    print(f"\nSending to: {name} - {number}")

    try:
        pywhatkit.sendwhatmsg(number, message, hour, minute)
        print("Sent Successfully!")
    except Exception as e:
        print("Error:", e)

    time.sleep(random.randint(5, 10))

print("\nAll messages sent!")
