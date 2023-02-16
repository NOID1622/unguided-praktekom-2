#input
inch = int(input('jarak:'))

#proses

mile = int(inch/63360)
inch1 = inch%(1760*3*12)
yard = int(inch1//(3*12))
inch2 = inch%(3*12)
feet = int(inch2//12)
inch3 = int(inch2%12)

#output
print(inch , '=', mile, 'mile', yard, 'yard', feet, 'feet', inch3,'inch')