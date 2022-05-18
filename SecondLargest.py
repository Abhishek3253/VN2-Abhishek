#Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given  scores.
#Store them in a list and find the score of the runner-up.

N= input()
L= input().split()
I=[] 
assert N>=2 and N<=10 
for i in L: 
    I.append(int(i)) 
    I.sort() 
    largest=max(I) 
    count=I.count(largest) 
for i in range(count): 
    I.remove(largest) 
print max(I)

