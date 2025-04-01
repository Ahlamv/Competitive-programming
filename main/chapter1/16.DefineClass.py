class Student:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
    def display_info(self):
        print(self.name)
        print(self.age)
        print(self.course)
Student1=Student("Ahlam",20,5)
Student1.display_info()