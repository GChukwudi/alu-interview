#!/usr/bin/python3


def rain(walls):
    """
    Calculate the total amount of rainwater retained.

    Args:
    - walls: A list of non-negative integers representing the heights of walls.

    Returns:
    - Integer indicating the total amount of rainwater retained.
    """
    if len(walls) < 3:
        return 0

    total = 0
    for i in range(1, len(walls) - 1):
        left_max = max(walls[:i])
        right_max = max(walls[i+1:])
        water = min(left_max, right_max) - walls[i]
        if water > 0:
            total += water

    return total