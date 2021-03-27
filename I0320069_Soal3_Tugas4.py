lolos = True
gagal = False
#Satuan lbs
def lbs():
    berat = int(input("Masukan Berat Bagasi Anda = "))
    if berat <= 50:
        print(lolos)
        start()
    elif berat > 50:
        print(gagal)
        start()
    else:
        print("Input tidak valid")
        lbs()
#Satuan kg
def kg():
    berat = float(input("Masukan Berat Bagasi Anda = "))
    if berat <= 22.6:
        print(lolos)
        start()
    elif berat > 22.6:
        print(gagal)
        start()
    else:
        print("Input tidak valid")
        kg()
def start():
    print("===== Pemeriksaan Berat Bagasi =====")
    print("Berat Maksimum = 50 lbs / 22.6 kg")
    print("1. Kilogram (kg)")
    print("2. Pound (lbs)")
    pilihan = input("Masukan Pilihan Satuan Berat (1/2) : ")
    if pilihan == "1":
        kg()
    elif pilihan == "2":
        return lbs()
    else:
        print("Input tidak valid")
        start()
start()

#a. Jika input berat lebih dari 110 kg maka False
#b. Jika input berat 49 kg maka False
