#!/usr/bin/python3

def get_matrix_sizes(matrix, name):
    '''Checks the validity of a matrix and returns its dimensions.
    Args:
        matrix (list): The matrix.
        name (str): The name of the matrix.
    Returns:
        list: The rows and columns of the given matrix.
    Raises:
        ValueError: If the matrix is empty or invalid.
        TypeError: If the matrix or any of its elements are not of the correct type.
    '''
    if not matrix:
        raise ValueError(f'{name} cannot be empty')
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError(f'{name} must be a list of lists')
    if not all(map(lambda row: all(isinstance(cell, (int, float)) for cell in row), matrix)):
        raise TypeError(f'All elements of {name} must be integers or floats')
    if not all(map(lambda row: len(row) == len(matrix[0]), matrix)):
        raise ValueError(f'Each row of {name} must be of the same size')
    return len(matrix), len(matrix[0])


def matrix_mul(matrix_a, matrix_b):
    '''Multiplies two matrices.
    Args:
        matrix_a (list): The first matrix.
        matrix_b (list): The second matrix.
    Returns:
        list: The product matrix.
    Raises:
        ValueError: If the matrices have incompatible dimensions.
    '''
    rows_a, cols_a = get_matrix_sizes(matrix_a, 'matrix_a')
    rows_b, cols_b = get_matrix_sizes(matrix_b, 'matrix_b')

    if cols_a != rows_b:
        raise ValueError('matrix_a and matrix_b cannot be multiplied')

    product = []
    for row_a in matrix_a:
        product_row = []
        for col_b in range(cols_b):
            cell_sum = 0
            for i in range(cols_a):
                cell_sum += row_a[i] * matrix_b[i][col_b]
            product_row.append(cell_sum)
        product.append(product_row)

    return product
