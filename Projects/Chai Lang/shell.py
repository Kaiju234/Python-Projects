import chai

while True:
	text = input('Chai > ')
	result, error = chai.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)