#list
nama1="lily"
nama2="jeremy"
nama3="rachell"

#index
nama = ["lily","jeremy","rachell"]
nim = ["251712023","251712021","25192019"]
prodi = ["informatika","kesehatan","industri"]
print(nama[1])

print(nama)
print(nim)
print(prodi)

data = ["lily", 20, 3.75 , True]
print(data)

mahasiswa =[
        ["lily", 251712023, "informatika"],
        ["jeremy", 251712021,"kesehatan"],
        ["rachell",25192019,"indusri"],
        ]
#insert
mahasiswa.insert(1,"tia")
print(mahasiswa)

#access
mahasiswa = ["lily","jeremy","rachell"]
print(mahasiswa[0])
print(mahasiswa[-1])

#transversal
nama = []
mahasiswa = ["jeremy","rachell","pieter"]
for nama in mahasiswa:
        print(nama)

#menggunakan range dan len
#len menghitung jumlah data di dalam 
#range

mahasiswa = ["jeremy","rachell","pieter"]
print(len(mahasiswa))

range(len(mahasiswa))
print(list(range(len(mahasiswa))))

#menambah data
mahasiswa = ["jeremy","rachell","pieter"]
mahasiswa.append("tia")
print(mahasiswa)
mahasiswa.insert(2,"fansen")
print(mahasiswa)
mahasiswa1=["sofia"]
mahasiswa.extend(mahasiswa1)
print(mahasiswa)

#menghapus data
mahasiswa.remove("fansen")
print(mahasiswa)

#pop() dan del
mahasiswa.pop(1)
del mahasiswa[0]
  
#menambah update (mengganti nama gitu)menghapus dan menambah
mahasiswa[1]="evan"