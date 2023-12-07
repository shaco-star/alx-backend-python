#!/usr/bin/env python3

"""
    Write a type-annotated function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k: string
        v: float and int

    Returns:
        tuple
    """
    return (k, float(v ** 2))
