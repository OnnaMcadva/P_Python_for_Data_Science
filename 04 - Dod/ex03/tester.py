from new_student import Student


def main():
	student1 = Student(name="Edward", surname="agle")
	print(student1)

	# Additional edge-case tests
	try:
		student2 = Student(name="Edward", surname="agle", id="toto")
		print(student2)
	except Exception as e:
		print("Error:", e)
	
	try:
		student6 = Student(name="Edward", surname="agle", login="toto")
		print(student6)
	except Exception as e:
		print("Error:", e)

	try:
		student7 = Student(name="Edward", surname="agle", toto="extra")
		print(student7)
	except Exception as e:
		print("Error:", e)

	# Test with different cases
	student3 = Student(name="aLICE", surname="Smith")
	print(student3)

	# Test with empty surname
	try:
		student4 = Student(name="Bob", active=False, surname="")
		print(student4)
	except Exception as e:
		print("Error:", e)

	# Test that login and id cannot be changed
	student5 = Student(name="Bob", surname="Lee")
	print(student5)
	try:
		student5.login = "hack"
	except Exception as e:
		print("Error:", e)
	try:
		student5.id = "hackid"
	except Exception as e:
		print("Error:", e)
	print(student5)
	print(student5.login, "'s ID length still", len(student5.id))

if __name__ == "__main__":
	main()