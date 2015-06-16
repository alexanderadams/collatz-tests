#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, max_cycle_length, cycle_length

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s = "10 5\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 5)

    # ----------------
    # max_cycle_length
    # ----------------
    def test_max_1 (self) :
        a = [1,2,3,4,5]
        v = max_cycle_length(a)
        self.assertEqual(v, 5)

    def test_max_2 (self) :
        a = [2,15,3,15,7]
        v = max_cycle_length(a)
        self.assertEqual(v, 15)

    def test_max_3 (self) :
        a = [5,4,3,2,1]
        v = max_cycle_length(a)
        self.assertEqual(v, 5)

    def test_max_4 (self) :
        a = [4]
        v = max_cycle_length(a)
        self.assertEqual(v,4)


    # ------------
    # cycle_length
    # ------------
    def test_cycle_1 (self) :
        v = cycle_length(5)
        self.assertEqual(6, v)

    def test_cycle_2(self) :
        v = cycle_length(10)
        self.assertEqual(7, v)

    def test_cycle_3(self) :
        v = cycle_length (3)
        self.assertEqual(8, v)

    def test_cycle_4(self) :
        v = cycle_length (1)
        self.assertEqual(1, v)
    
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v,1)

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
