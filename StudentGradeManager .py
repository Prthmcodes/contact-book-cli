students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 91
}
while True:
    try:
        name =input ("Enter student name: ")
        if name == "exit":            break
        if name not in students:
            raise KeyError(f"Student '{name}' not found.")
        grade = int(input("Enter student grade: "))
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        students[name] = grade
        print(f"Added {name} with grade {grade}.")
    except ValueError as e:
        print(e)
    except KeyError as e:
        print(e)
    
   
    finally:
       print("Student grade entry complete.")
   