=====
Usage
=====

To use OrderedSet in a project::

    from orderedset import OrderedSet

    oset = OrderedSet([1, 2, 3])
    oset2 = OrderedSet([3, 2, 1])
    oset3 = OrderedSet([1, 2, 3, 4])

    oset == oset2  # False
    oset <= oset2  # True, same as issubset


OrderedSet normally compares like a set, but can be made to make
ordered sub-/superset comparisons::

    oset.isorderedsubset(oset2)  # False
    oset.isorderedsubset(oset3)  # True


OrderedSets work with other sets, and with lists::

    from orderedset import OrderedSet

    oset = OrderedSet([1, 2, 3])
    lst = [1, 2, 3]
    tes = {1, 2, 3}

    oset <= lst  # True
    oset <= tes  # True

    oset | lst  # OrderedSet([1, 2, 3])
    oset | tes  # OrderedSet([1, 2, 3])
