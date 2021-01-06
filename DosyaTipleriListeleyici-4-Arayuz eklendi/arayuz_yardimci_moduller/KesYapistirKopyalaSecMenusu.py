import tkinter as tk

# entry icin kaynak: https://gist.github.com/angeloped/91fb1bb00f1d9e0cd7a55307a801995f
class KesYapistirKopyalaSecMenusu(tk.Menu):
    def __init__(self, parent, *args, **kwargs):
        tk.Menu.__init__(self, parent, tearoff=0, *args, **kwargs)
        self.parent = parent

        self.add_command(label="Kes")
        self.add_command(label="Kopyala")
        self.add_command(label="Yapistir")
        self.add_separator()
        self.add_command(label="Hepsini Sec")

        # ctrl a varmis zaten, onun icin fonksiyon yazmaya gerek yok.

        self.parent.bind_class("Entry", "<Button-3><ButtonRelease-3>", self._entry_show_textmenu)
        #self.parent.bind_class("Entry", "<Control-a>", self._entry_callback_select_all)
        self.parent.bind_class("Text", "<Button-3><ButtonRelease-3>", self._entry_show_textmenu)

    #def _entry_callback_select_all(self, event):
        # select text after 50ms
        #self.parent.after(50, lambda:event.widget.select_range(0, 'end'))

    def _entry_show_textmenu(self, event):
        e_widget = event.widget
        self.entryconfigure("Kes",command=lambda: e_widget.event_generate("<<Cut>>"))
        self.entryconfigure("Kopyala",command=lambda: e_widget.event_generate("<<Copy>>"))
        self.entryconfigure("Yapistir",command=lambda: e_widget.event_generate("<<Paste>>"))
        self.entryconfigure("Hepsini Sec",command=lambda: e_widget.event_generate("<Control-a>"))
        self.tk.call("tk_popup", self, event.x_root, event.y_root)


if __name__ == "__main__":
    root = tk.Tk()

    menu = KesYapistirKopyalaSecMenusu(root)
    e1 = tk.Entry(); e1.pack()
    e2 = tk.Entry(); e2.pack()

    root.mainloop()