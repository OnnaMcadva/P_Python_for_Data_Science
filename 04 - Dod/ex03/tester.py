from new_student import Student


def main():
	student1 = Student(name="Edward", surname="agle")
	print(student1)

	# Additional edge-case tests
	try:
		student2 = Student(name="Edward", surname="agle", id="toto")
	except Exception as e:
		print("Error:", e)

	# Test with different cases
	student3 = Student(name="ALICE", surname="Smith")
	print(student3)

	# Test with empty surname
	try:
		student4 = Student(name="Bob", surname="")
		print(student4)
	except Exception as e:
		print("Error:", e)

	# Test that login and id cannot be changed
	student5 = Student(name="Charlie", surname="Brown")
	try:
		student5.login = "hack"
	except Exception as e:
		print("Error:", e)
	try:
		student5.id = "hackid"
	except Exception as e:
		print("Error:", e)

	# Test that id is always 15 characters
	print("ID length:", len(student5.id))

if __name__ == "__main__":
	main()