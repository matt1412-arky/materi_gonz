class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(f"Nama: {self.name}, Email: {self.email}")


class UserManager:
    def __init__(self):
        self.users = []  # Menyimpan daftar objek User

    def add_user(self):
        name = input("Masukkan nama: ")
        email = input("Masukkan email: ")
        user = User(name, email)
        self.users.append(user)
        print("✅ Data berhasil ditambahkan.")

    def show_users(self):
        if not self.users:
            print("⚠️ Belum ada data.")
        else:
            print("\n📄 Daftar Pengguna:")
            for i, user in enumerate(self.users, start=1):
                print(f"{i}. ", end="")
                user.display()


def main():
    manager = UserManager()

    while True:
        print("\n=== Menu ===")
        print("1. Tambah User")
        print("2. Tampilkan Semua User")
        print("3. Keluar")

        pilihan = input("Pilih menu [1-3]: ")

        if pilihan == "1":
            manager.add_user()
        elif pilihan == "2":
            manager.show_users()
        elif pilihan == "3":
            print("👋 Program selesai.")
            break
        else:
            print("❌ Pilihan tidak valid.")

if __name__ == "__main__":
    main()
