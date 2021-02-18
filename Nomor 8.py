# Alfarrel Daffa M/2
# XI MIA 5
def modus(angka):
    count = 0
    terbanyak = angka[0]

    for i in angka:
        flag = angka.count(i)
        if flag >= count:
            count = flag
            terbanyak = i
    return(terbanyak)
while True:
    a = input( "Masukkan angka:")

    angka = a.split()
    print( "Modusnya adalah: ", modus(angka))
    break
