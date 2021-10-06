class Person:
  def __init__(self, name, age):# The __init__() function is called automatically every time the class is being used to create a new object.
    self.name = name
    self.age = age

obj = Person("Satish", 24)

print(obj.name)
print(obj.age)

