#=============================================================class=============================================================


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("Enter your journal entry:\n")

        with open(self.filename, "a") as file:
            file.write(entry + "\n")

        print("Entry added successfully!\n")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

            if data:
                print("\nYour Journal Entries:")
                print(data)
            else:
                print("No journal entries found.\n")

        except FileNotFoundError:
            print("No journal file found. Add an entry first.\n")

    def search_entry(self):
        keyword = input("Enter keyword to search: ")

        try:
            with open(self.filename, "r") as file:
                found = False
                for line in file:
                    if keyword.lower() in line.lower():
                        print(line.strip())
                        found = True

                if not found:
                    print("No matching entries found.\n")

        except FileNotFoundError:
            print("No journal file found.\n")

    def delete_entries(self):
        confirm = input("Delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            open(self.filename, "w").close()
            print("All entries deleted.\n")
        else:
            print("Deletion cancelled.\n")


def main():
    journal = JournalManager()   
#=============================================================program=============================================================

    while True:
        print("===== Personal Journal Manager =====")
        print()
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")
        print()
        print("User Input:")
        choice = int(input())

        match choice:
            case 1:
                journal.add_entry()

            case 2:
                journal.view_entries()

            case 3:
                journal.search_entry()

            case 4:
                journal.delete_entries()

            case 5:
                print("Thank you for using Personal Journal Manager. Goodbye!")
                break

            case _:
                print("Invalid option. Please select a valid option.\n")


if __name__ == "__main__":
    main()

