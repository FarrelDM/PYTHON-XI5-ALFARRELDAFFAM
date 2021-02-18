# Alfarrel Daffa M/2
# XI MIA 5
num1 = int(input( "Masukkan panjang alas: "))
num2 = int(input( "Masukkan  tinggi: "))

def luas_segitiga(x, y):
    luas = float(x * y / 2)
    print(format(luas, '.2f'))

luas_segitiga(num1, num2)