#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascals triangle of n
    """
    list = []
    if n <= 0:
        return list
    list.append([1])
    for i in range(n - 1):
        list.append([1] + [list[i][j] + list[i][j + 1]
                    for j in range(len(list[i]) - 1)] + [1])
    return list


if __name__ == "__main__":
    pascal_triangle(n)
