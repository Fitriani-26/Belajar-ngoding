print('''Nama    : Fitriani
Nim     : D0221370
Kelas   : Informatika H\n''')

print ('======MENGHITUNG LUAS DAN VOLUME BANGUN RUANG======\n')

# Parent class
class BangunRuang :
    def luas (self):
        pass
    
    def volume (self):
        pass
    
# Child class
class Balok (BangunRuang):
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0
                
    def luas (self):
        print ("luas = ", 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi))
                
    def volume (self):
        print ("volume = ", self.panjang * self.lebar * self.tinggi)
        
class Bola(BangunRuang):            
    def __init__(self):
        self.jari = 0
                
    def luas (self):
        print ("luas = ", 4 * 3.14 * self.jari**2)
                
    def volume (self):
        print ("volume = ", 4/3 * 3.14 * self.jari**3)


class Kubus (BangunRuang):
    def __init__(self):
        self.sisi = 0
                
    def luas (self):
        print ("luas = ", 6 * self.sisi**2)
                
    def volume (self):
        print ("volume = ", self.sisi**3)
        
# panggil kelas
balok = Balok ()
bola = Bola ()
kubus = Kubus ()

while True :
    print ('''Pilih Bangun Ruang dibawah ini :
1. Balok
2. Bola
3. Kubus
4. Exit ''')
    pilih = input("\nMasukkan pilihan diatas : ")

    if pilih == '1':
        balok.panjang = float(input("masukkan panjang Balok : "))
        balok.lebar = float(input("masukkan lebar Balok : "))
        balok.tinggi = float(input("masukkan tinggi Balok : "))
        
        print ()
        print ('''====Pilih menu di bawah ini====
1. Menghitung Luas
2. Menghitung Volume''')
        n = input ("\nMasukkan pilihan di atas : ")
        
        if n == '1':
            balok.luas ()
            print ()
        elif n == '2':
            balok.volume ()
            print ()
        else :
            print ('Menu yang Anda pilih tidak tersedia')
            print ()
            
    elif pilih == '2':
        bola.jari = float(input("masukkan jari-jari Bola : "))
        
        print ()
        print ('''====Pilih menu di bawah ini====
1. Menghitung Luas
2. Menghitung Volume''')
        
        n = input ("\nMasukkan pilihan di atas : ")
        
        if n == '1':
            bola.luas ()
            print ()
        elif n == '2':
            bola.volume ()
            print ()
        else :
            print ('Menu yang Anda pilih tidak tersedia')
            print ()
     
    elif pilih == '3':
        kubus.sisi = float(input("masukkan sisi : "))
        
        print ()
        print ('''====Pilih menu di bawah ini====
1. Menghitung Luas
2. Menghitung Volume ''')
        n = input ("\nMasukkan pilihan di atas : ")
        
        if n == '1':
            kubus.luas ()
            print ()
        elif n == '2':
            kubus.volume ()
            print ()
        else :
            print ('Menu yang Anda pilih tidak tersedia')
            print ()
            
    elif pilih == '4':
        print ("Terima kasih")
        break
    
    else :
        print ("Periksa kembali inputan anda!\n")
        
        
               
  
        
