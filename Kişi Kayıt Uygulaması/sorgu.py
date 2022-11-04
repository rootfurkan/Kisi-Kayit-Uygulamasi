# Import module
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import sqlite3

# Veritabanı İşleri

baglan = sqlite3.connect("veri.db")
veri = baglan.cursor()


def bul():
    sayi = 0
    for degisken in veri.execute("SELECT  adivesoyadi, tckimlik,cinsiyet, memleket, adresil, adresilce, acikadres, telno, ekbilgiler FROM arkadaslar"):
        if degisken[0] == giris.get():

            tree.insert("", tkinter.END, values=degisken)
            tree2.insert("", tkinter.END, values=degisken)
            textbox.insert('end',  degisken)
            giris.delete(0,'end')

    sayi+1

baglan.commit()

def silme():

    textbox.delete("0.0", END)
    for item in tree.get_children():
        tree.delete(item)
    for item in tree2.get_children():
        tree2.delete(item)

# Obje Yaratma
pencere = Tk()

# Ana Özellikler
pencere.geometry("1400x600")
pencere.maxsize(1400, 600)
pencere.title("Furkan Private SM Database Systems")

# Resim ekleme Kısmı
arkaplan = PhotoImage(file = "2.png")
ikon = PhotoImage(file="isimsizlogo.png")
sorbuton = PhotoImage(file="button.png")
veriolustur = PhotoImage(file="dataolustur.png")
cikisdugmesi = PhotoImage(file="cikis.png")
sifirla = PhotoImage(file="sifirla.png")

# Arkaplan Resmi
anakatman = Label(pencere, image = arkaplan)
anakatman.place(x = -2, y = 0)
# Yazı Kısmı
etiket1= tkinter.Label(anakatman, text="Hoşgeldin Sahip..!", font="Xirod-Regular", fg="white", bg="#363636")
etiket1.place(y=240, x=105)
etiket2= tkinter.Label(anakatman, text="Sorgulanacak Kişi:", font="Xirod-Regular 10", fg="white", bg="#363636")
etiket2.place(y=300, x=140)

# Arama Çubuğu
giris = tkinter.Entry(pencere, bg="#e6c619",font="Arial 13" ,fg="black" ,bd=8,width=27)
giris.place(x=110, y=322)

# Butonlar
btn = tkinter.Button(pencere, height=30, width=30, bd=3 ,bg="#363636",image= sorbuton, activebackground="#e6c619", command=bul)
btn.place(x=380 ,y=322)

cikis = tkinter.Button(pencere, height=30, width=60, image=cikisdugmesi, bg="#363636", activebackground="#e6c619", command=pencere.quit)
cikis.place(x=220, y=480)

veributon = tkinter.Button(pencere,height=30, width=200, image=veriolustur,bg="#363636", activebackground="#e6c619")
veributon.place(x=150, y=380)

sfr = tkinter.Button(pencere, height=30, width=60, image=sifirla, bg="#363636", activebackground="#e6c619", command=silme)
sfr.place(x=220, y=430)

style = ttk.Style(pencere)
style.theme_use("alt")
style.configure("Treeview", background="#e6c619",fieldbackground="#363636", foreground="black", font=("Ubuntu", 15), rowheight=25)
style.map("Treeview", background=[("selected", "green")])



tree= ttk.Treeview(pencere, columns=("A", "B", "C","D"), show='headings', height=1)

tree.heading("A", text="AD SOYAD")
tree.heading("B", text="TC KİMLİK")
tree.heading("C", text="CİNSİYET")
tree.heading("D", text="MEMLEKET")


tree.column("A", width=200, anchor=CENTER)
tree.column("B", width=200, anchor=CENTER)
tree.column("C", width=200, anchor=CENTER)
tree.column("D", width=200, anchor=CENTER)
tree.place(x=542, y=10)




tree2= ttk.Treeview(pencere, columns=("A", "B", "C","D","E","F","G","H"), show='headings', height=1, displaycolumns=("E","F","G","H"))
tree2.heading("E", text="ADRES İL ")
tree2.heading("F", text="ADRES İLÇE")
tree2.heading("G", text="AÇIK ADRES")
tree2.heading("H", text="TELEFON")



tree2.column("E", width=200, anchor=CENTER)
tree2.column("F", width=200, anchor=CENTER)
tree2.column("G", width=200, anchor=CENTER)
tree2.column("H", width=200, anchor=CENTER)
tree2.place(x=542, y=60)




textbox = tkinter.Text(pencere, height=8, width=73, bg="#e6c619", font="Ubuntu 14")
textbox.place(x=540, y=120)





# Pencere Üst İkonu
pencere.iconphoto(False, ikon)



# Döngü
pencere.mainloop()