def is_adult(age):
	if age >= 18:
		return True
	else:
		return False

ages = [12,17, 18, 25, 67]

for age in ages:
	if is_adult(age):
		print(f"{age} is an adult")
	else:
		print (f"{age} is not an adult")

