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

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, collatz_cycleLength

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

    #   added by mchav05

    def test_read_2 (self) :
        s    = "0 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  0)
        self.assertEqual(j,  0)

    def test_read_3 (self) :
        s    = "7 8 9\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  7)
        self.assertEqual(j,  8)

    def test_read_4 (self) :
        s    = "999999      \t 1000000\t\t\t \n"
        i, j = collatz_read(s)
        self.assertEqual(i,  999999)
        self.assertEqual(j, 1000000)

    def test_read_5 (self) :
        s    = "-2 -3\n"
        i, j = collatz_read(s)
        self.assertEqual(i, -2)
        self.assertEqual(j, -3)


# ----
# cycleLength
# ----

    def test_cycleLength_1 (self) :
        c = collatz_cycleLength(1)
        self.assertEqual(c, 1)

    def test_cycleLength_2 (self) :
        c = collatz_cycleLength(666)
        self.assertEqual(c, 114)

    def test_cycleLength_3 (self) :
        c = collatz_cycleLength(11235)
        self.assertEqual(c, 87)
    """
    def test_eval_4 (self) :
        c = collatz_cycleLength(10)
        self.assertEqual(c, 1)
    """
    # end additions

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


    #   added by mchav05
    def test_eval_5 (self) :
        v = collatz_eval(24, 24)
        self.assertEqual(v, 11)

    def test_eval_6 (self) :
        v = collatz_eval(10000, 1)
        self.assertEqual(v, 262)

    """
    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 1)

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 1)

    TEST(CollatzFixture, eval_7) {
        const int v = collatz_eval(1, 999999);
        ASSERT_EQ(525, v);}

    TEST(CollatzFixture, eval_8) {
        const int v = collatz_eval(999999, 1);
        ASSERT_EQ(525, v);}
    """

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    #   added by mchav05
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 0, -1, -2)
        self.assertEqual(w.getvalue(), "0 -1 -2\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 1000000, 1000, 1000000000)
        self.assertEqual(w.getvalue(), "1000000 1000 1000000000\n")

#   end additions


    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    #   added by mchav05

    def test_solve_2 (self) :
        r = StringIO("1 1\n2 2\n 4 4\n8 8\n 16 16\n 32 32\n 64 64\n 128 128\n 256 256\n 512 512\n 1024 1024\n 2048 2048\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n2 2 2\n4 4 3\n8 8 4\n16 16 5\n32 32 6\n64 64 7\n128 128 8\n256 256 9\n512 512 10\n1024 1024 11\n2048 2048 12\n")

    def test_solve_3 (self) :
        r = StringIO("10 1\n200 100\n210 200\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 200 89\n1000 900 174\n")

    def test_solve_4 (self) :
        r = StringIO("1   1  1\n1   1   1\n1      1          1  1  1\n1      1    1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 1 1\n1 1 1\n1 1 1\n1 1 1\n")

#   end additions


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
