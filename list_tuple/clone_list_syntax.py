A = "A,B,C,D".split(",")

print("A", A)

B = A
print("after copying A to  B", B)
B[0] = 'manoj'
print("after copying of A to B and modification in B, A", A)
print("after copying of A to  B and modification in B, B", B)

B = A[:]

print("after clone B", B)
B[0] = 'manish'
print("after cloning of A to B and modification in B, List A is ", A)
print("after cloning of A to B and modification in B, List B is ", B)
