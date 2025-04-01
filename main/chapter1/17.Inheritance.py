class Course:
    def __init__(self,name):
          self.name=name
    def get_details(self,name):
           self.name=name
          

class WebDevclass(Course):
        pass
course=WebDevclass("c++")
print(course.name)