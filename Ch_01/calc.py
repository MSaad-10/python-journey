''' =========== Mathematical Operations =========== '''

# Floating Point Division /
print(f"2/4:\t{2/4}")
print(f"4/2:\t{4/2}")
print(f"1/3:\t{1/3}")

# Intger Division //
print(f"4//2:\t{4//2}")
print(f"2//4:\t{2//4}")   # floor function will be used

# Exponent **
print(f"2**3:\t{2**3}")
print(f"2**0.5:\t{2**0.5}")   # square root
print(f"Round:\t{round(2**0.5, 2)}")   # round to 2 places
print(f"8**0.33:\t{8**0.3333333333333333}")   # cube root

# Modulus %
print(f"3%2:\t{3%2}")
print(f"2%6:\t{2%6}")
print(f"0%4:\t{0%4}")

# Multiplication *
print(f"2*3:\t{2*3}")
print(f"4*5:\t{4*5}")

# Addition +
print(f"2+3:\t{2+3}")
print(f"10+3:\t{10+3}")

# Subtraction -
print(f"3-5:\t{3-5}")
print(f"10-5:\t{10-5}")

''' =========== Precedence & Associativity Rule =========== '''

print((2+3)*5/2%6)
print(2**3**2)   # Right -> Left


#   OPERATORS               PRECEDENCE
#   ---------               ----------
#   Paranthesis ()          Highest
#   Exponent **             Right -> Left
#   *,/,//,%                Left  -> Right
#   +,-                     Left  -> Right 