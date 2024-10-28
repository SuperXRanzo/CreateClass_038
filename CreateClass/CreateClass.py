class PersegiPanjang:
    def _init_(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def _str_(self):
        return f"Persegi Panjang, Panjang {self.panjang} cm, dan Lebar {self.lebar} cm"

    if _name_ == "_main_":
        persegi = PersegiPanjang(3, 2)

    print(persegi)  
    print(f"Keliling: {persegi.hitung_keliling()} cm")  
    print(f"Luas: {persegi.hitung_luas()} cm")  