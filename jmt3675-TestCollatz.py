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

import Collatz # We need the module name to access Collatz.lookup
from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, calc_cycle, process_queue, update_meta_range

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
        s   = "900 1000\n"
        i,j = collatz_read(s)
        self.assertEqual(i, 900)
        self.assertEqual(j, 1000)

    def test_read_3 (self) :
        s   = "0 0\n"
        i,j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)

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
        self.assertEqual(v, 20);

    def test_eval_6 (self) :
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125)

    def test_eval_7 (self) :
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174)
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
    
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 2, 3)
        self.assertEqual(w.getvalue(), "1 2 3\n")

    def test_print_3 (self) :
        w = StringIO()
        a,b,c = 10,20,30
        collatz_print(w, a, b, c)
        self.assertEqual(w.getvalue(), "10 20 30\n")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("10 1\n200 100\n210 201\n1000 900\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "10 1 20\n200 100 125\n210 201 89\n1000 900 174\n")

    # -------------
    # process_queue
    # -------------
    def test_proc_queue_1 (self) :
        q = [10,5,16,8,4,2]
        v = 7

        process_queue(q,v)

        self.assertEqual(Collatz.lookup[10], 7)
        self.assertEqual(Collatz.lookup[5], 6)
        self.assertEqual(Collatz.lookup[16],5)
        self.assertEqual(Collatz.lookup[8],4)
        self.assertEqual(Collatz.lookup[4],3)
        self.assertEqual(Collatz.lookup[2],2)
        
    def test_proc_queue_2 (self) :
        q = [20,10]
        v = 8
        
        process_queue(q,v)

        self.assertEqual(Collatz.lookup[20], 8)
        self.assertEqual(Collatz.lookup[10], 7)
        
    # -----------------
    # update_meta_range
    # -----------------
    def test_update_meta_1 (self) :
        i = 1
        j = 3001
        r = []
        ranges = update_meta_range(i,j,r)
        self.assertEqual(ranges, [(3000,3001)])
        self.assertEqual(r, [Collatz.meta_cache[0], Collatz.meta_cache[1], Collatz.meta_cache[2]])

    def test_update_meta_2 (self) :
        i = 1
        j = 10
        r = []
        ranges = update_meta_range(i,j,r)
        self.assertEqual(ranges, [(1,10)])
        self.assertEqual(r, [])

    def test_update_meta_3 (self) :
        i = 372
        j = 2101
        r = []
        ranges = update_meta_range(i,j,r)
        self.assertEqual(ranges, [(372,1000),(2000, 2101)])
        self.assertEqual(r, [Collatz.meta_cache[1]])

    def test_update_meta_4 (self) :
        i = 900
        j = 1000
        r = []
        ranges = update_meta_range(i,j,r)
        self.assertEqual(ranges, [(900,1000)])
        self.assertEqual(r, [])

# ----------
# calc_cycle
# ----------
    def test_calc_cycle_1 (self) :
        self.assertEqual(calc_cycle(10), 7)

    def test_calc_cycle_2 (self) :
        cycles = []
        for i in range(1, 10+1) :
            cycles.append(calc_cycle(i))

        self.assertEqual(max(cycles), 20)
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
