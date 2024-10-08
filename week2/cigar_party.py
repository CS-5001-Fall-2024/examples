"""
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
"""
LOW_BOUNDARY = 40
HIGH_BOUNDARY = 60


def cigar_party(cigars: int, is_weekend: bool) -> bool:
	"""Return True if the party is successful and False
	otherwise.
	"""
	return not ((cigars < LOW_BOUNDARY)
	 or (cigars > HIGH_BOUNDARY and not is_weekend))

	# if ((cigars < LOW_BOUNDARY) 
	#  or (cigars > HIGH_BOUNDARY and not is_weekend)):
	# 	return False
	# return True


	# if cigars < LOW_BOUNDARY:
	# 	return False
	# elif cigars > HIGH_BOUNDARY and not is_weekend:
	# 	return False
	# else:
	# 	return True


	# if cigars < LOW_BOUNDARY:
	# 	return False
	# elif cigars > HIGH_BOUNDARY and is_weekend:
	# 	return True
	# elif cigars > HIGH_BOUNDARY and not is_weekend:
	# 	return False
	# else:
	# 	return True

def main():
 	# How many tests do we need to do
	# to ensure that our function
	# is correct?
	print(cigar_party(39, True))
	print(cigar_party(39, False))
	print(cigar_party(61, True))
	print(cigar_party(618, True))

	print(cigar_party(61, False))
	print(cigar_party(618, False))
	print(cigar_party(45, True))
	print(cigar_party(45, False))

	print(cigar_party(40, True))
	print(cigar_party(40, False))
	print(cigar_party(60, True))
	print(cigar_party(60, False))
	print(cigar_party(-60, False))

if __name__ == '__main__':
	main()