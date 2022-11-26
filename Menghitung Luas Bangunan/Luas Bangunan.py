# Program Menghitung Luas
# Nama  : Fitriani
# Nim   : D0221370
# Kelas : Informatika H

print ("=====Selamat datang di Program Untuk mengitung Luas===== \n")

while True :
    print (""" Silahkan pilih menu dibawah ini :
1. Luas Persegi
2. Luas Lingkaran
3. Luas segitiga
4. Berhenti """)
    pilih = input("Masukkan menu di atas : ")

    if pilih == "1" :
        print ("Menghitung Luas Persegi Panjang")
        s = float(input("Masukkan sisi Persegi : "))
        luas = s * s
        print ("Luas = ", s , "*", s, "=", luas, "cm")
        print ("\n")
        
    elif pilih == "2":
        print ("Menghitung Luas Lingkaran")
        r = float(input("Masukkan jari - jari Lingkaran : "))
        luas = 3.14 * r * r
        print ("Luas = ", 3.14, "*", r, "*", r , "=", luas, "cm2")
        print ("\n")
            
    elif  pilih == "3":
        print ("Menghitung Luas Segitiga")
        a = float(input("Masukkan Alas Segitiga : "))
        t = float(input("Masukkan Tinggi Segitiga : "))
        luas = 0.5 * a * t
        print ("Luas = ", 0.5, "*", a, "*", t, "=", luas, "cm2")
        print ("\n")
        
    elif pilih == "4":
        break
    
    else :
        print ("Periksa kembali Inputan Anda!")
        print ("\n")
    
    
        
