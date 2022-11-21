import random
import sys

class ATM():
    def __init__(self, nama, nomor_akun, saldo = 0):
        self.nama = nama
        self.nomor_akun = nomor_akun
        self.saldo = saldo

    def detail_akun (self):
        print("\n----------DETAIL AKUN----------")
        print(f"Pemilik Akun : {self.nama}")
        print(f"Nomor Akun : {self.nomor_akun}")
        print(f"Saldo yang Tersedia : Rp.{self.saldo}\n")

    def setor(self, jumlah):
        self.jumlah = jumlah
        self.saldo = self.saldo + self.jumlah
        print("Saldo rekening saat ini: Rp.", self.saldo)
        print()
        
    def menarik(self, jumlah):
        self.jumlah = jumlah
        if self.jumlah > self.saldo:
            print("Saldo Anda tidak Cukup!")
            print(f"Saldo Anda hanya Rp.{self.saldo}")
            print("Coba dengan jumlah yang lebih rendah dari saldo.")
            print()
        else :
            self.saldo = self.saldo - self.jumlah
            print(f"Rp.{jumlah} Penarikan Berhasil!")
            print("Saldo rekening saat ini: Rp.", self.saldo)
            print()
            
    def check_saldo(self):
        print("Saldo yang Tersedia : Rp.", self.saldo)
        print()

    def transaksi(self):
        print("""
            TRANSAKSI
        *********************
            Menu:
            1. Detail Akun 
            2. Check Saldo
            3. Setor
            4. Menarik
            5. Exit
        *********************
        """)

        while True:
            try:
                pilih = int(input("Maukkan angka 1, 2, 3, 4 atau 5: "))
            except:
                print("Error: Masukkan angka 1, 2, 3, 4, atau 5 saja!\n")
                continue
            else:
                if pilih == 1:
                    atm.detail_akun()
                elif pilih == 2:
                    atm.check_saldo()
                elif pilih == 3:
                    jumlah = int(input("Berapa banyak yang ingin Anda Setrorkan(Rp.): "))
                    atm.setor(jumlah)
                elif pilih == 4:
                    jumlah = int(input("Berapa banyak yang ingin Anda tarik (Rp.): "))
                    atm.menarik(jumlah)
                elif pilih == 5:
                    print(f"""
                Tanda Penerima..............
          ****************************************
              Transaksi Selesai.                         
              Nomor Transaksi: {random.randint(10000, 1000000)} 
              Pemilik Akun : {self.nama}                  
              Nomor Akun : {self.nomor_akun}                
              Saldo yang Tersedia: Rp.{self.saldo}                    
 
              Terima kasih telah memilih kami sebagai bank Anda                 
          *********************************************************
          """)
                    sys.exit()
                 
 
print("*******SELAMAT DATANG DI BANK INDONESIA*******")
print("___________________________________________________________\n")
print("----------------PEMBUATAN AKUN---------------")
nama = input("Masukkan nama Anda : ")
nomor_akun = input("Masukkan nomor akun Anda : ")
print("Selamat! Akun Anda berhasil dibuat......\n")
 
atm = ATM(nama, nomor_akun)
 
while True:
    trans = input("Apakah anda ingin melakukan Transaksi?(y/n): ")
    if trans == "y":
        atm.transaksi()
    elif trans == "n":
        print("""
    ----------------------------------------------------
   | Terima kasih telah memilih kami sebagai bank Anda  |
   | Kunjungi kami lagi!                                |
    ----------------------------------------------------
        """)
        break
    else:
        print("Perintah yang Anda masukkan salah!  Masukkan 'y' untuk Ya dan 'n' untuk Tidak.\n")
