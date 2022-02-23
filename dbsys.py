import mariadb as mysqlconnector

connect = mysqlconnector.connect(
	user = "root",
	password = "12345678",
	host = "localhost",
	db = "cs"

	)

# Repeat the same functions for other shit
def printstuff(stuff):


	contacts = []

	stuff.execute("SELECT first_name, last_name, email FROM contacts")

	for (first_name, last_name, email) in stuff:

		contacts.append(f"\n{first_name} {last_name}|{email}\n")

	print("\n".join(contacts))


# For inserting shit 
def insertstuff(stuff):

	first_name = input("Enter first name ")
	last_name = input("Enter last name ")
	email = input("Enter email ")

	stuff.execute(f"INSERT into contacts (first_name, last_name, email) values ('{first_name}', '{last_name}', '{email}')")






# Essential driver code
if __name__ == "__main__":
	cursor = connect.cursor()

	insertstuff(cursor)

	printstuff(cursor)

	connect.close()

	print("Connection established")