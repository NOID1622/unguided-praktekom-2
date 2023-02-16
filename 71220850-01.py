# #input 
# object_1 = float(input('objek 1:'))
# object_2 = float(input('objek 2:'))

# import math
# #proses 
# jarak_kedua =  math.sqrt() 
from math import sqrt as pangkat
x1 = int(input('masukkan x1 :')) 
x2 = int(input('masukkan x2 :')) 
y1 = int(input('masukkan y1 :')) 
y2 = int(input('masukkan y2 :')) 

rumus = float(pangkat(((x2-x1)**2)+((y2-y1)**2)))

print('jadi hasilnya adalah: ', rumus)