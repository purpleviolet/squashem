# -*- coding: utf-8 -*-

"""Main module."""


def squashem(matrix):
    """Return squashed list from 2D list of lists"""
    return [
        item
        for row in matrix
        for item in row
    ]
