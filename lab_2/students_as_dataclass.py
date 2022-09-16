from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

# can override the dataclass's included string method by simply including the __str__ method and customizing

def main():
    alex = Student('Alex', 'abcdef', 3.5)
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'qwerty', 4.0)
    print(sam)

main()
