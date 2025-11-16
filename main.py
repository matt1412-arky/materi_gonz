import sqlite3

# --- Inisialisasi database ---
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()


# --- Create ---
def create_user(name, email):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("✅ User created successfully.")
    except sqlite3.IntegrityError as e:
        print(f"❌ Error: {e}")
    conn.close()


# --- Read ---
def list_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    if users:
        print("\n📄 User List:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    else:
        print("⚠️ No users found.")


# --- Update ---
def update_user(user_id, new_name, new_email):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name, new_email, user_id))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ User updated successfully.")
    else:
        print("❌ User not found.")
    conn.close()


# --- Delete ---
def delete_user(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("✅ User deleted successfully.")
    else:
        print("❌ User not found.")
    conn.close()


# --- Menu ---
def main():
    init_db()
    while True:
        print("\n=== User Management ===")
        print("1. Create User")
        print("2. List Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")

        choice = input("Choose an option [1-5]: ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            create_user(name, email)
        elif choice == "2":
            list_users()
        elif choice == "3":
            try:
                user_id = int(input("Enter user ID to update: "))
                new_name = input("Enter new name: ")
                new_email = input("Enter new email: ")
                update_user(user_id, new_name, new_email)
            except ValueError:
                print("❌ Invalid ID.")
        elif choice == "4":
            try:
                user_id = int(input("Enter user ID to delete: "))
                delete_user(user_id)
            except ValueError:
                print("❌ Invalid ID.")
        elif choice == "5":
            print("👋 Exiting.")
            break
        else:
            print("❌ Invalid option. Please choose between 1-5.")


if __name__ == "__main__":
    main()
