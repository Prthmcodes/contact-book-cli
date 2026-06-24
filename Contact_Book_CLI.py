import sqlite3

def show_menu():
    print("\n1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")


def get_connection():
    conn = sqlite3.connect("contacts.db")
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS contacts(
                   id  INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone TEXT NOT NULL
                   email TEXT

                   )
                   
        """)
    conn.commit()
    conn.close()


def add_contact(name, phone):
    try:
        if not name:
         raise ValueError("name can't be empty")
        if not phone:
            raise ValueError("phone can't be empty")
        if not phone.isdigit() or len(phone) != 11:
            raise ValueError("phone number must be 11 digits and contain only numbers")
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()
        print(f"{name} added successfully")
        
    except ValueError as e:
        print(e)
   


def view_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        print("no contacts found")
    else:
        for row in rows:
            print(f"{row[1]} : {row[2]}")

def search_contact(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name = ?" ,(name,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        print("contact not found")
    else:
        print(f"{row[1]} : {row[2]}")

def delete_contact(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row is None:
        print("Contact not found.")
    else:
        cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        conn.commit()
        print(f"{name} has been deleted.")
    conn.close()

if __name__ == "__main__":
    create_table()
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