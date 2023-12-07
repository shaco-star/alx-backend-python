#!/usr/bin/env python3

"""
    Write a type-annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """

    Args:
        multiplier: float

    Returns:
            float
    """
    return lambda x: x * multiplier
