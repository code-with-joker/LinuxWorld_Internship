print("----------SIMPLE NOTEPAD CONSOLE APP --------------")

while True:
    print("""
    1. Add Note
    2. View All Notes
    3. Search Note
    4. Exit
    """)

    choice = input("Enter your choice: ")

    # ---------------- ADD NOTE ----------------
    if choice == "1":
        note = input("\nWrite your note here:\n")

        file = open("notes.txt", "a")
        file.write("\n---- NOTE ----\n")
        file.write(note + "\n")
        file.close()

        print("\nNote saved successfully!")

    # ---------------- VIEW NOTES ----------------
    elif choice == "2":
        try:
            file = open("notes.txt", "r")
            print("\n======= ALL NOTES =======")
            print(file.read())
            file.close()
        except:
            print("\nNo notes found!")

    # ---------------- SEARCH NOTE ----------------
    elif choice == "3":
        search_text = input("\nEnter word to search: ")

        try:
            file = open("notes.txt", "r")
            lines = file.readlines()
            file.close()

            found = False
            print("\n======= SEARCH RESULT =======")

            for line in lines:
                if search_text.lower() in line.lower():
                    print(line, end="")
                    found = True

            if not found:
                print("\nNo matching text found!")

        except:
            print("\nNo notes file found!")

    # ---------------- EXIT ----------------
    elif choice == "4":
        print("\nThank you for using Notepad App!")
        break

    else:
        print("\nInvalid choice! Try again.")
