print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print                                    ("Data Mahasiswa")
print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

nama = str(input("masukkan nama :"))
nim = int(input("masukkan nim :"))
prodi = str(input("masukkan prodi :"))
ip = float(input("masukkan ip anda :"))
Jenis_kelamin = str(input("masukkan jenis kelamin :"))

pilihan = "Y"
while pilihan == "Y":
        List = [nama, nim, prodi, ip, Jenis_kelamin]
        pilih = str(input( "pilih data yan ingin ditampilkan? (misal : nama, nim, prodi, ip, jenis kelamin):" ))
        
        if pilih == "nama" :
             print  ("hasil input data:", nama)
        elif pilih == "nim" :
             print  ("hasil input data:", nim)
        elif pilih == "prodi" :
            print  ("hasil input data:", prodi)
        elif pilih == "ip" :
             print  ("hasil input data:", ip)
        elif pilih == "jenis kelamin" :
             print  ("hasil input data:", Jenis_kelamin)
        pilihan = input("apakah masih ingin melihat data? Y jika yes dan N jika no :")
print ("terima kasih")
    