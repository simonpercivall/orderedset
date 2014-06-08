#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_orderedset
----------------------------------

Tests for `orderedset` module.
"""
import sys

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
import weakref
import gc

from orderedset import *


class TestOrderedset(unittest.TestCase):

    def setUp(self):
        self.lst = list(range(10))

    def test_add_new(self):
        oset = OrderedSet(self.lst)
        lst = self.lst

        item = 10
        lst.append(item)
        oset.add(item)

        self.assertEqual(list(oset), lst)

    def test_add_existing(self):
        oset = OrderedSet(self.lst)
        lst = self.lst

        oset.add(1)
        oset.add(3)
        self.assertEqual(list(oset), lst)

    def test_discard(self):
        oset = OrderedSet([1, 2, 3])

        oset.discard(1)
        self.assertNotIn(1, oset)

        oset.discard(4)

    def test_pop(self):
        oset = OrderedSet([1, 2, 3])

        v = oset.pop()
        self.assertEqual(v, 3)
        self.assertNotIn(v, oset)

        v = oset.pop(last=False)
        self.assertEqual(v, 1)
        self.assertNotIn(v, oset)

    def test_remove(self):
        oset = OrderedSet(self.lst)
        lst = self.lst

        oset.remove(3)
        lst.remove(3)

        self.assertEqual(list(oset), lst)

    def test_clear(self):
        val = frozenset([1])

        oset = OrderedSet()
        ws = weakref.WeakKeyDictionary()

        oset.add(val)
        ws[val] = 1
        oset.clear()

        self.assertEqual(list(oset), [])

        del val
        gc.collect()
        self.assertEqual(list(ws), [])

    def test_copy(self):
        oset1 = OrderedSet(self.lst)
        oset2 = oset1.copy()

        self.assertIsNot(oset1, oset2)
        self.assertEqual(oset1, oset2)

        oset1.clear()
        self.assertNotEqual(oset1, oset2)

    def test_difference_and_update(self):
        oset1 = OrderedSet([1, 2, 3])
        oset2 = OrderedSet([3, 4, 5])

        oset3 = oset1 - oset2
        self.assertEqual(oset3, OrderedSet([1, 2]))

        self.assertEqual(oset1.difference(oset2), oset3)

        oset4 = oset1.copy()
        oset4 -= oset2
        self.assertEqual(oset4, oset3)

        oset5 = oset1.copy()
        oset5.difference_update(oset2)
        self.assertEqual(oset5, oset3)

    def test_intersection_and_update(self):
        oset1 = OrderedSet([1, 2, 3])
        oset2 = OrderedSet([3, 4, 5])

        oset3 = oset1 & oset2
        self.assertEqual(oset3, OrderedSet([3]))

        oset4 = oset1.copy()
        oset4 &= oset2

        self.assertEqual(oset4, oset3)

        oset5 = oset1.copy()
        oset5.intersection_update(oset2)
        self.assertEqual(oset5, oset3)

    def test_issubset(self):
        oset1 = OrderedSet([1, 2, 3])
        oset2 = OrderedSet([1, 2])

        self.assertTrue(oset2 < oset1)
        self.assertTrue(oset2.issubset(oset1))

        oset2 = OrderedSet([1, 2, 3])
        self.assertTrue(oset2 <= oset1)
        self.assertTrue(oset1 <= oset2)
        self.assertTrue(oset2.issubset(oset1))

        oset2 = OrderedSet([1, 2, 3, 4])
        self.assertFalse(oset2 < oset1)
        self.assertFalse(oset2.issubset(oset1))
        self.assertTrue(oset1 < oset2)

    def test_issuperset(self):
        oset1 = OrderedSet([1, 2, 3])
        oset2 = OrderedSet([1, 2])

        self.assertTrue(oset1 > oset2)
        self.assertTrue(oset1.issuperset(oset2))

        oset2 = OrderedSet([1, 2, 3])
        self.assertTrue(oset1 >= oset2)
        self.assertTrue(oset2 >= oset1)
        self.assertTrue(oset1.issubset(oset2))

        oset2 = OrderedSet([1, 2, 3, 4])
        self.assertFalse(oset1 > oset2)
        self.assertFalse(oset1.issuperset(oset2))
        self.assertTrue(oset2 > oset1)

    def test_symmetric_difference_and_update(self):
        oset1 = OrderedSet([1, 2, 3])
        oset2 = OrderedSet([2, 3, 4])

        oset3 = oset1 ^ oset2
        self.assertEqual(oset3, OrderedSet([1, 4]))

        oset4 = oset1.copy()
        self.assertEqual(oset4.symmetric_difference(oset2), oset3)

        oset4 ^= oset2
        self.assertEqual(oset4, oset3)

        oset5 = oset1.copy()
        oset5.symmetric_difference_update(oset2)
        self.assertEqual(oset5, oset3)

    def test_union_and_update(self):
        oset = OrderedSet(self.lst)
        lst = self.lst

        oset2 = oset | [3, 9, 27]
        self.assertEqual(oset2, lst + [27])

        # make sure original oset isn't changed
        self.assertEqual(oset, lst)

        oset1 = OrderedSet(self.lst)
        oset2 = OrderedSet(self.lst)

        oset3 = oset1 | oset2
        self.assertEqual(oset3, oset1)

        self.assertEqual(oset3, oset1.union(oset2))

        oset1 |= OrderedSet("abc")
        self.assertEqual(oset1, oset2 | "abc")

        oset1 = OrderedSet(self.lst)
        oset1.update("abc")
        self.assertEqual(oset1, oset2 | "abc")

    def test_index(self):
        oset = OrderedSet("abcd")
        self.assertEqual(oset.index("b"), 1)

    def test_getitem(self):
        oset = OrderedSet("abcd")
        self.assertEqual(oset[2], "c")

    def test_getitem_slice(self):
        oset = OrderedSet("abcdef")
        self.assertEqual(oset[:2], OrderedSet("ab"))
        self.assertEqual(oset[2:], OrderedSet("cdef"))
        self.assertEqual(oset[::-1], OrderedSet("fedcba"))
        self.assertEqual(oset[1:-1:2], OrderedSet("bd"))
        self.assertEqual(oset[1::2], OrderedSet("bdf"))

    def test_len(self):
        oset = OrderedSet(self.lst)
        self.assertEqual(len(oset), len(self.lst))

        oset.remove(0)
        self.assertEqual(len(oset), len(self.lst) - 1)

    def test_contains(self):
        oset = OrderedSet(self.lst)
        self.assertTrue(1 in oset)

    def test_iter_mutated(self):
        oset = OrderedSet(self.lst)
        it = iter(oset)
        oset.add('a')

        with self.assertRaises(RuntimeError):
            next(it)

        it = reversed(oset)
        oset.add('b')

        with self.assertRaises(RuntimeError):
            next(it)

    def test_iter_and_valid_order(self):
        oset = OrderedSet(self.lst)
        self.assertEqual(list(oset), self.lst)

        oset = OrderedSet(self.lst + self.lst)
        self.assertEqual(list(oset), self.lst)

    def test_reverse_order(self):
        oset = OrderedSet(self.lst)
        self.assertEqual(list(reversed(oset)), list(reversed(self.lst)))

    def test_repr(self):
        oset = OrderedSet([1])
        self.assertEqual(repr(oset), "OrderedSet([1])")

    def test_eq(self):
        oset1 = OrderedSet(self.lst)
        oset2 = OrderedSet(self.lst)

        self.assertEqual(oset1, oset2)


if __name__ == '__main__':
    unittest.main()
