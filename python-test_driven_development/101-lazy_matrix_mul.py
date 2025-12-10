#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a: first matrix (list of lists)
        m_b: second matrix (list of lists)

    Returns:
        New matrix resulting from multiplication.

    Raises:
        TypeError: if matrices are invalid (same messages as 100-matrix_mul)
        ValueError: if matrices can't be multiplied
    """

    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check elements of m_a
    if not all(isinstance(num, (int, float))
               for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    # Check elements of m_b
    if not all(isinstance(num, (int, float))
               for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check row sizes for m_a
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Check row sizes for m_b
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check multiplication viability
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # NumPy multiplication
    result = np.matmul(m_a, m_b)

    return result.tolist()
