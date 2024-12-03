class nilaiMahasisa:
    def __init__(self):
        self.mhs = []

    def tambahData(self,nama,nilai):
        newObject = {
            "nama":nama,
            "nilai":nilai
        }
        self.mhs.append(newObject)

    def tampilkanData(self):
        for index,data in enumerate(self.mhs,1):
            print(f''' {index} | {data['nama']}  {data["nilai"]}''')

    def hapusData(self,index):
        if 1 <= index <= len(self.mhs):
            print('Data Di hapus')
            del self.mhs[index - 1]
        else:
            print("Index tidak valid!")
 
    def editData(self, index, nama=None, nilai=None):
        if 1 <= index <= len(self.mhs):
            if nama is not None:
                self.mhs[index - 1]["nama"] = nama
            elif nilai is not None:
                self.mhs[index - 1]["nilai"] = nilai
            print("Data berhasil diedit")
        else:
            print("Index tidak valid!")


# Membuat nilaiMahasiswa
Nilai = nilaiMahasisa()
# Tambah Data
Nilai.tambahData("Budi Arie",50)
Nilai.tambahData("Susantau Del",90)
Nilai.tambahData("Risma Anwar",29)
# Tampilkan Data
Nilai.tampilkanData()
# Hapus nama
Nilai.hapusData(2)
# editData
Nilai.editData(1,"Sinte",70)
Nilai.tampilkanData()
