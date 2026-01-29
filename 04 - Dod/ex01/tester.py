from in_out import ft_square, ft_outer, ft_pow


def main():
	ft_counter = ft_outer(3, ft_square)
	print(ft_counter())
	print(ft_counter())
	print(ft_counter())
	print("---")

	another_counter = ft_outer(1.5, ft_pow)
	print(another_counter())
	print(another_counter())
	print(another_counter())

	# Additional edge-case tests
	print("---")
	# Test with negative number
	neg_counter = ft_outer(-2, ft_square)
	print(neg_counter())
	print(neg_counter())

	# Test with zero
	zero_counter = ft_outer(0, ft_pow)
	print(zero_counter())

	# Test with float and custom function
	def plus_one(x):
		return x + 1
	plus_counter = ft_outer(1.5, plus_one)
	print(plus_counter())
	print(plus_counter())

	# Test that counter is persistent
	persistent = ft_outer(2, ft_square)
	print(persistent())
	print(persistent())
	print(persistent())


if __name__ == "__main__":
    main()
