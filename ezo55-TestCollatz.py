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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length, collatz_check_order, collatz_check_range

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :

    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "10 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j, 10)

    def test_read_3 (self) :
        s    = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10)
        self.assertEqual(j,  1)

    def test_read_4 (self) :
        s    = "-1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j,  1)

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

    # ----
    # check_order
    # ----

    def test_check_order_1 (self) :
        a = [0,10]        
        collatz_check_order(a)
        self.assertEqual(a,[0,10])

    def test_check_order_2 (self) :
        a = [10,0]        
        collatz_check_order(a)
        self.assertEqual(a,[0,10])

    def test_check_order_3 (self) :
        a = [10,0]        
        collatz_check_order(a)
        self.assertEqual(a.index(10),1)

    # ----
    # check_range
    # ----

    def test_check_range_1 (self) :
        a = [0,10]        
        collatz_check_range(a)
        self.assertEqual(a,[6,10])

    def test_check_range_2 (self) :
        a = [10,99]        
        collatz_check_range(a)
        self.assertEqual(a,[50,99])

    def test_check_range_3 (self) :
        a = [51,99]
        collatz_check_range(a)
        self.assertEqual(a,[51,99])

    # ----
    # cycle_length
    # ----

    def test_cycle_length_1 (self) :
        v = collatz_cycle_length(1)
        self.assertEqual(v, 1)

    def test_cycle_length_2 (self) :
        v = collatz_cycle_length(5)
        self.assertEqual(v, 6)

    def test_cycle_length_3 (self) :
        v = collatz_cycle_length(10)
        self.assertEqual(v, 7)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 3, 2, 1)
        self.assertEqual(w.getvalue(), "3 2 1\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 999999, 0, 8)
        self.assertEqual(w.getvalue(), "999999 0 8\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) : 
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("1 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_solve_3 (self) :
        r = StringIO("10 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n")

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
