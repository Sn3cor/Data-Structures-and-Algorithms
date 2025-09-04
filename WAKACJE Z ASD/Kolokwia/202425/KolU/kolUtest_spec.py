from testy import MY_random, MY_modulus
ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n, k, hint
  (10, 2, 6),
  (20, 5, 76),
  (40, 8, 310),
  (50, 10, 659),
  (100, 20, 2588),
  (1000, 30, 239011),
  (10000, 30, 24124248),
  (100000, 30, 2410043373),
  (1000000, 20, 237655278427),
  (5000000, 5, 5002992734165),
]




def gentest(n, k, hint):
    from testy import MY_random
    T = []
    for i in range(n):
        a = int(MY_random()/MY_modulus*k)+1
        T.append(a)
    return (T, k), hint





    
