import psycopg2
import csv

# connect to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="Daniel2008F",
    port="5432"
)

# create cursor to execute SQL queries
cur = conn.cursor()


# 1. create table
def create_table():
    # create phonebook table if it does not exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username TEXT,
            phone TEXT
        )
    """)
    conn.commit()  # save changes
    print("Table created")


# 2. insert data from console
def add_user():
    name = input("Name: ")
    phone = input("Phone: ")

    # insert new record
    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Added")


# 3. insert data from CSV file
def add_from_csv():
    filename = input("CSV file: ")

    # open CSV file
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip header

        for row in reader:
            # insert each row into table
            cur.execute(
                "INSERT INTO phonebook VALUES (DEFAULT, %s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    print("CSV added")


# 4. show all data
def show_all():
    # select all rows
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    # print all rows
    for r in rows:
        print(r)


# 5. update phone by username
def update_phone():
    name = input("Name: ")
    new_phone = input("New phone: ")

    # update phone number
    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE username=%s",
        (new_phone, name)
    )
    conn.commit()
    print("Updated")


# 6. delete user by username
def delete_user():
    name = input("Name to delete: ")

    # delete record
    cur.execute(
        "DELETE FROM phonebook WHERE username=%s",
        (name,)
    )
    conn.commit()
    print("Deleted")


# main menu
while True:
    print("\n1.Create table")
    print("2.Add user")
    print("3.Add from CSV")
    print("4.Show all")
    print("5.Update phone")
    print("6.Delete user")
    print("0.Exit")

    choice = input(">> ")

    if choice == "1":
        create_table()
    elif choice == "2":
        add_user()
    elif choice == "3":
        add_from_csv()
    elif choice == "4":
        show_all()
    elif choice == "5":
        update_phone()
    elif choice == "6":
        delete_user()
    elif choice == "0":
        break


conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT * FROM search_contacts(%s)", ('Dan',))
rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()
conn.close()


