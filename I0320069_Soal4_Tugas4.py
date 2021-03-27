print("===== PENDAFTARAN KURSUS ONLINE =====")
nama = str(input("Masukan namamu = "))
umur = int(input("Berapa usiamu = "))
if umur < 21:
    print("Anda tidak dapat mendaftar di kursus.")
elif umur >= 21:
    response = input("Apakah Anda sudah lulus ujian kualifikasi (Y / T)? =")
    if response == 'y' :
        print("Anda dapat mendaftar di kursus")
    elif response == 't' :
        print("Anda tidak dapat mendaftar di kursus.")
    else:
        print("Input tidak valid")

