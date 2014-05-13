===========
Ordered Set
===========

.. image:: https://badge.fury.io/py/orderedset.png
    :target: http://badge.fury.io/py/orderedset

.. image:: https://travis-ci.org/simonpercivall/orderedset.png?branch=master
    :target: https://travis-ci.org/simonpercivall/orderedset

.. image:: https://pypip.in/d/orderedset/badge.png
    :target: https://crate.io/packages/orderedset?version=latest


An Ordered Set implementation in Cython. Based on `Raymond Hettinger's OrderedSet recipe`_.

Example::

    >>> from orderedset import OrderedSet
    >>> oset = OrderedSet([1, 2, 3])
    >>> oset
    OrderedSet([1, 2, 3])
    >>> oset | [5, 4, 3, 2, 1]
    OrderedSet([1, 2, 3, 5, 4])

* Free software: BSD license
* Documentation: http://orderedset.rtfd.org.

Features
--------

* Works like a regular set, but remembers insertion order;
* Is approximately 5 times faster than the pure Python implementation overall
  (and 5 times slower than :class:`set`);
* Compatible with Python 2.6 through 3.4.;
* Supports the full set interface;
* Supports some list methods, like :meth:`index` and :meth:`__getitem__`.

.. _`Raymond Hettinger's OrderedSet recipe`: http://code.activestate.com/recipes/576694/
