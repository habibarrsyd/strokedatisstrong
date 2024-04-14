import statistics
print("===========================================================")
print("SELAMAT DATANG DI SISTEM AKADEMIK MATA KULIAH STRUKTUR DATA")
print("============================================================")

data_mahasiswa = []

def menu():
    print("Daftar Menu Sistem Akademik")
    print("[1] Input Data dan Nilai Akhir Mahasiswa")
    print("[2] Menampilkan peringkat Mata Kuliah")
    print("[3] Melihat Sejarah Perubahan Nilai dan Peringkat")
    print("[4] Melihat Analisis Statistik nilai")
    print("[5] Mencari dan Menghapus Data")
    print("[6] Keluar Sistem")
    pilih=input("Pilih Menu ->> ")
    pilihmenu(pilih)

def pilihmenu(pilih):
    if pilih=="1":
        data()
    elif pilih=="2":
        rank()
    elif pilih=="3":
        history()
    elif pilih=="4":
        static()
    elif pilih=="5":
        find()
    elif pilih=="6":
        print("Keluar")
        exit()

def data():
    print("Masukkan Data dan Nilai Mahasiswa")
    inputnama = input("Nama : ")
    inputnim = input("NIM : ")
    inputnilaiuts = int(input("\nNilai UTS\t\t\t: "))
    inputnilaiuas = int(input("\nNilai UAS\t\t\t: "))
    inputnilaikuis = int(input("\nNilai KUIS\t\t\t: "))
    inputnilaiprakt = float(input("\nNilai Praktikum\t\t: "))
    inputnilaitugas = int(input("\nNilai Tugas\t\t\t: "))
    nilaiakhir = ((inputnilaiuts * 0.3) + (inputnilaiuas * 0.3) + (inputnilaikuis * 0.05) + (inputnilaiprakt * 0.3) + (inputnilaitugas * 0.05))
    simpandata = index(nilaiakhir)
    print("Nilai Akhir: ", nilaiakhir)
    print("Index Akhir: ", simpandata)

    data_mahasiswa.append({
        "Nama": inputnama,
        "NIM": inputnim,
        "UTS" : inputnilaiuts,
        "UAS" : inputnilaiuas,
        "KUIS" : inputnilaikuis,
        "Praktikum" : inputnilaiprakt,
        "Nilai Akhir": nilaiakhir,
        "Index Akhir": simpandata

    })
    input("ketik 'y' untuk kembali ke menu: ")
    menu()

def index(nilaiakhir):
    if nilaiakhir >= 75:
        return "A"
    elif 75 > nilaiakhir >= 70:
        return "AB"
    elif 70 > nilaiakhir >= 60:
        return "B"
    elif 60 > nilaiakhir >= 50:
        return "BC"
    elif 50 > nilaiakhir >= 40:
        return "C"
    elif 40 > nilaiakhir >= 30:
        return "D"
    else:
        return "E"

def rank():
    n = len(data_mahasiswa)
    for i in range(n):
        for j in range(0, n-i-1):
            if data_mahasiswa[j]["Nilai Akhir"] < data_mahasiswa[j+1]["Nilai Akhir"]:
                data_mahasiswa[j], data_mahasiswa[j+1] = data_mahasiswa[j+1], data_mahasiswa[j]
    
    print("Urutan peringkat:")
    for i, mahasiswa in enumerate(data_mahasiswa, start=1):
        print(f"{i}. Nama: {mahasiswa['Nama']}, Nilai Akhir: {mahasiswa['Nilai Akhir']}, Index Akhir: {mahasiswa['Index Akhir']}")

    menu()

    # sorted_data_mahasiswa = sorted(data_mahasiswa)
    
def history():
    pass
def static():
    x=data_mahasiswa
    max=0
    for i in x:
        if i['Nilai Akhir']>max:
            max=i['Nilai Akhir']
    print("\nData Mahasiswa dengan Nilai Terbesar adalah : ")
    print(max)
        
    for i in x:
        min=max
        if i['Nilai Akhir']<min:
            min=i['Nilai Akhir']
    print("\nData Mahasiswa dengan Nilai Terkecil adalah : ")
    print(min)
       
    #mean
    sum_nilai=sum([i['Nilai Akhir'] for i in x])
    rata2=sum_nilai/len(x)
    print('\nRerata nilai: ')
    print(rata2)

    
    #median
    #MODE NILAI AKHIR
    # input nilai tertinggi
    # input nilai terendah
    # hitung rata rata nilai
    # hitung rata rata indeks dari rata rata nilai
    # hitung nilai akhir terbanyak
    # hitung nilai akhir tersedikit

    pass
def find():
    print("Pilih Fitur: ")
    print("[1] Cari Data")
    print("[2] Hapus Data")
    print("[3] Kembali")
    choice=input("Pilih Menu--> ")
    if (choice=="1"):
        cari()
    elif(choice=="2"):
        delete()
    else :
        menu()

def cari():
    x=data_mahasiswa
    cariin=input("\nMasukkan NIM yang ingin dicari : ")
    data_ditemukan=False
    for i in x:
        if i['NIM']==cariin:
            print("\nData Ditemukan! \n")
            print("NIM\t: ",i['NIM'])
            print("Nama\t: ", i['Nama'])
            print("Nilai Akhir\t:",i['Nilai Akhir'])
            data_ditemukan=True
    if not data_ditemukan:
        print("Data Tidak Tersedia/belum Terdaftar\n")
    menu()

def delete():
    x=data_mahasiswa
    a=input("Input NIM data yang ingin dihapus: ")
    for i in x:
        if i['NIM'] == a :
            print("Data Ditemukan")
            b = input("Yakin ingin menghapus data ini? (y/n)")
            if (b=="y") :
                data_mahasiswa.remove(i)
                print("Berhasil Menghapus Data!")
        elif i['NIM'] != a:
            i['NIM']=i+1
        
    menu()
    

menu()