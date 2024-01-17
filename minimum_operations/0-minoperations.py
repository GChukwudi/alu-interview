#!/usr/bin/python3
"""
This script defines a function 'minOperation' to calculate the fewest number
of operations needed to obtain 'n' 'H' characters in the file.
"""


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

  if n % 2 == 0:
    return 1 + minOperation(n / 2)
  return 1 + minOperation(n - 1)

n = 4
print(minOperation(n))