cart = []

def alphabetical():
	global cart
	cart.sort()
	return cart

def shopping_list(thing):
	global cart
	thing = thing.lower()

	if thing in cart:
		print thing + " is already in the cart!"
	else:
		cart.append(thing)
	return alphabetical()


def item_back(unwantedthing):
	global cart
	unwantedthing = unwantedthing.lower()

	if unwantedthing in cart:
		cart.remove(unwantedthing)
	else:
		print unwantedthing + " is NOT in the cart!"
	return alphabetical()


def main():
	print shopping_list('zoo')
	print shopping_list('grapefruit')
	print shopping_list('peacHY')
	print shopping_list('ZOO')
	print shopping_list('apple')

	print item_back('orange')
	print item_back('apple')

if __name__ == '__main__':
	main()