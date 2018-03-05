v = [2, -3, 1]
print(4*v) #wrong thing - this concatenates 4 copies of v

#scalar multiplication *4
w = [4*x for x in v]
print(w)

#Cartesian Product
#If A and B are sets,
#the Cartesian Product
#is the set of pairs (a, b)
#where 'a' is in A and 'b' is in B

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)

u = [(a * b) for a in A for b in B]
print(u)
