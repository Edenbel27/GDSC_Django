def basic_operations(a, b):
  results = []
  addition= a + b
  subtraction = a - b
  multiplication = a * b
  division = a / b
  results.append(addition)
  results.append(subtraction)
  results.append(multiplication)
  results.append(division)
  for i in results:
      print(i)


def power_operation(base, exponent, **kwargs):
  
  if "modulo" in kwargs:
    return pow(base, exponent, kwargs["modulo"])
  else:
    return pow(base, exponent)

def apply_operations(operation_list):
  
  results = []
  for function, arguments in operation_list:
    # instead of the for loop we can use 'map'.
    results.append(function(*arguments))
  return results