print("===== STUDENT REPORT CARD MANAGEMENT SYSTEM =====")

while True:
    print("""
    1. Add Student report.txt
    2. View Saved Reports
    3. Search
    4. Exit
    """)

    choice = input("\nEnter your choice: ")

    # -----ADD NEW STUDENT------------
    if choice == "1":
        name = input("\nEnter Student Name: ")
        roll = input("Enter Roll Number: ")
        clas = input("Enter Class: ")

        subjects = ("Maths", "Science", "English", "Computer", "History")
        marks = []
        print("\nEnter marks out of 100:")

        # Taking marks with error handling
        for sub in subjects:
            while True:
                try:
                    m = int(input(f"Marks in {sub}: "))
                    if m < 0 or m > 100:
                        print("Marks must be 0-100, try again!")
                        continue
                    marks.append(m)
                    break
                except:
                    print("Invalid input! Enter numbers only!")

        # Calculate total and percentage
        total = 0
        for m in marks:
            total += m
        percentage = total / len(subjects)

        # Grade calculation
        if percentage >= 90:
            grade = "A"
        elif percentage >= 80:
            grade = "B"
        elif percentage >= 70:
            grade = "C"
        elif percentage >= 60:
            grade = "D"
        else:
            grade = "Fail"

        # Show report
        print("\n=========== REPORT CARD ===========")
        print(f"Name: {name}")
        print(f"Roll No.: {roll}")
        print(f"Class: {clas}")
        print("-----------------------------------")

        for i in range(len(subjects)):
            print(f"{subjects[i]} : {marks[i]}")

        print("-----------------------------------")
        print(f"Total Marks: {total}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print("===================================")

        # Save to file
        file = open("report.txt", "a")
        file.write("\n========== REPORT CARD ==========\n")
        file.write(f"Name: {name}\n")
        file.write(f"Roll No.: {roll}\n")
        file.write(f"Class: {clas}\n")
        file.write("----------------------------------\n")

        for i in range(len(subjects)):
            file.write(f"{subjects[i]} : {marks[i]}\n")

        file.write("----------------------------------\n")
        file.write(f"Total Marks: {total}\n")
        file.write(f"Percentage: {percentage:.2f}%\n")
        file.write(f"Grade: {grade}\n")
        file.write("==================================\n")
        file.close()

        print("\nReport saved successfully!")

    # ------Show SAVED REPORTS--------
    elif choice == "2":
        try:
            fr = open("report.txt", "r")
            print("\n======= SAVED REPORTS =======")
            print(fr.read())
            fr.close()
        except:
            print("\nNo reports found!")

    # ------SEARCH STUDENT REPORT--------
    elif choice == "3":
        search_value = input("\nEnter Name or Roll Number to search: ")
    
        try:
            file = open("report.txt", "r")
            data = file.readlines()
            file.close()
    
            found = False
    
            print("\n======= SEARCH RESULT =======")
    
            for i in range(len(data)):
                if search_value.lower() in data[i].lower():
    
                    found = True

                    j = i
                    while j < len(data) and "====" not in data[j]:
                        print(data[j], end="")
                        j += 1
                    print()  # new line break
                    break
    
            if not found:
                print("\nNo matching record found!")
    
        except:
            print("\nFile not found!")


    # ------EXIT--------
    elif choice == "4":
        print("\nThank you for using the Report Card System!")
        break

    else:
        print("Invalid choice! Try again.")
