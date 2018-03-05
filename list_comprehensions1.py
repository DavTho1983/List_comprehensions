# [expr for val in collection]

# [expr for val in collection if <test>]

# [expr for val in collection if <test1> and <test2>]

# [expr for val1 in collection1 and val2 in collection2]

# List of squares of first 100 +ve integers

squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

# List of remainders when you divide 100 squares by 5
remainder5 = [x**2 % 5 for x in range(1, 101)]
print(remainder5)

# List of remainders when you divide 100 squares by 11
remainder11 = [x**2 % 11 for x in range(1, 101)]
print(remainder11)
