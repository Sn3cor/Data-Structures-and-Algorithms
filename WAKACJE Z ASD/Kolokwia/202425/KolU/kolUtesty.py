# kolUtesty.py
from testy import *
from kolUtest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return arg #deepcopy(arg)


def printarg(T, k):
    print("Kwiatki w doniczkach:\t", limit(T))
    print("Maksymalna liczba kwiatów w doniczce: ", k)


def printhint( hint ):
    print("Wynik poprawny:\t\t", hint)


def printsol( sol ):
    print("Wynik algorytmu:\t", sol)


def check( T, hint, sol ):
    return hint == sol

def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    T =  [2, 7, 8, 4]
    k =  10
    newtest = {}
    newtest["arg"] = (T, k)
    k=2
    newtest["hint"] = k
    TESTS.append(newtest)

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)
#        print(TESTS)
#    print(TESTS)
    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

