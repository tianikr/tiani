import tabula as tb

bulan = []
tahun = []
inflasi = []

df = tb.read_pdf("Inflasi.pdf", pages='all')

#TIANI KHUSNUL RAHMAWATI
#dapat array daftar tahun
tahune = "tahune"
for x in range(0,len(df['Inflasi'])):
    datene = df['Month'][x]
    nama = datene.split(" ")
    if nama[1] != tahune:
        tahun.append(nama[1])
        tahune = nama[1]

# print(tahun.index('2019'))
for y in range(0,len(tahun)):
    berapa_bulan = 0
    inflasine = 0.0
    for x in range(0,len(df['Inflasi'])):
        datene = df['Month'][x]
        nama = datene.split(" ")
        if tahun[y] == nama[1]:
            berapa_bulan = berapa_bulan + 1
            angkane = df['Inflasi'][x]
            angka = angkane.replace('%','')
            inflasine = inflasine+float(angka)
    bulan.append(berapa_bulan)
    infla_tahun = inflasine / berapa_bulan
    inflasi.append(infla_tahun)

for z in range(0,len(tahun)):
    nomor = z+1
    print("No. %d Tahun %s Selama %d Bulan, Rata-Rata Inflasi %2.2f" % (nomor,tahun[z],bulan[z],inflasi[z]))
    
