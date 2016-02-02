Changelog
=========

2.0 - 2016-02-02
~~~~~~~~~~~~~~~~

* breaking change: All comparisons, other than `eq`, against other ordered sets
  are now performed unordered; i.e., they are treated as regular sets.
* `isorderedsubset` and `isorderedsuperset` have been added to perform ordered
  comparisons against other sequences. Using these methods with unordered
  collections wield yield arbitrary (and depending on Python implementation,
  unstable) results.

1.2 - 2015-09-29
~~~~~~~~~~~~~~~~

* bugfix: Set operations only worked with iterables if the OrderedSet was on the
  left-hand side. They now work both ways.
* bugfix: The order of an intersection was the right-hand side's order. It is now
  fixed to be the left-hand side's order.

1.1.2 - 2014-10-02
~~~~~~~~~~~~~~~~~~

* Make comparisons work with sets and lists, and not crash when compared with None.

1.1.1 - 2014-08-24
~~~~~~~~~~~~~~~~~~

* Add pickle/copy support to OrderedSet

1.1 - 2014-06-04
~~~~~~~~~~~~~~~~

* Make OrderedSets handle slicing in __getitem__().

1.0.2 - 2014-05-14
~~~~~~~~~~~~~~~~~~

* Add proper attribution and licenses.

1.0.1 - 2014-05-13
~~~~~~~~~~~~~~~~~~

* Don't require Cython to build an sdist.

1.0 - 2014-05-11
~~~~~~~~~~~~~~~~

* First implementation.
