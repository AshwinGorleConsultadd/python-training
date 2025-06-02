#Parent class

class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def calculate_salary(self):
        """Override this in subclasses"""
        return self.base_salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Final Salary: ${self.calculate_salary():.2f}")


# Classes inheriting form Employee with some extra attributes (parent class)
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        tax = 0.10 * self.base_salary
        pf = 0.12 * self.base_salary
        final_salary = self.base_salary - tax - pf
        return final_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        base_salary = hourly_rate * hours_worked
        super().__init__(name, employee_id, base_salary)

    def calculate_salary(self):
        tax = 0.10 * self.base_salary
        pf = 0.12 * self.base_salary
        final_salary = self.base_salary - tax - pf
        return final_salary


class Contractor(Employee):
    def __init__(self, name, employee_id, contract_amount):
        super().__init__(name, employee_id, contract_amount)

    def calculate_salary(self):
        tax = 0.10 * self.base_salary
        final_salary = self.base_salary - tax  # No PF
        return final_salary

#Driver code

emp1 = FullTimeEmployee("Alice", "FT101", 6000)
emp2 = PartTimeEmployee("Bob", "PT202", hourly_rate=20, hours_worked=80)
emp3 = Contractor("Charlie", "CT303", contract_amount=5000)

print("\n--- Full-Time Employee ---")
emp1.display_info()

print("\n--- Part-Time Employee ---")
emp2.display_info()

print("\n--- Contractor ---")
emp3.display_info()



