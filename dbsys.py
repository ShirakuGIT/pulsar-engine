import mariadb as mysqlconnector

connect = mysqlconnector.connect(
	user = "root",
	password = "12345678",
	host = "localhost",
	db = "cs"

	)


def printstuff(stuff):


	contacts = []

	stuff.execute("SELECT first_name, last_name, email FROM contacts")

	for (first_name, last_name, email) in stuff:

		contacts.append(f"\n{first_name} {last_name}|{email}\n")

	print("\n".join(contacts))

cursor = connect.cursor()

printstuff(cursor)

connect.close()

print("Connection established")