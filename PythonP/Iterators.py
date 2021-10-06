class Income:
  def __iter__(self):
    self.a = 10000
    return self

  def __next__(self):
    x = self.a
    self.a += 2000
    return x

My_class = Income()
My_iter = iter(My_class)

print(next(My_iter))
print(next(My_iter))
print(next(My_iter))
print(next(My_iter))
print(next(My_iter))
print(next(My_iter))
print(next(My_iter))
print(next(My_iter))
print(next(My_iter))
print(next(My_iter))

