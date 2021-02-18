# Alfarrel Daffa M/2
# XI MIA 5
def bebek(jumlah_bebek, bagi):
    hasil_bagi = int( jumlah_bebek / bagi )
    sisa = jumlah_bebek % bagi
    return( hasil_bagi, sisa)

while True:
    a = int(input( "Masukkan jumlah bebek: "))
    b = int(input( "Masukkan jumlah teman: "))
    

    x, y = bebek( a, b )
    print( "Masing-masing ", x)
    print( "Sisa: ", y)
    break