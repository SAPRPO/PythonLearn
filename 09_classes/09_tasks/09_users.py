class User:
    def __init__(self, first_name, last_name, email, age, country, city):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.country = country
        self.city = city

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")   
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

# Example usage
user1 = User('John', 'Doe', 'john@example.com', 25, 'USA', 'New York')
user2 = User('Jane', 'Smith', 'jane@example.com', 30, 'Canada', 'Toronto')
user3 = User('Alice', 'Johnson', 'alice@example.com', 22, 'Australia', 'Sydney')

user1.describe_user()
user1.greet_user()
print("\n")
user2.describe_user()
user2.greet_user()
print("\n")
user3.describe_user()
user3.greet_user()