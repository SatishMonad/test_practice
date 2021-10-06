class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def my_func(self):#object method
    print("Hello my name is " + self.name)

obj = Person("Satish", 24)
obj.my_func()

