from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Toplevel,Label
from tkinter import ttk
import os
import time


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Administrator\Desktop\Yazılım\bilgisayar kapatıcı\build\assets\frame0")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def kapatiptal_button_fonksiyon():
    kapatiptalkomut = f"shutdown /a"
    os.system(kapatiptalkomut)
    yeni_pencere = Toplevel(window)
    yeni_pencere.geometry("350x100")
    window.resizable(False, False)
    def kapat():
        print("destroy pencere")
        yeni_pencere.destroy()
    yeni_pencere.title("Bilgilendirme")
    yeni_etiket = Label(yeni_pencere, text="varsayılan kapatma Durduruldu",font=('Montserrat 16'))
    closebutton = Button(yeni_pencere,text="Tamam",font=('Montserrat 16'),command =kapat)
    closebutton.place(x=130,y=40)
    yeni_etiket.pack()

def kapatma_komutu(saniye):
    if not hasattr(kapatma_komutu, 'called') or not kapatma_komutu.called:
        print("Fonksiyon ilk kez çağrıldı.")
        kapatma_komutu.called = True
        komut = f"shutdown /s /f /t {saniye}"

        if dakika_entry.get() == "":
            print (saat_entry.get(),"saat sonra kapatılacak")
            os.system(komut)

        elif saat_entry.get() == "":
            print (dakika_entry.get(),"dakika sonra kapatılacak")
            os.system(komut)   

        else:
            print (saat_entry.get(),"saat", dakika_entry.get(),"dakika sonra kapatılacak")
            os.system(komut)
    else:
        print("ilkinci cagırma htsı")
        kapatma_komutu.called=False
        hatapencere1()


def kapatma_button():
    print("kapat_button fonskiyon")
    if dakika_entry.get() == "" and saat_entry.get() == "":
        print("Dakika ve saat boş")
        saniye=0
        yeni_pencere()
    else:
        
        if saat_entry.get() == "":
            saat_entry.get() == 0
            dakika = int(dakika_entry.get())
            saniye = dakika * 60
            kapatma_komutu(saniye)

        if dakika_entry.get() == "":
            dakika_entry.get() == 0
            saat = int(saat_entry.get())
            saniye = saat * 3600
            kapatma_komutu(saniye)   

        else :
            saat = int(saat_entry.get())
            dakika = saat * 60 + int(dakika_entry.get())
            saniye = dakika * 60
            kapatma_komutu(saniye)

def bilgisayarıkapat():
    komut = f"shutdown /s /f /t 0"
    os.system(komut)

def yeni_pencere():
    yeni_pencere = Toplevel(window)
    window.resizable(False, False)
    def kapat():
        print("destroy pencere")
        yeni_pencere.destroy()
    
    yeni_pencere.title("Bilgilendirme")
    yeni_pencere.geometry("350x125")
    yazı1 = Label(yeni_pencere, text="Saat ve dakika boş bırakılamaz.",font=('Montserrat 16'))
    yazı1.pack()
    yazı2 = Label(yeni_pencere, text="isterseniz hemen şimdi kapatın.",font=('Montserrat 16'))
    yazı2.pack()
    geridonbutton = Button(yeni_pencere,text = "Geri Dön",height= 2, width=15,font=('Montserrat 12'),command =kapat)
    geridonbutton.place(x=10,y=70)
    kapatbutton = Button(yeni_pencere,text = "Bilgisayarı Kapat",height= 2, width=15,font=('Montserrat 12'),command =bilgisayarıkapat)
    kapatbutton.place(x=200,y=70)

def hatapencere1():
    yeni_pencere = Toplevel(window)
    window.resizable(False, False)
    def kapat():
        print("destroy pencere")
        yeni_pencere.destroy()
    def coklukapatiptal_button_fonksiyon():
        kapat()
        kapatiptal_button_fonksiyon()
    yeni_pencere.title("Bilgilendirme")
    yeni_pencere.geometry("350x125")
    yazı1metin = "Halihazırda kapatma komutu girilmiş.\nYeni bir kapatma komutu oluşturmak için\n'varsayılan kapatmayı durdur'a tıklayın. "
    yazı2metin = ""
    yazı1 = Label(yeni_pencere, text=yazı1metin,font=('Montserrat 13'))
    yazı1.pack()
    yazı2 = Label(yeni_pencere, text=yazı2metin,font=('Montserrat 10'))
    yazı2.pack()
    geridonbutton = Button(yeni_pencere,text = "Geri Dön",height= 2, width=15,font=('Montserrat 9'),command =kapat)
    geridonbutton.place(x=10,y=70)
    kapatbutton = Button(yeni_pencere,text = "varsayılan kapatmayı durdur",height= 2, width=22,font=('Montserrat 12'),command =coklukapatiptal_button_fonksiyon)
    kapatbutton.place(x=140,y=62)


window = Tk()

window.geometry("400x125")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 125,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    200.0,
    20.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    98.0,
    60.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    294.0,
    60.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    262.0,
    60.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    200.0,
    20.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    59.0,
    60.0,
    image=image_image_6
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
kapat_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=kapatma_button,
    relief="flat"
)
kapat_button.place(
    x=295.0,
    y=85.0,
    width=80.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
kapatiptal_button = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=kapatiptal_button_fonksiyon,
    relief="flat"
)
kapatiptal_button.place(
    x=13.0,
    y=85.0,
    width=282.0,
    height=30.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    130.0,
    60.0,
    image=entry_image_1
)
saat_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat 16')
)
saat_entry.place(
    x=95.0,
    y=45.0,
    width=70.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    335.0,
    60.0,
    image=entry_image_2
)
dakika_entry = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=('Montserrat 16')
)
dakika_entry.place(
    x=309.0,
    y=45.0,
    width=52.0,
    height=28.0
)
window.resizable(False, False)
window.mainloop()
