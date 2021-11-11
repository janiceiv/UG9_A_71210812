#print
print ("=====MASUKAN JUMLAH MAKANAN YANG DIPESAN=====")

#proses
ikan = int(input("IKAN BAKAR         Rp 25.000,00  : "))
es = int(input("ES DOGER           Rp 6.000,00   : "))
rujak = int(input("RUJAK CINGUR       Rp 8.000,00   : "))

#proses
ikann = ikan * 25000
ess = es * 6000
rujakk = rujak * 8000
total = ikann + ess + rujakk

#print
print ("=====TOTAL=====")
print ("TOTAL IKAN BAKAR     : Rp", ikann)
print ("TOTAL ES DOGER       : Rp", ess)
print ("TOTAL RUJAK CINGUR   : Rp", rujakk)
print ("Jumlah total biaya yang harus dibayar adalah Rp", total)


