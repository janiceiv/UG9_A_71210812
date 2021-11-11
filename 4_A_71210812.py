#print
print ("=====MASUKAN JUMLAH MAKANAN YANG DIPESAN=====")

#proses
ikan = int(input("IKAN BAKAR         Rp 25.000,00  : "))
es = int(input("ES DOGER           Rp 6.000,00   : "))
rujak = int(input("RUJAK CINGUR       Rp 8.000,00   : "))

#proses
ikanb = ikan * 25000
esd = es * 6000
rujakc = rujak * 8000
total = ikanb + esd + rujakc

#print
print ("=====TOTAL=====")
print ("TOTAL IKAN BAKAR     : Rp", ikanb)
print ("TOTAL ES DOGER       : Rp", esd)
print ("TOTAL RUJAK CINGUR   : Rp", rujakc)
print ("Jumlah total biaya yang harus dibayar adalah Rp", total)


