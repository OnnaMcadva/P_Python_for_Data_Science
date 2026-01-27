from in_out import outer, square, pow

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")

another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())

# Additional edge-case tests
print("---")
# Test with negative number
neg_counter = outer(-2, square)
print(neg_counter())
print(neg_counter())

# Test with zero
zero_counter = outer(0, pow)
print(zero_counter())

# Test with float and custom function
def plus_one(x):
	return x + 1
plus_counter = outer(1.5, plus_one)
print(plus_counter())
print(plus_counter())

# Test that counter is persistent
persistent = outer(2, square)
print(persistent())
print(persistent())
print(persistent())
