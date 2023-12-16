# math_operations.py

def basic_operations(a, b):
  """Perform basic arithmetic operations (addition, subtraction, multiplication, division).

  Args:
    a: The first number.
    b: The second number.

  Returns:
    A dictionary with the results for each operation.
  """
  results = {}
  results["addition"] = a + b
  results["subtraction"] = a - b
  results["multiplication"] = a * b
  results["division"] = a / b
  return results

def power_operation(base, exponent, **kwargs):
  """Calculate the result of the power operation.

  Args:
    base: The base number.
    exponent: The exponent.
    **kwargs: Optional keyword arguments.

  Returns:
    The result of the power operation.
  """
  if "modulo" in kwargs:
    return pow(base, exponent, kwargs["modulo"])
  else:
    return pow(base, exponent)

def apply_operations(operation_list):
  """Apply each function to its arguments and return a list of results.

  Args:
    operation_list: A list of tuples, where each tuple contains a function and its corresponding arguments.

  Returns:
    A list of results.
  """
  results = []
  for function, arguments in operation_list:
    results.append(function(*arguments))
  return results

if __name__ == "__main__":
  from math_operations import basic_operations, power_operation, apply_operations

  # Test basic_operations
  result_basic = basic_operations(10, 5)
  print("Basic Operations Result:", result_basic)

  # Test power_operation
  result_power = power_operation(2, 3)
  print("Power Operation Result:", result_power)

  # Test power_operation with modulo
  result_power_modulo = power_operation(2, 3, modulo=5)
  print("Power Operation with Modulo Result:", result_power_modulo)

  # Test apply_operations
  operations = [
    (lambda x, y: x + y, (3, 4)),
    (lambda x, y: x * y, (2, 5)),
  ]
  result_apply = apply_operations(operations)
  print("Apply Operations Result:", result_apply)