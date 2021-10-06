def my_func(n):
  return lambda a : a * n

double_value = my_func(5)
triple_value = my_func(10)

print(double_value(100)) 
print(triple_value(200))

