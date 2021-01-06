from arayuz_yardimci_moduller.DosyaKonumuAlma import KlasorKonumKutucugu
from dosya_tiplerini_listele import DosyaTipleriListesi
from dosya_tiplerini_listele import DosyaBoyutu
from arayuz_yardimci_moduller.KesYapistirKopyalaSecMenusu import KesYapistirKopyalaSecMenusu as KopyalaMenusu
import tkinter as tk
import webbrowser
from io import StringIO   

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# kaynak: https://stackoverflow.com/questions/61494832/embedding-mapplotlib-pie-chart-into-tkinter-gui-issue
class Pasta(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pastaGrafigi = None

    def pastayiOlustur(self, adlar, degerler):
        self.adlar = adlar
        self.degerler = degerler

        fig = Figure(tight_layout=True)
        ax = fig.add_subplot(111)

        toplamDeger = sum(degerler)
        ax.pie(self.degerler, radius=1, labels=self.adlar, 
               autopct=lambda p: '%{:.2f} ({})'.format(p, DosyaBoyutu.sadeBoyutStringDon(p*toplamDeger/100.0)), shadow=True)

        chart1 = FigureCanvasTkAgg(fig, self)

        self.pastaGrafigi = chart1.get_tk_widget()
        self.pastaGrafigi.pack()

    def pastayiYe(self):
        if self.pastaGrafigi:
            self.pastaGrafigi.pack_forget()


class YazarIsmi(tk.Frame):
    def __init__(self, parent, 
                 yazarIsmi="Lutfullah Erkaya", 
                 github=r"https://github.com/lutfullaherkaya", 
                 *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.yazarIsmi = yazarIsmi
        self.github = github

        self.lblYazar = tk.Label(master=self, text="Yazar: " + self.yazarIsmi)

        self.frmGithubVeLink = tk.Frame(master=self)

        self.lblGithub = tk.Label(master=self.frmGithubVeLink, text="Github:")
        self.lblGithubLink = tk.Label(master=self.frmGithubVeLink, text=self.github, 
                                  fg="blue", cursor="hand2")
        self.lblGithubLink.bind("<Button-1>", lambda e: self.linkAc(self.github))
        self.lblGithub.grid(row=0, column=0, sticky="w")
        self.lblGithubLink.grid(row=0, column=1, sticky="w")

        self.lblYazar.grid(row=0, column=0, sticky="w")
        self.frmGithubVeLink.grid(row=1, column=0, sticky="w")

    def linkAc(self, url):
        webbrowser.open_new(url)

        
class Uygulama(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        PAD1 = 20
        PAD2 = 7

        self.baslik = tk.Label(master=self, text="Dosya Tipleri Listeleyici", fg="maroon4")
        self.baslik.config(font=("Segoe", 26))
        self.baslik.grid(row=0, column=0, pady=(0, PAD2))

        self.konumKutucugu = KlasorKonumKutucugu(self)
        self.konumKutucugu.grid(row=1, column=0, sticky="w", pady=(0, PAD2))

        self.btnListele = tk.Button(master=self, text="Listele", command=self._listele)
        self.btnListele.config(font=("Segoe", 16))
        self.btnListele.grid(row=2, column=0, sticky="w", pady=(0, PAD2))

        self.ciktiVePasta = tk.Frame(master=self)

        self.pasta = Pasta(self.ciktiVePasta, relief=tk.SUNKEN, borderwidth=5)
        self.pasta.grid(row=0, column=1, sticky="nswe")

        self.cikti = tk.Text(master=self.ciktiVePasta, state=tk.DISABLED, relief=tk.SUNKEN, borderwidth=5)
        self.cikti.grid(row=0, column=0, sticky="nswe", padx=(0, PAD1))

        self.ciktiVePasta.columnconfigure(0, weight=1, minsize=75)
        self.ciktiVePasta.columnconfigure(1, weight=1, minsize=75)
        self.ciktiVePasta.rowconfigure(0, weight=1, minsize=75)
        self.ciktiVePasta.grid(row=3, column=0, sticky="nswe")

        self.kopyalaMenusu = KopyalaMenusu(self)

        self.yazarIsmi = YazarIsmi(self, relief=tk.RIDGE, borderwidth=2)
        self.yazarIsmi.grid(row=4, column=0, sticky="nswe", pady=(PAD2, 0))


        self.columnconfigure(0, weight=1, minsize=75)
        for i in range(5):
            if (i == 3):
                self.rowconfigure(i, weight=1, minsize=50)
            else:
                self.rowconfigure(i, weight=0, minsize=5)
    
    @staticmethod
    def _textGuncelle(textWidget, yazi):
        textWidget.configure(state=tk.NORMAL)
        textWidget.delete("1.0", tk.END)
        textWidget.insert("1.0", yazi)
        textWidget.configure(state=tk.DISABLED)

    def _listele(self):
        Uygulama._textGuncelle(self.cikti, "Dosya Tipleri listeleniyor. Lutfen bekleyiniz.")
        self.parent.update()
        self.pasta.pastayiYe()
        self.pasta.grid(row=0, column=1, sticky="nswe")

        try:          
            liste = DosyaTipleriListesi(konum=self.konumKutucugu.konumAl())

            dosyaTipleri = [item.dosyaTipi for item in liste.dosyaTipleri]
            boyutlar = [item.boyut for item in liste.dosyaTipleri]
            self.pasta.pastayiOlustur(dosyaTipleri, boyutlar)

            strStream = StringIO("")
            liste.streameYazdir(strStream)
            strStream.seek(0)
            Uygulama._textGuncelle(self.cikti, strStream.read())
            strStream.close()

        except Exception as ex:
            if str(ex)[:5] == "HATA:":
                # bizim raise ettigimiz exceptiondur bu
                Uygulama._textGuncelle(self.cikti, "HATA: Konumu dogru girmenizi rica etmekteyiz.")
            else:
                Uygulama._textGuncelle(self.cikti, str(ex))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Dosya Tipleri Listeleyici")
    Uygulama(root).pack(side="top", fill="both", expand=True, padx=20, pady=20)
    root.mainloop()
    
    
    

    

    

    
