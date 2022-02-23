import mariadb as mysqlconnector

try:
	connect = mysqlconnector.connect(
		user = "root",
		password = "12345678",
		host = "localhost",
		db = "cs"
		)
	print("Connection has been established")
except:
	print("Error, please try again")


# Repeat the same functions for other shit
def printstuff(stuff):


	contacts = []

	stuff.execute("SELECT * FROM contacts")

	for (first_name, last_name, email) in stuff:

		contacts.append(f"\n{first_name} {last_name}|{email}\n")

	print("\n".join(contacts))


# For inserting shit 
def insertstuff(stuff):

	first_name = input("Enter first name\t")
	last_name = input("Enter last name\t")
	email = input("Enter email\t")

	stuff.execute(f"INSERT into contacts (first_name, last_name, email) values ('{first_name}', '{last_name}', '{email}')")



# Essential driver code
if __name__ == "__main__":
	cursor = connect.cursor()

	insertstuff(cursor)

	printstuff(cursor)

	connect.commit()

	connect.close()

