A = "A,B,C,D".split(",")

print("A", A)

B = A
print("Shallow copy after copying A to  B", B)
B[0] = 'manoj'
print("after copying of A to B and modification in B B[0] = 'manoj' , A", A)
print("after copying of A to  B and modification in B, B", B)

B = A[:] # deep copy

print("Deep copy after clone B", B)
B[0] = 'manish'
print("after cloning of A to B and modification in B (added manish), List A is ", A)
print("after cloning of A to B and modification in B, List B is ", B)
