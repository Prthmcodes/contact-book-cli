def show_menu():
    print("\n1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

contacts = {}
def add_contact(name, phone):
    try:
        if not name:
         raise ValueError("name can't be empty")
        if not phone:
            raise ValueError("phone can't be empty")
        if not phone.isdigit() or len(phone) != 11:
            raise ValueError("phone number must be 11 digits and contain only numbers")
        if name in contacts:
            raise KeyError(f"'{name}' already exists in contactbook.")
    except ValueError as e:
        print(e)
    except KeyError as e:
        print(e)
    else:
        contacts[name] = phone
        print(f"{name} successfully added with contact number {phone}")
        save_contacts()

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def search_contact(name):
    if not contacts:
        print("your contact book is empty mate")
    elif name not in contacts:
        print("name not found")
    else:
        print(f"{name} 's phone number is : {contacts[name]}")

def delete_contact(name):
    if not contacts:
        print("your contact book is empty mate")
    elif name not in contacts:
        print("name not found")
    else:
        del contacts[name]
        print(f"{name} has been deleted from contacts")
        save_contacts()


def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        print("No existing contacts found. Starting with an empty contact book.")
def save_contacts():
    with open("contacts.txt", "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

if __name__ == "__main__":
    load_contacts()
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice")