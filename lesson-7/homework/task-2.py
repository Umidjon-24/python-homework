class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    def __str__ (self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

file = "D:\Python\python-homework\lesson-7\homework\employees.txt" 
class EmployeeManager:
    
    def __init__(self):
       pass
    def menu(self):
        print("""1. Add new employee record\n2. View all employee records\n3. Search for an employee by Employee ID\n4. Update an employee's information\n5. Delete an employee record\n6. Exit""")
        choice = int(input("Choose an option: "))
        return choice

    def add(self):
            
        with open(file) as f:
            employee_id = int(input("Enter a employee ID: "))
            lines = f.readlines()
            while True:
                for line in lines:
                    if line.startswith(str(employee_id)):
                        print("Employee ID already exists!")
                        employee_id = int(input("Enter unique employee ID: "))
                    else: False
            
        name = input("Enter a name: ")
        position = input("Enter a position: ")
        try:    
            salary = int(input("Enter a salary: "))
        except ValueError:
            print("Invalid value. Please enter numeric value: ")  
            
        
        with open(file) as f:
            new_employee = Employee(employee_id, name, position, salary)
            f.write(f"{new_employee.employee_id}, {new_employee.name}, {new_employee.position}, {new_employee.salary}\n")
        print("Employee added successfully!")
    
    def view(self):
        with open(file) as f:
            print(f.read())

    def update(self):
        with open(file) as f:
            lines = f.readlines()
        with open(file, 'w') as f:
            employee_id = input("Enter a employee ID to update: ")
            found = False
            for line in lines:
                if line.startswith(employee_id + ","):
                    name = input("Enter a new name: ")
                    position = input("Enter a new position: ")
                    salary = input("Enter a new salary: ")
                    f.write(f"{employee_id}, {name}, {position}, {salary}")
                    found = True
                else:
                    f.write(line)
            if found:
                print("Updated")
            else: print("Employee is not found")

    def search(self):
        employee_id = input("Enter employee ID: ")
        found = False
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith(employee_id + ","):
                    print("Employee found: ", line.strip())
                    found = True
        if found == False:
            print("Employee is not found")
        

    def delete(self):
        with open(file) as f:
            lines = f.readlines()
        with open(file, 'w') as f:
            employee_id = input("Enter a employee ID to delete: ")
            found = False
            for line in lines:
                if employee_id not in line:
                    f.write(line)
                    found = True
            if found:
                print("Deleted")
            else: print("Employee is not found")

def main_menu():
    manager = EmployeeManager()
    while True:
        match manager.menu():
            case 1:
                manager.add()
            case 2:
                manager.view()
            case 3:
                manager.search()
            case 4:
                manager.update()
            case 5:
                manager.delete()
            case 6:
                exit()
            case _:
                print("Enter value in between 1-6: ")

main_menu()

           