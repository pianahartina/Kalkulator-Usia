from datetime import date

# Kalkulator Usia
# 1. Minta user input tanggal lahir

print("Kalkulator Usia")
print(" ")
print("masukkan tanggal lahir")
tahun = int(input("Tahun lahir:"))
bulan = int(input("Bulan lahir:"))
hari = int(input("Tanggal lahir:"))
           
# 2. Bikin tanggal lahir + tanggal hari ini
tanggal_lahir = date(tahun, bulan, hari)
hari_ini = date.today()

# 3. Hitung selisihnya
selisih = hari_ini - tanggal_lahir

# 4. Ubah ke tahun, bulan, hari
usia_tahun = selisih.days // 365 # // = bagi bulat
sisa_hari = selisih.days % 365 # % = sisa bagi
usia_bulan = sisa_hari // 30
usia_hari = sisa_hari % 30

print(f"usia kamu: {usia_tahun} tahun, {usia_bulan} bulan, {usia_hari} hari")