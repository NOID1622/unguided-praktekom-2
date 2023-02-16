# input
tinggi_badan  = int(input('tinggi badan :'))
bmi = float(input('bmi:'))

#proses 
tinggi_badancm = tinggi_badan/100
berat = bmi*(tinggi_badan**2)

#output
print('berat badan anda adalah:', berat,'kg')