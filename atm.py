def atm_sederhana():
    saldo = 100000
    
    while True:
        try:
            print(f"\n💳 Saldo: Rp {saldo:,}")
            print("1. Tarik Tunai")
            print("2. Cek Saldo") 
            print("3. Keluar")
            
            pilihan = int(input("Pilihan: "))
            
            if pilihan == 1:
                jumlah = int(input("Jumlah penarikan: Rp "))
                if jumlah > saldo:
                    raise ValueError("Saldo tidak cukup!")
                saldo -= jumlah
                print(f"✅ Penarikan berhasil! Sisa saldo: Rp {saldo:,}")
                
            elif pilihan == 2:
                print(f"💰 Saldo Anda: Rp {saldo:,}")
                
            elif pilihan == 3:
                print("🙏 Terima kasih!")
                break
                
            else:
                raise ValueError("Pilihan tidak valid!")
                
        except ValueError as e:
            print(f"❌ Error: {e}")
        except KeyboardInterrupt:
            print("\n🚫 Program dibatalkan")
            break

# Jalankan program
atm_sederhana()

