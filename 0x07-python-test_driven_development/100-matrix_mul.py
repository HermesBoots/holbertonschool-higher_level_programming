#!/usr/bin/python3
"""Function to multiply matrices"""


def matrix_mul(m_a, m_b):
    """Multiply 2 matrices

    Args:
        m_a (list of list of (int or float)): first matrix
        m_b (list of list of (int or float)): second matrix

    Returns:
        list of list of (int or float): dot product of matrices

    """

    isita = isinstance
    if not isita(m_a, list):
        raise TypeError('m_a must be a list')
    if not isita(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isita(i, list) for i in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isita(i, list) for i in m_b):
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError('m_b can\'t be empty')
    if not all(isita(i, float) or isita(i, int) for l in m_a for i in l):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isita(i, float) or isita(i, int) for l in m_b for i in l):
        raise TypeError('m_b should contain only integers or floats')
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError('each row of m_a must should be of the same size')
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
    return [
        [
            sum(r * c for r, c in zip(left, right))
            for right in list(zip(*m_b))
        ]
        for left in m_a
    ]
