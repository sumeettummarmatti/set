"""Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8} Intersection of E and N is {2, 4} Difference of E and N is {8, 0, 6} Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}
"""


n1=int(input("Enter the no. of inputs to put in set 1 "))
n2=int(input("Enter the no. of inputs to put in set 2 "))
set1=set()
set2=set()
for i in range(n1):
    set1.add(input())
for i in range(n2):
    set2.add(input())



print("UNION: ",set1.union(set2))
print("INTERSECTION: ",set1.intersection(set2))
print("DIFFERENCE: ",set1.difference(set2))
print("SYMM DIFFERENCE: ",set1.symmetric_difference(set2))





