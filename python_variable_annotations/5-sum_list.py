#!/usr/bin/env python3
"""
This script defines a function to compute the sum of a list of floating-point numbers.

Functions:
    sum_list(input_list): Returns the sum of all elements in a list of floats.
"""


def sum_list(input_list: list[float]) -> float:
    """
    Computes the sum of all elements in a list of floating-point numbers.

    Args:
        input_list (list[float]): A list of floating-point numbers to sum.

    Returns:
        float: The sum of all elements in the input list.
    """
    float_sum = 0.0  # Initialize the sum to zero
    for number in input_list:
        float_sum += number
    return float_sum
