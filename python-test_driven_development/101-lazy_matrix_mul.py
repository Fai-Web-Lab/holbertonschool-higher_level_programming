#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy
    """
    try:
        return np.matmul(m_a, m_b)
    except Exception:
        if isinstance(m_a, str) or isinstance(m_b, str):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        raise
