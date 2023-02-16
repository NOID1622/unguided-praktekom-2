#input
x = int(input('masukan detik : '))

#proses
hari = n // (3600*24)
n = x % (3600*24)
jam = n // 3600
sisa = n % 3600
menit = sisa // 60
detik = sisa % 60

#output
print (' hari,', hari,' jam, ', jam,' menit, ', menit,' detik, ', detik)
