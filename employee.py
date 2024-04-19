import csv

class Person:
    def __init__(self, id, name, age, department, email):
        self.id = id
        self.name = name
        self.age = age
        self.department = department
        self.email = email

    file_path = 'employees.csv'

    @staticmethod
    def read_db(file_path):
        a = []
        with open(file_path, 'r') as file:
            b = csv.DictReader(file)
            for row in b:
                c = Person(int(row['id']), row['name'], int(row['age']), row['department'], row['email'])
                a.append(c)
        return a

    def f(self, file_path):
        a = Person.read_persons_from_csv(file_path)
        for person in a:
            if person.name == self.name and person.email == self.email:
                raise ValueError("Person already exists in the CSV file.")
        with open(file_path, 'a', newline='') as file:
            b = csv.writer(file)
            b.writerow([self.id, self.name, self.age, self.department])

