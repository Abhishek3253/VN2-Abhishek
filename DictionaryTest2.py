A= {10:56, 10:4, 20:1, 20:9, 30:1, 50:6}
B= {}
for x in A:
       if x in B:
            B[x] += 1
       else:
             B[x] = 1
print(B)

