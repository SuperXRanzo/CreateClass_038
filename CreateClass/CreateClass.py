class PersegiPanjang:
    def _init_(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
        
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)
