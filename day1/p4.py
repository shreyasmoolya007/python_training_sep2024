#Math table upto 20

n = int(input("Enter a number"))

for i in range (1,21):
    print('%d * %02d = %03d'%(n, i, i*n))