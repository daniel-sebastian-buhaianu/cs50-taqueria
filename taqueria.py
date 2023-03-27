menu = {
	"Baja Taco": 4.00,
	"Burrito": 7.50,
	"Bowl": 8.50,
	"Nachos": 11.00,
	"Quesadilla": 8.50,
	"Super Burrito": 8.50,
	"Super Quesadilla": 9.50,
	"Taco": 3.00,
	"Tortilla Salad": 8.00
}

# convert all dict keys to lowercase
menu = {item.lower(): price for item, price in menu.items()}

# initialize order's total
total = 0.00

# Ask for input until user inputs CTRL+D
while True:
	try:
		# store user's input in lower case
		item = input("Item: ").lower()

		# check if item is in menu
		if item in menu.keys():
			# update total
			total += menu[item]
			format_total = "{:.2f}".format(total)
			print(f"Total: ${format_total}")

	# catch CTRL+D
	except EOFError:
		break


