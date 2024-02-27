def basic_operations(a, b):
  
  results = []
  results["addition"] = a + b
  results["subtraction"] = a - b
  results["multiplication"] = a * b
  results["division"] = a / b
  return results


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