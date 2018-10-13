=====
Usage
=====

To use Squashem in a project::

    import squashem

Or::

    from squashem import squashem

Then you can use the function ``squashem`` as follows.
If you used the first import above, use ``squashem.squashem``::

    matrix = [[1, 2, 3], [4, 5, 6]]
    new_list = squashem(matrix)

At this point, ``new_list`` will contain ``[1, 2, 3, 4, 5, 6]``.
