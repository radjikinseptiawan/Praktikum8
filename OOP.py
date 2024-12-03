class Person():
    def __init__(self, nama):
        self.nama = nama
        self.alamat = ""
        self.__umur = 0 # Atribut Private
    
    def __cek_umur(self):
        if self.__umur > 17:
            return 'Sudah dewasa'
    
    @property
    def umur(self):
        return self.__umur
    @umur.setter
    def umur(self,value):
        self.__umur = value


ari = Person("Ari")
ari.nama = 'Ari Santoso'
print(ari.umur)