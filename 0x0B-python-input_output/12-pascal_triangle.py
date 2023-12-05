#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(d):
    """Represent Pascal's Triangle of size d.

    Returns a list of lists of integers representing the triangle.
    """
    if d <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != d:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
