class Employee():
    def __init__(self, name, surname, salary_year):
        self.name = name
        self.surname = surname
        self.salary_year = salary_year
    
    def give_raise(self, salary_year_raise=5000):
        old_salary= self.salary_year
        self.salary_year = self.salary_year + salary_year_raise
        print(f"Good Day {self.name} {self.surname}\nYour salary: {old_salary} raised up {salary_year_raise}.\nNow your current is: {self.salary_year} ")