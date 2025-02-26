def menu():
    while True:
        file = "D:\Python\python-homework\lesson-6\homework\employees.txt"
        print("Options")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        
        option = int(input("Enter your choice: "))
        if option == 1:
            f = open(file, 'a')
            id = input("Employee ID: ")
            name = input("Name: ")
            position = input("Position: ")
            salary = input("Salary: ")
            f.write(f"{id}, {name}, {position}, {salary}\n")
            f.close()
            print("Added!")
            break
        elif option == 2:
            f = open(file)
            print(f.read())
            f.close()
            break
        elif option == 3:
            with open(file, 'r') as f:
                lines = f.readlines()
            id_input = input("Enter an employee ID: ")
            found = False
            for line in lines:
                if line.startswith(id_input):
                    print("Employee found: ", line.strip())
                    found = True
                    
            if found == True:
                break
            else:
                print("Employee not found.\n")
                break
        elif option == 4:
            id_input = input("Enter employee ID: ")
            with open(file, 'r') as f:
                lines = f.readlines()
            found = False
            with open(file, 'w') as f:
                for line in lines:
                    if line.startswith(id_input +","):
                        name = input("Enter new name: ")
                        position = input("Enter new position: ")
                        salary = input("Enter new salary: ")
                        f.write(f"{id_input}, {name}, {position}, {salary}\n")
                        found = True
                    else:
                        f.write(line)
                    
            if found:
                print("Updated!")
            else: print("ID not found")
            break
        elif option == 5:
            id_input = input("Enter employee ID: ")
            with open(file) as f:
                lines = f.readlines()
            with open(file, 'w') as f:
                for line in lines:
                    if id_input not in line:
                        f.write(line)
            break
        elif option == 6:
            exit()
            break    
menu()
