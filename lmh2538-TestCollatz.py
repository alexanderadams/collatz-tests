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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_calc

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
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)

    # -----
    # calc
    # -----

    def test_calc_1(self) :
        v = collatz_calc(10)
        self.assertEqual(v, 7)

    def test_calc_2(self) :
        v = collatz_calc(100)
        self.assertEqual(v, 26)

    def test_calc_3(self) :
        v = collatz_calc(172583)
        self.assertEqual(v, 197)

    def test_calc_4(self) :
        v = collatz_calc(999999)
        self.assertEqual(v, 259)

    def test_calc_5(self) :
        v = collatz_calc(1)
        self.assertEqual(v, 1)

    def test_calc_6(self) :
        v = collatz_calc(2)
        self.assertEqual(v, 2)

    def test_calc_7(self) :
        v = collatz_calc(3489)
        self.assertEqual(v, 88)

    def test_calc_8(self) :
        v = collatz_calc(123456)
        self.assertEqual(v, 62)

    def test_calc_9(self) :
        v = collatz_calc(55)
        self.assertEqual(v, 113)

    def test_calc_10(self) :
        v = collatz_calc(55)
        self.assertEqual(v, 113)    

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
