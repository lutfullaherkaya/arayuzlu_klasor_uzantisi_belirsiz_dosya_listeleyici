import tkinter as tk
from tkinter import filedialog

from .KesYapistirKopyalaSecMenusu import KesYapistirKopyalaSecMenusu as KopyalaMenusu

class KlasorKonumKutucugu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        

        self.lblKlasorKutucugu = tk.Label(text="Klasor Konumu:", master=self)


        self.entKlasorKutucugu = tk.Entry(master=self, width=20)
        self.entKlasorKutucugu.bind("<Key>", self._konumKutusuGenislikGuncelle)
        self.entKlasorKutucugu.bind("<<Paste>>", self._konumKutusuGenislikGuncelle)

        self.kopyalaMenusu = KopyalaMenusu(self)



        self.btnKlasorKutucugu = tk.Button(master=self, text="Dosya Gezgini...", command=self._klasorKonumuIste)

        self.lblKlasorKutucugu.grid(row=0, column=0, sticky="w")
        self.entKlasorKutucugu.grid(row=1, column=0, sticky="nsew")
        self.btnKlasorKutucugu.grid(row=1, column=1, sticky="wns")


        self.columnconfigure(0, weight=1, minsize=1)
        self.columnconfigure(1, weight=0, minsize=1)
        self.rowconfigure(0, weight=0, minsize=1)
        self.rowconfigure(1, weight=1, minsize=1)



    def _konumKutusuGenislikGuncelle(self, event=None):
        self.parent.after(50, lambda:self.entKlasorKutucugu.config(
                width=min(max(len(self.entKlasorKutucugu.get())+7, 20), 100)))

    def _klasorKonumuIste(self):
        self.entKlasorKutucugu.delete(0, tk.END)
        self.entKlasorKutucugu.insert(0, filedialog.askdirectory())
        
        self._konumKutusuGenislikGuncelle()
        

    def konumAl(self):
        return self.entKlasorKutucugu.get()
            



class Uygulama(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.klasorKonumKutucugu = KlasorKonumKutucugu(self)
        self.alinanKonum = tk.Label(master=self, text="")
        self.btnKonumAl = tk.Button(master=self, command=self._konumYaz, text="konum al")
        
        


        self.klasorKonumKutucugu.grid(row=0, column=0)
        self.btnKonumAl.grid(row=1, column=0)
        self.alinanKonum.grid(row=2, column=0)

        

    def _konumYaz(self):
        self.alinanKonum["text"] = "konumunuz: " + self.klasorKonumKutucugu.konumAl()



        


if __name__ == "__main__":
    root = tk.Tk()
    Uygulama(root).pack(side="top", fill="both", expand=True)
    root.mainloop()