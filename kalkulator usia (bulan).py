from datetime import date

print("Masukkan Tanggal Lahir")
tahun = int(input("Tahun lahir:"))
bulan = int(input("Bulan lahir:"))
hari = int(input("Tanggal lahir:"))
           
tanggal_lahir = date(tahun, bulan, hari)
hari_ini = date.today()

#Rumus bulan semua
usia_bulan = (((hari_ini.year - tanggal_lahir.year) * 12) + (hari_ini.month - tanggal_lahir.month))

if hari_ini.day < tanggal_lahir.day:
    usia_bulan = usia_bulan - 1

print(f"Usia kamu: {usia_bulan} bulan")