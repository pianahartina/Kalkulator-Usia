from datetime import date, date

print("Masukkan Tanggal Lahir")
tahun = int(input("Tahun lahir:"))
bulan = int(input("Bulan lahir:"))
hari = int(input("Tanggal lahir:"))
           
tanggal_lahir = date(tahun, bulan, hari)
hari_ini = date.today()

#Rumus hari semua
usia_hari = (hari_ini - tanggal_lahir).days
print(f"Usia kamu: {usia_hari} hari")


