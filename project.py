print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rows = int(input("Enter the number of rows for the pattern: "))
        if rows <= 0:
            print("Invalid row count!")
            continue

        print("Pattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    elif choice == "2":
        rows = int(input("Enter the number of rows for the pattern: "))
        if rows <= 0:
            print("Invalid row count!")
            continue

        print("Pattern:")
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end="")
            for j in range(2 * i - 1):
                print("*", end="")
            print()

    elif choice == "3":
        rows = int(input("Enter the number of rows for the pattern: "))
        if rows <= 0:
            print("Invalid row count!")
            continue

        print("Pattern:")
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            print()

    elif choice == "4":
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if end <= start:
            print("Invalid range!")
            continue

        total = 0

        for n in range(start, end + 1):
            if n % 2 == 0:
                print("Number", n, "is Even")
            else:
                print("Number", n, "is Odd")
            total += n

        print("Sum of all numbers from", start, "to", end, "is:", total)

    elif choice == "5":
        print("Thank you for using the Pattern Generator and Number Analyzer!")
        break

    else:
        print("Invalid choice!")
        continue

    print("\n" + "-" * 60)
