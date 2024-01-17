#!/usr/bin/python3
"""
This script defines a function 'minOperation' to calculate the fewest number
of operations needed to obtain 'n' 'H' characters in the file.
"""
import math


def minOperation(n):
  """
  Recursively calculates the minimum number of operations needed.

  Args:
  - n: The target number of 'H' characters.

  Returns:
  - The fewest number of operations required.
  """
  if n <= 1:
    return 0
  
  operations = 0
  for i in range(2, int(math.sqrt(abs(n))) + 1):
    while n % i == 0:
        operations += i
        n //= i

  if n > 1:
    operations += n

  return operations
