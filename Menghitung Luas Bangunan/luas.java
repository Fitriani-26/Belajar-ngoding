// Tugas ke 3
// Fitriani_D0221370
// Informatika H

package tugas;
import java.util.Scanner;
public class luas {
    public static void main(String[] args) {
        // Luas persegi
        System.out.println("Luas persegi");
        double sisi, luas ;
        Scanner input = new Scanner (System.in);
        System.out.print("Masukkan panjang sisi persegi : ");
        sisi = input.nextInt();
        luas = sisi * sisi ;
        System.out.println("Luas = " + sisi + " * " + sisi + " = " + luas + " cm ");
        System.out.println("================================");
        
        // Luas Lingkaran
        System.out.println("Luas Lingkaran");
        double phi = 3.14, r, luas2;
        Scanner input2 = new Scanner (System.in);
        System.out.print("Masukkan jari - jari lingkaran : ");
        r = input2.nextInt();
        luas2 = phi * r * r ;
        System.out.println("Luas = " + phi + " * " + r + " * " + r + " = " + luas2 + " cm2 ");
        System.out.println("================================");
        
        // Luas Segitiga
        System.out.println("Luas Segitiga");
        double a, t, luas3;
        Scanner input3 = new Scanner (System.in);
        System.out.print("Masukkan panjang alas segitiga : ");
        a = input3.nextInt();
        System.out.print("Masukkan tinggi segitiga : ");
        t = input3.nextInt();
        luas3 = 0.5 * a * t;
        System.out.println("Luas = " + 0.5 + " * " + a + " * " + t + " = " + luas3 + " cm2 ");
        
        
        
        
    }
   
}
