from filetype import guess
from sys import argv
from sys import stdout
import os
from ntpath import basename




class DosyaBoyutu:
    def __init__(self, boyut, dosyaTipi, herZamanSade = True):
        self.dosyaTipi = dosyaTipi

        self.boyut = boyut # boyut burada bayttir
        self.birim = "B"
        self.__herZamanSade = herZamanSade
        if self.__herZamanSade:
            self.sadeBoyutHesapla()
        
    birimler = ["B", "KB", "MB", "GB", "TB", "PB"]
    birimSwitch = {"B":0, "KB":1, "MB":2, "GB":3, "TB":4, "PB":5}

    def sadeBoyutHesapla(self):
        self.sadeBoyut = self.boyut
        self.sadeBirim = self.birim
        while self.sadeBoyut >= 1024.0 and self.birimSwitch[self.sadeBirim] < 5:
            self.sadeBoyut /= 1024.0
            self.sadeBirim = self.birimler[self.birimSwitch[self.sadeBirim]+1]
        self.sadeBoyut = round(self.sadeBoyut, 3)

    def boyutEkle(self, boyut):
        self.boyut += boyut
        if self.__herZamanSade:
            self.sadeBoyutHesapla()

    @staticmethod
    def sadeBoyutStringDon(boyut):
        boyut = DosyaBoyutu(int(boyut), None)
        return str(boyut.sadeBoyut) + boyut.birim

class DosyaTipleriListesi:
    def __init__(self, konum):
        self.konum = konum
        self.mechuller = []
        self.dosyaTipleri = []

        self._listele()


    def _listele(self):
        if os.path.isdir(self.konum):
            dosya_tipleri = {"meçhul": DosyaBoyutu(0, "meçhul", False)}
            tipi_mechul_dosyalar = []
            for dosya_veya_klasor in os.listdir(self.konum):
                dosya_veya_klasor = os.path.join(self.konum, dosya_veya_klasor)
                if os.path.isfile(dosya_veya_klasor):
                    dosya_tipi = guess(dosya_veya_klasor)
                    if dosya_tipi is None:
                        dosya_tipleri["meçhul"].boyutEkle(os.path.getsize(dosya_veya_klasor))
                        tipi_mechul_dosyalar.append(dosya_veya_klasor)
                    else:
                        dosya_tipi = dosya_tipi.mime # mime yerine extension yazarsan image/png degil de direk png der.
                        if dosya_tipi in dosya_tipleri:
                            dosya_tipleri[dosya_tipi].boyutEkle(os.path.getsize(dosya_veya_klasor))
                        else:
                            dosya_tipleri[dosya_tipi] = DosyaBoyutu(
                                os.path.getsize(dosya_veya_klasor), dosya_tipi, False)


            for dosya_tipi in dosya_tipleri:
                dosya_tipleri[dosya_tipi].sadeBoyutHesapla()

            # dosya tiplerini jigabaytina gore siralama
            dosya_tipleri = [v for k, v in sorted(dosya_tipleri.items(), key=lambda item: item[1].boyut, reverse=True)]
            
            self.dosyaTipleri = dosya_tipleri
            self.mechuller = tipi_mechul_dosyalar
        else:
            raise Exception("HATA: Lutfen klasor adresi giriniz veya pathiniz boslukluysa kenarlara \" koyunuz.")


    def streameYazdir(self, stream):
        stream.write("Dizininizde Bulunan Her Bir Dosya Tipinin Kapladığı Boyut\n")
        for dosya_tipi in self.dosyaTipleri:
            stream.write(dosya_tipi.dosyaTipi + "\t" + str(dosya_tipi.sadeBoyut) + dosya_tipi.sadeBirim + "\n")
        
        stream.write("\nTipi Meçhul Olan Dosyalar\n")
        for mechul in self.mechuller:
            stream.write("Dosya Adı: \"" + basename(mechul) + "\"\n")

    def txtYazdir(self, dosyaAdi="DosyaTipleriListesi.txt"):
        with open(dosyaAdi, "w", encoding="utf-8") as dosya:
            self.streameYazdir(dosya)

    def komutSatirinaYazdir(self):
        print("-----------------------------------------------------------------")
        print("\nAlttaki bilgiler ayni zamanda DosyaTipleriListesi.txt dosyasina kaydedilmistir.\n")
        print("-----------------------------------------------------------------")
        self.streameYazdir(stdout)
        print("-----------------------------------------------------------------")







if __name__ == '__main__':
    liste = DosyaTipleriListesi(konum=argv[1])
    liste.txtYazdir()
    liste.komutSatirinaYazdir()

