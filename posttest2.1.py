print ("menu")
print ("konversi suhu")
print ("a. fahrenheit ke celcius")
print ("b. kelvin ke celcius")
print ("c. reamur ke celcius")
pilihan = "Y"
while pilihan == "Y":
    pilih = str(input( "pilih konversi suhu? (misal : a, b,dan c):" ))

    if pilih == "a" :
        fahrenheit = int(input("masukkan nilai fahrenheit :"))
        a = (fahrenheit - 32) * 5/9
        print  ("hasil konversi dari fahrenheit ke celcius :", a)
     
    elif pilih == "b" :
        kelvin = int(input("masukkan nilai kelvin :"))
        b = kelvin - 273.15
        print ("hasil konversi dari kelvin ke celcius :", b )
    
    elif pilih == "c" :
        reamur = int(input("masukkan nilai reamur :"))
        c = 5/4 * reamur
        print ("hasil konversi dari reamur ke celcius :", c)
    
    else :
        print("hasil konversi salah")
    pilihan = input("apakah ingin menhitung ulang? Y jika yes dan N jika no :")
print ("terima kasih")