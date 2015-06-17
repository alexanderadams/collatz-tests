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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20) # fixed

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)# fixed

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)# fixed

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)# fixed

    def test_eval_5 (self) :
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)# fixed

    def test_eval_6 (self) :
        v = collatz_eval(11, 11)
        self.assertEqual(v, 15)# fixed

    def test_eval_7 (self) :
        v = collatz_eval(200, 1)
        self.assertEqual(v, 125)# fixed

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 9, 10, 11)
        self.assertEqual(w.getvalue(), "9 10 11\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 0, 0, 0)
        self.assertEqual(w.getvalue(), "0 0 0\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 6, 66, 666)
        self.assertEqual(w.getvalue(), "6 66 666\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self):
        s = "1 2\n2 3\n3 4\n4 5\n"
        r = StringIO(s)
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 2 2\n2 3 8\n3 4 8\n4 5 6\n")#fixed

    def test_solve_3 (self):
        s = "666 1\n1 666\n3 4\n666 999\n"
        r = StringIO(s)
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "666 1 145\n1 666 145\n3 4 8\n666 999 179\n")#fixed

    def test_solve_4 (self):
        s = "12345 54321\n1337 80085\n2525 1701\n2345 2344\n"
        r = StringIO(s)
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "12345 54321 340\n1337 80085 351\n2525 1701 209\n2345 2344 152\n")#fixed


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
