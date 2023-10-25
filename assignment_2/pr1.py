class Student:
    def __init__(self) -> None:
        self.name = input("Enter name: ")
        self.roll = int(input("Enter roll:"))
        self.dept = input("Enter dept:")
        self.marks = int(input("Enter marks:"))
    
    def displayData(self):
        print("\n\nName:", self.name)
        print("Roll:", self.roll)
        print("Dept:", self.dept)
        print("Marks:", self.marks)

    
noOfStudents = int(input("Enter no of students:"))

for i in range(noOfStudents):
    s = Student()
    s.displayData()
    print()
