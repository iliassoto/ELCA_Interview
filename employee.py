import csv

class Person:
    def __init__(self, id, name, age, department, email):
        self.id = id
        self.name = name
        self.age = age
        self.department = department
        self.email = email

    @staticmethod
    def read_persons_from_csv(file_path):
        a = []
        with open(file_path, 'r') as file:
            b = csv.DictReader(file)
            for row in b:
                c = Person(int(row['id']), row['name'], int(row['age']), row['department'], row['email'])
                a.append(c)
        return a

    @staticmethod
    def add_person_to_csv(file_path, new_person):
        a = Person.read_persons_from_csv(file_path)
        for person in a:
            if person.name == new_person.name and person.email == new_person.email:
                raise ValueError("Person already exists in the CSV file.")
        with open(file_path, 'a', newline='') as file:
            b = csv.writer(file)
            b.writerow([new_person.id, new_person.name, new_person.age, new_person.department])

# Example usage
file_path = 'employees.csv'


def add(name, age, dept, email):
    new_person = Person("John Doe", 30, "IT", "john.doe@elca.com")
    try:
        Person.add_person_to_csv(file_path, new_person)
        print("Person added successfully.")
    except ValueError as e:
        print(e)