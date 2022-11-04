# Import module
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import sqlite3

# Veritabanı Oluşturma
veritabani = sqlite3.connect("veri.db")
im = veritabani.cursor()
im.execute("CREATE TABLE IF NOT EXISTS arkadaslar(tckimlik TEXT, adivesoyadi TEXT,  cinsiyet TEXT, memleket TEXT, adresil TEXT, adresilce TEXT, acikadres TEXT, telno TEXT,  ekbilgiler TEXT)")


# Veritabanı Kayıt Fonksiyonu
def submit():
    # db connect
    veritabani = sqlite3.connect("veri.db")
    im = veritabani.cursor()



    #tablo ekleme
    im.execute("INSERT INTO arkadaslar VALUES(:tckimlik,:adivesoyadi, :cinsiyet, :memleket, :adresil, :adresilce ,:acikadres, :telno, :ekbilgiler)",
               {
                   'tckimlik': tckimlik.get(),
                   'adivesoyadi': adivesoyadi.get(),
                   'cinsiyet': cinsiyet.get(),
                   'memleket': memleket.get(),
                   'adresil': adresil.get(),
                   'adresilce' : adresilce.get(),
                   'acikadres': acikadres.get(),
                   'telno': telno.get(),
                   'ekbilgiler': ekbilgiler.get('1.0', END)


               })




    # clear text box

    tckimlik.delete(0, END)
    adivesoyadi.delete(0, END)
    cinsiyet.delete(0, END)
    memleket.delete(0, END)
    adresil.delete(0, END)
    adresilce.delete(0,END)
    acikadres.delete(0, END)
    telno.delete(0, END)
    ekbilgiler.delete('1.0', END)




    veritabani.commit()



# Obje Yaratma
pencere = Tk()
arkaplan = PhotoImage(file="veribg.png")
kaydetbuton = PhotoImage(file="kaydetbuton.png")
ikon = PhotoImage(file="isimsizlogo.png")
yuklebuton = PhotoImage(file="yukle.png")
uploadresim = PhotoImage(file="uploadimage.PNG")
cikisbuton = PhotoImage(file="cikis.png")

# Ana Özellikler
pencere.geometry("800x600")
pencere.maxsize(800, 600)
pencere.title("Furkan Private SM Database Systems")
background = Label(pencere,image= arkaplan)
background.place(x = -2, y = 0)
pencere.iconphoto(False, ikon)


# Veri Giriş Pencere Ayarları
etiket3 = tkinter.Label(pencere, text="Yeni Kayıt Ekleme Ekranı", font="Xirod-regular", fg="white", bg="#363636")
etiket3.place(x=200, y=4)
# Veri Giriş 1
etiket4 = tkinter.Label(pencere, text="tc no", font="Xirod-regular 10", fg="white", bg="#363636")
etiket4.place(x=10, y=65)
tckimlik = tkinter.Entry(pencere, font="Arial 13" , bd=5, bg="#e6c619", width=18)
tckimlik.place(x=10, y=85)
# Veri Giriş 2
etiket5 = tkinter.Label(pencere, text="ad soyad", font="Xirod-regular 10", fg="white", bg="#363636")
etiket5.place(x=200, y=65)
adivesoyadi = tkinter.Entry(pencere, font="Arial 13" , bd=5 ,bg="#e6c619", width=18)
adivesoyadi.place(x=200, y=85)
# Veri Giriş 3
etiket6 = tkinter.Label(pencere, text="cinsiyet", font="Xirod-regular 10", fg="white", bg="#363636")
etiket6.place(x=390, y=65)
cinsiyet = tkinter.Entry(pencere,font="Arial 13", bd=5 ,bg="#e6c619", width=18)
cinsiyet.place(x=390, y=85)
# Veri Giriş 4
etiket7 = tkinter.Label(pencere, text="memleket", font="Xirod-regular 10", fg="white", bg="#363636")
etiket7.place(x=580, y=65)
memleket = tkinter.Entry(pencere,font="Arial 13", bd=5 ,bg="#e6c619", width=18)
memleket.place(x=580, y=85)
# Veri Giriş 5
etiket8 = tkinter.Label(pencere, text="adres il", font="Xirod-regular 10", fg="white", bg="#363636")
etiket8.place(x=10, y=150)
adresil = tkinter.Entry(pencere, font="Arial 13",bd=5 ,bg="#e6c619", width=18)
adresil.place(x=10, y=170)
# Veri Giriş 6
etiket9 = tkinter.Label(pencere, text="adres ilçe", font="Xirod-regular 10", fg="white", bg="#363636")
etiket9.place(x=200, y=150)
adresilce = tkinter.Entry(pencere, font="Arial 13",bd=5 ,bg="#e6c619", width=18)
adresilce.place(x=200, y=170)
# Veri Giriş 7
etiket10 = tkinter.Label(pencere, text="açık adres", font="Xirod-regular 10", fg="white", bg="#363636")
etiket10.place(x=390, y=150)
acikadres = tkinter.Entry(pencere, font="Arial 13",bd=5 ,bg="#e6c619", width=18)
acikadres.place(x=390, y=170)
# Veri Giriş 8
etiket11 = tkinter.Label(pencere, text="tel no", font="Xirod-regular 10", fg="white", bg="#363636")
etiket11.place(x=580, y=150)
telno = tkinter.Entry(pencere, font="Arial 13", bd=5  ,bg="#e6c619", width=18)
telno.place(x=580, y=170)

# Veri Giriş 12
etiket15 = tkinter.Label(pencere, text="ek bilgiler", font="Xirod-regular 10", fg="white", bg="#363636")
etiket15.place(x=8, y=230)
ekbilgiler = tkinter.Text(pencere, font="Arial 11",bd=5, bg="#e6c619", height=15, width=28)
ekbilgiler.place(x=8, y=250)




etiket16 = tkinter.Label(pencere, text="resim/dosya yükle", font="Xirod-regular 10", fg="white", bg="#363636")
etiket16.place(x=270, y=270)
yüklemeresim = tkinter.Label(pencere, image=uploadresim, height=182, width=182)
yüklemeresim.place(x=280, y=290)

uploadbuton = tkinter.Button(pencere, image=yuklebuton, bg="#363636", activebackground="#e6c619")
uploadbuton.place(x=350, y=760)

# Kaydet Butonu
submit_btn = tkinter.Button(pencere, bg="#363636", bd=5, activebackground="#e6c619", height=30, width=60,image=kaydetbuton, command=submit )
submit_btn.place(x=550,y=330)

# Çıkış Butonu
cikis = tkinter.Button(pencere, height=30, width=60, bd=5 ,image=cikisbuton, bg="#363636", activebackground="#e6c619", command=pencere.quit)
cikis.place(x=550, y=400)




pencere.mainloop()