from in_out import mysquare, myouter, mypow


def main():
	my_counter = myouter(3, mysquare)
	print(my_counter())
	print(my_counter())
	print(my_counter())
	print("---")

	another_counter = myouter(1.5, mypow)
	print(another_counter())
	print(another_counter())
	print(another_counter())

	# Additional edge-case tests
	print("---")
	# Test with negative number
	neg_counter = myouter(-2, mysquare)
	print(neg_counter())
	print(neg_counter())

	# Test with zero
	zero_counter = myouter(0, mypow)
	print(zero_counter())

	# Test with float and custom function
	def plus_one(x):
		return x + 1
	plus_counter = myouter(1.5, plus_one)
	print(plus_counter())
	print(plus_counter())

	# Test that counter is persistent
	persistent = myouter(2, mysquare)
	print(persistent())
	print(persistent())
	print(persistent())


if __name__ == "__main__":
    main()
