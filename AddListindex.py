A = [1, 3, 4, 6, 8]
B = [4, 5, 6, 2, 10]

print("List A : " + str(A))
print("List B : " + str(B))

C = []
for i in range(0, len(A)):
       C.append(A[i] + B[i])

print("Added resulatnt List id : " + str(C))