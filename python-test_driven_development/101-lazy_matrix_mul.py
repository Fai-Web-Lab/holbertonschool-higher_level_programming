#!/usr/bin/python3
"""
This module provides a function for matrix multiplication using NumPy.
It leverages NumPy's optimized C backend for faster calculations.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using the NumPy module.

    Args:
        m_a: First matrix (list of lists).
        m_b: Second matrix (list of lists).

    Returns:
        The result of the multiplication.
    """
    return np.matmul(m_a, m_b)
