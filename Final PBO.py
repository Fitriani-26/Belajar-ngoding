# Nama : Fitriani
# Kelas : Informatika H
# Nim : D0221370

print('''Nama    : Fitriani
Nim     : D0221370
Kelas   : Informatika H\n''')

print ('======MENGHITUNG LUAS DAN VOLUME BANGUN RUANG======\n')
class Balok ():
    def __init__(self, panjang, lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
                
    def luas (self):
        luas = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi)
        print ("Luas Balok adalah = ",luas)
                
    def volume (self):
        volume = self.panjang * self.lebar * self.tinggi
        print ("Volume Balok adalah = ", volume)
        
class Bola():            
    def __init__(self, jari):
        self.jari = jari
                
    def luas (self):
        luas = 4 * 3.14 * self.jari**2
        print ("Luas Bola adalah = ",luas)
                
    def volume (self):
        volume = 4/3 * 3.14 * self.jari**3
        print ("Volume Bola adalah = ", volume)


class Kubus ():
    def __init__(self, sisi):
        self.sisi = sisi
                
    def luas (self):
        luas = 6 * self.sisi**2
        print ("Luas Kubus adalah = ",luas)
                
    def volume (self):
        volume = self.sisi**3
        print ("Volume Kubus adalah = ", volume)


pilih = 'y'
while pilih == 'y':
    print ('''Pilih menu dibawah ini :
1. Balok
2. Bola
3. Kubus ''')
    pilih = input("\nMasukkan pilihan diatas : ")

    if pilih == '1':
        panjang = float(input("masukkan panjang Balok : "))
        lebar = float(input("masukkan lebar Balok : "))
        tinggi = float(input("masukkan tinggi Balok : "))
        balok = Balok (panjang, lebar, tinggi)
        print ()
        n = input ("Mau hitung apa ? \nketik luas untuk menghitung luas atau ketik volume untuk menghitung volume [luas/volume] = ")
        if n == 'luas':
            balok.luas ()
        elif n == 'volume':
            balok.volume ()
        else :
            print ('Periksa inputan anda')
            
    elif pilih == '2':
        jari = float(input("masukkan jari-jari Bola : "))
        bola = Bola (jari)
        print ()
        n = input ("Mau hitung apa ? \nketik luas untuk menghitung luas atau ketik volume untuk menghitung volume [luas/volume] = ")
        if n == 'luas':
            bola.luas ()
        elif n == 'volume':
            bola.volume ()
        else :
            print ('Periksa inputan anda')
            
        
    elif pilih == '3':
        sisi = float(input("masukkan sisi : "))
        kubus = Kubus (sisi)
        print ()
        n = input ("Mau hitung apa ? \nketik luas untuk menghitung luas atau ketik volume untuk menghitung volume [luas/volume] = ")
        if n == 'luas':
            kubus.luas ()
        elif n == 'volume':
            kubus.volume ()
        else :
            print ('Periksa inputan anda')        
        
    else :
        print ("Periksa kembali inputan anda!!")

    pilih = input('\nMau menghitung lagi ? pilih y jika Ya, dan pilih n jika Tidak [y/n] = ')
    if pilih == 'n':
        print ('Terima Kasih')
        break
               
  
        
