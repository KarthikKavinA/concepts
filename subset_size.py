'''The number of subsets of size k of a set of size n (also called an n-set) is
C(n,k) = P(n,k)/k!    =     n!/(k!*(n−k)!)    =  (nk).     pronounced as "n choose k".'''




'''To find occurence of any number (assume=5) chosen from set ,then its probability (times) of
occurences in sub-set is ===(nk)*k/n  ------refer above'''





'''l=[1,2,3,4,5,6,7,8,9]
   c=itertools.combinations(l,2)
   
   (1, 2) (1, 3) (1, 4) (1, 5) (1, 6) (1, 7) (1, 8) (1, 9) (2, 3) (2, 4) (2, 5) (2, 6) (2, 7)
   (2, 8) (2, 9) (3, 4) (3, 5) (3, 6) (3, 7) (3, 8) (3, 9) (4, 5) (4, 6) (4, 7) (4, 8) (4, 9)
   (5, 6) (5, 7) (5, 8) (5, 9) (6, 7) (6, 8) (6, 9) (7, 8) (7, 9) (8, 9)

   total no of sub-sets(chosen 2 from 9)====36

   total occurence of any no in a sub-set (no=5=assumption=chosen from set)====8'''


   


import math as m
n=int(input("Enter set size:"))
k=int(input("Enter sub-set size:"))

n1=m.factorial(n)
d1=m.factorial(k)
t=n-k
d2=m.factorial(t)

ss=n1//(d1*d2)

sss=ss*k//n

print("The no of subsets(k) in set(n) is: ",ss)

print("Total no of times,the number occured in sub-set is: ",sss)
