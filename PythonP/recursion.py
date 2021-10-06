def exmple_recursion(k):
  if(k > 0):
    result = k + exmpl_recursion(k - 1)
    print(result)
   else:
     result = 0
   return result

print("\n\nRecursion Examples Results")
exmpl_recursion(10)
