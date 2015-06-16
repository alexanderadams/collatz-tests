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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycle_length, collatz_maxcl

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

 
    def test_read2 (self) :
        s    = "10 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10)
        self.assertEqual(j, 10)


    def test_read3 (self) :
        s    = "10 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  10)
        self.assertEqual(j, 1)


    def test_read4 (self) :
        s    = "100 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 10)

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
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    def test_eval_7 (self) :
        v = collatz_eval(210, 201)
        self.assertEqual(v, 89)

    # ----
    # cycle_length
    # ----

    def test_cyclelength1 (self) :
        c = collatz_cycle_length(1)
        self.assertEqual(c, 1)

    def test_cyclelength2 (self) :
        c = collatz_cycle_length(5)
        self.assertEqual(c, 6)

    def test_cyclelength3 (self) :
        c = collatz_cycle_length(10)
        self.assertEqual(c, 7)

    def test_cyclelength4 (self) :
        c = collatz_cycle_length(704)
        self.assertEqual(c, 21)

    def test_cyclelength5 (self) :
        c = collatz_cycle_length(2)
        self.assertEqual(c, 2)

    # ----
    # maxcl
    # ----

    def test_maxcl1 (self) :
        m = collatz_maxcl(1, 10)
        self.assertEqual(m, 20)

    def test_maxcl2 (self) :
        m = collatz_maxcl(100, 200)
        self.assertEqual(m, 125)

    def test_maxcl3 (self) :
        m = collatz_maxcl(201, 210)
        self.assertEqual(m, 89)

    def test_maxcl4 (self) :
        m = collatz_maxcl(900, 1000)
        self.assertEqual(m, 174)

    def test_maxcl5 (self) :
        m = collatz_maxcl(1, 1)
        self.assertEqual(m, 1)

    def test_maxcl6 (self) :
        m = collatz_maxcl(10, 11)
        self.assertEqual(m, 15)

    def test_maxcl7 (self) :
        m = collatz_maxcl(1, 2)
        self.assertEqual(m, 2)
   
    def test_maxcl8 (self) :
        m = collatz_maxcl(10, 10)
        self.assertEqual(m, 7)
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print2 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print3 (self) :
        w = StringIO()
        collatz_print(w, 210, 201, 89)
        self.assertEqual(w.getvalue(), "210 201 89\n")

    def test_print4 (self) :
        w = StringIO()
        collatz_print(w, 1, 2, 2)
        self.assertEqual(w.getvalue(), "1 2 2\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve2 (self) :
        r = StringIO("1 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_solve3 (self) :
        r = StringIO("1 2\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 2 2\n")

    def test_solve4 (self) :
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

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
