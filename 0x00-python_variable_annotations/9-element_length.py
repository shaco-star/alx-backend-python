#!/usr/bin/env python3

"""
    Write a type-annotated function
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """

    Args:
        lst:

    Returns:
        tuple i
    """
    return [(i, len(i)) for i in lst]
