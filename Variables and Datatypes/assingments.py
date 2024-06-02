p,q,r = 1,2,3 # Correct the values of p,q,r

p,q = 1,2,3 # SyntaxError: cannot assign to literal

p,q,r = 1,2 # ValueError: not enough values to unpack (expected 3, got 2)

p = 1,2,3 # p is a tuple