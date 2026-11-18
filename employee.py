class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"Role: {self.role}")


employee = Employee("Vasavi", "DevOps Engineer")
employee.display_details()
