#!/usr/bin/env python3

"""
    Write a type-annotated function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """

    Args:
        input_list:

    Returns:
        float

    """
    return float(sum(input_list))
