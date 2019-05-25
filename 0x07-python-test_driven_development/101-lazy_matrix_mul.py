#!/usr/bin/python3
"""Function to multiply matrices unsing numpy"""


import numpy.matrixlib


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using numpy

    Args:
        m_a (list of list of (float or int)): first matrix
        m_b (list of list of (float or int)): second matrix

    Returns:
        (matrix): product of m_a and m_b

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
    m_a = numpy.matrixlib.matrix(m_a)
    m_b = numpy.matrixlib.matrix(m_b)
    return m_a * m_b
