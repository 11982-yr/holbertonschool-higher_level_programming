#!/usr/bin/python3
"""
Function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix
    """

    # 1. m_a and m_b must be lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. m_a and m_b must be lists of lists
    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. m_a and m_b cannot be empty: [] or [[]]
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Elements must be ints or floats
    for row in m_a:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # 5. m_a and m_b must be rectangles (rows same size)
    row_len_a = len(m_a[0])
    if any(len(row) != row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_len_b = len(m_b[0])
    if any(len(row) != row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Validate multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            dot = 0
            for k in range(len(m_b)):
                dot += m_a[i][k] * m_b[k][j]
            row_result.append(dot)
        result.append(row_result)

    return result
