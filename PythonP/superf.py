class Person:
  def __init__(self, fname, lname, age , designation):
    self.firstname = fname
    self.lastname = lname
    self.age   =age
    self.designation= designation

  def Print_name(self):
    print(self.firstname, self.lastname, self.age,self.designation)

class Employee(Person):
  def __init__(self, fname, lname, age,designation):
    super().__init__(fname, lname, age,designation)

x = Employee("Satish", "Patidar",24,"Jr.Software Engineer")
x.Print_name()

