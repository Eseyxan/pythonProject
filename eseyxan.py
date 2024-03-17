from tkinter import *
import tkinter as tk

import pygame.mixer
from PIL import Image, ImageTk
from  tkinter.ttk import  Notebook
from PIL.ImageTk import PhotoImage

def play1():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\eminemchart.mp3')
    pygame.mixer.music.play(loops=0)
def play2():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\drakechart.mp3')
    pygame.mixer.music.play(loops=0)
def play3():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\weekndchart.mp3')
    pygame.mixer.music.play(loops=0)
def play4():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\staychart.mp3')
    pygame.mixer.music.play(loops=0)
def play5():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\emi1.mp3')
    pygame.mixer.music.play(loops=0)
def play6():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\emi2.mp3')
    pygame.mixer.music.play(loops=0)
def play7():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\emi3.mp3')
    pygame.mixer.music.play(loops=0)
def play8():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\praise.mp3')
    pygame.mixer.music.play(loops=0)
def play9():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\flash.mp3')
    pygame.mixer.music.play(loops=0)
def play10():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\offthe.mp3')
    pygame.mixer.music.play(loops=0)
def play11():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\stronger.mp3')
    pygame.mixer.music.play(loops=0)
def play12():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\heartsong.mp3')
    pygame.mixer.music.play(loops=0)
def play13():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\lightsong.mp3')
    pygame.mixer.music.play(loops=0)
def play14():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\starboysong.mp3')
    pygame.mixer.music.play(loops=0)
def play15():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\alarmsong.mp3')
    pygame.mixer.music.play(loops=0)
def play16():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\olimpicosong.mp3')
    pygame.mixer.music.play(loops=0)
def play17():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\strangersong.mp3')
    pygame.mixer.music.play(loops=0)
def play18():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\crownsong.mp3')
    pygame.mixer.music.play(loops=0)
def play19():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\Flysong.mp3')
    pygame.mixer.music.play(loops=0)
def play20():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\animalsong.mp3')
    pygame.mixer.music.play(loops=0)
def play21():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\polosong.mp3')
    pygame.mixer.music.play(loops=0)
def play22():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\ramoksong.mp3')
    pygame.mixer.music.play(loops=0)
def play23():
        pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\lifesong.mp3')
        pygame.mixer.music.play(loops=0)
def play24():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\olsenemessong.mp3')
    pygame.mixer.music.play(loops=0)
def play25():
        pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\jureksong.mp3')
        pygame.mixer.music.play(loops=0)
def play26():
        pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\almatysong.mp3')
        pygame.mixer.music.play(loops=0)
def play27():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\universesong.mp3')
    pygame.mixer.music.play(loops=0)
def play28():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\danceofknight.mp3')
    pygame.mixer.music.play(loops=0)
def play29():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\FurElise.mp3')
    pygame.mixer.music.play(loops=0)
def play30():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\swanlake.mp3')
    pygame.mixer.music.play(loops=0)
def play31():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\mocart.mp3')
    pygame.mixer.music.play(loops=0)
def play32():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\synt11.mp3')
    pygame.mixer.music.play(loops=0)
def play33():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\synt22.mp3')
    pygame.mixer.music.play(loops=0)
def play34():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\synt33.mp3')
    pygame.mixer.music.play(loops=0)
def play35():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\synt44.mp3')
    pygame.mixer.music.play(loops=0)
def play36():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\adai.mp3')
    pygame.mixer.music.play(loops=0)
def play37():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\2classsong.mp3')
    pygame.mixer.music.play(loops=0)
def play38():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\33song.mp3')
    pygame.mixer.music.play(loops=0)
def play39():
    pygame.mixer.music.load(r'C:\Users\bossa\Downloads\PhotoMusic\song444.mp3')
    pygame.mixer.music.play(loops=0)
def stop():
    pygame.mixer.music.stop()

#Главная
def new_vidjet1():
    tab1_control = Notebook(window)
    tab_1 = Frame(tab1_control)
    tab1_control.add(tab_1, text="Главная")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img,bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\gray.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    text1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\text1.png')
    text1 = ImageTk.PhotoImage(text1)
    text1_label = Label(image=text1)
    text1_label.image = text1
    text1_label.place(x=400, y=30)
    text2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\text2.png')
    text2 = ImageTk.PhotoImage(text2)
    text2_label = Label(image=text2)
    text2_label.image = text2
    text2_label.place(x=400, y=420)

    eminem_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\eminem.png')
    eminem_photo = ImageTk.PhotoImage(eminem_photo)
    eminem_label = Label(image=eminem_photo)
    eminem_label.image = eminem_photo
    eminem_label.place(x=400, y=100)
    btn_eminem = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Eminem1.png')
    btn_eminem = ImageTk.PhotoImage(btn_eminem)
    btneminem_label = Label(image=btn_eminem)
    btneminem_label.image = btn_eminem
    Button(window, image=btn_eminem, highlightthickness=0, bd=0, command=eminem_new).place(x=470, y=350)

    kanye_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Kanye.png')
    kanye_photo = ImageTk.PhotoImage(kanye_photo)
    kanye_label = Label(image=kanye_photo)
    kanye_label.image = kanye_photo
    kanye_label.place(x=730, y=100)
    btn_kanye = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Kanye1.png')
    btn_kanye = ImageTk.PhotoImage(btn_kanye)
    btnkanye_label = Label(image=btn_kanye)
    btnkanye_label.image = btn_kanye
    Button(window, image=btn_kanye, highlightthickness=0, bd=0, command=kanye_new).place(x=770, y=350)

    weeknd_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Weeknd.png')
    weeknd_photo = ImageTk.PhotoImage(weeknd_photo)
    weeknd_label = Label(image=weeknd_photo)
    weeknd_label.image = weeknd_photo
    weeknd_label.place(x=1060, y=100)
    btn_weeknd = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Weeknd1.png')
    btn_weeknd = ImageTk.PhotoImage(btn_weeknd)
    btnweeknd_label = Label(image=btn_weeknd)
    btnweeknd_label.image = btn_weeknd
    Button(window, image=btn_weeknd, highlightthickness=0, bd=0, command=weeknd_new).place(x=1090, y=350)

    dimash_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\dimash.png')
    dimash_photo = ImageTk.PhotoImage(dimash_photo)
    dimash_label = Label(image=dimash_photo)
    dimash_label.image = dimash_photo
    dimash_label.place(x=400, y=490)
    btn_dimash = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Dimash1.png')
    btn_dimash = ImageTk.PhotoImage(btn_dimash)
    btndimash_label = Label(image=btn_dimash)
    btndimash_label.image = btn_dimash
    Button(window, image=btn_dimash, highlightthickness=0, bd=0, command=dimashh_new).place(x=420, y=740)

    scryp_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Scryp.png')
    scryp_photo = ImageTk.PhotoImage(scryp_photo)
    scryp_label = Label(image=scryp_photo)
    scryp_label.image = scryp_photo
    scryp_label.place(x=730, y=490)
    btn_scryp = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Scryp1.png')
    btn_scryp = ImageTk.PhotoImage(btn_scryp)
    btnscryp_label = Label(image=btn_scryp)
    btnscryp_label.image = btn_scryp
    Button(window, image=btn_scryp, highlightthickness=0, bd=0, command=scyptonit_new).place(x=760, y=740)

    nurtas_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Kairat.png')
    nurtas_photo = ImageTk.PhotoImage(nurtas_photo)
    nurtas_label = Label(image=nurtas_photo)
    nurtas_label.image = nurtas_photo
    nurtas_label.place(x=1060, y=490)
    btn_nurtas = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\kairat1.png')
    btn_nurtas = ImageTk.PhotoImage(btn_nurtas)
    btnnurtas_label = Label(image=btn_nurtas)
    btnnurtas_label.image = btn_nurtas
    Button(window, image=btn_nurtas, highlightthickness=0, bd=0, command=kair_new).place(x=1070, y=740)

def eminem_new():
    tab1_control = Notebook(window)
    tab_1 = Frame(tab1_control)
    tab1_control.add(tab_1, text="Eminem")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\gray.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    eminemm_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\emibanner.png')
    eminemm_img = eminemm_img.resize((900, 400))
    eminemm_img = ImageTk.PhotoImage(eminemm_img)
    eminemm_img_label = Label(image=eminemm_img, bd=0)
    eminemm_img_label.image = eminemm_img
    eminemm_img_label.place(x=460, y=50)

    eminem1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\cover1.png')
    eminem1_photo = eminem1_photo.resize((100, 100))
    eminem1_photo = ImageTk.PhotoImage(eminem1_photo)
    eminem1_label = Label(image=eminem1_photo, bg='#1F2735')
    eminem1_label.image = eminem1_photo
    eminem1_label.place(x=360, y=500)
    btn_eminem1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\M.png')
    btn_eminem1 = ImageTk.PhotoImage(btn_eminem1)
    btneminem1_label = Label(image=btn_eminem1)
    btneminem1_label.image = btn_eminem1
    Button(window, image=btn_eminem1, highlightthickness=0, bd=0, activebackground='gray', command=play1).place(x=490, y=530)

    eminem1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\banner12.png')
    eminem1_photo = eminem1_photo.resize((100, 100))
    eminem1_photo = ImageTk.PhotoImage(eminem1_photo)
    eminem1_label = Label(image=eminem1_photo, bg='#1F2735')
    eminem1_label.image = eminem1_photo
    eminem1_label.place(x=950, y=500)
    btn_eminem1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Godzilla.png')
    btn_eminem1 = ImageTk.PhotoImage(btn_eminem1)
    btneminem1_label = Label(image=btn_eminem1)
    btneminem1_label.image = btn_eminem1
    Button(window, image=btn_eminem1, highlightthickness=0, bd=0, activebackground='gray', command=play7).place(x=1075, y=530)

    eminem1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Curtain.png')
    eminem1_photo = eminem1_photo.resize((100, 100))
    eminem1_photo = ImageTk.PhotoImage(eminem1_photo)
    eminem1_label = Label(image=eminem1_photo, bg='#1F2735')
    eminem1_label.image = eminem1_photo
    eminem1_label.place(x=950, y=650)
    btn_eminem1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Stan.png')
    btn_eminem1 = ImageTk.PhotoImage(btn_eminem1)
    btneminem1_label = Label(image=btn_eminem1)
    btneminem1_label.image = btn_eminem1
    Button(window, image=btn_eminem1, highlightthickness=0, bd=0, activebackground='gray', command=play5).place(x=1075, y=680)

    eminem1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Curtain.png')
    eminem1_photo = eminem1_photo.resize((100, 100))
    eminem1_photo = ImageTk.PhotoImage(eminem1_photo)
    eminem1_label = Label(image=eminem1_photo, bg='#1F2735')
    eminem1_label.image = eminem1_photo
    eminem1_label.place(x=360, y=650)
    btn_eminem1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\LoseYourself.png')
    btn_eminem1 = ImageTk.PhotoImage(btn_eminem1)
    btneminem1_label = Label(image=btn_eminem1)
    btneminem1_label.image = btn_eminem1
    Button(window, image=btn_eminem1, highlightthickness=0, bd=0, activebackground='gray', command=play6).place(x=490, y=680)

    # StopButtonMusic
    btn_stop = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop = btn_stop.resize((50, 50))
    btn_stop = ImageTk.PhotoImage(btn_stop)
    btnstop_label = Label(image=btn_stop)
    btnstop_label.image = btn_stop
    Button(window, image=btn_stop, highlightthickness=0, bd=0, command=stop).place(x=305, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=305, y=675)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=680)
def kanye_new():
    tab1_control = Notebook(window)
    tab_1 = Frame(tab1_control)
    tab1_control.add(tab_1, text="Kanye")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\gray.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #Banner_code
    west_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\west.png')
    west_img = west_img.resize((900, 400))
    west_img = ImageTk.PhotoImage(west_img)
    west_img_label = Label(image=west_img, bd=0)
    west_img_label.image = west_img
    west_img_label.place(x=460, y=50)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\west1.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    west1_label.place(x=360, y=500)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\btnwest2.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bd=0, activebackground='gray', command=play8).place(x=490, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\west1.png')
    west_photo =  west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage( west_photo)
    west_label = Label(image= west_photo, bg='#1F2735')
    west_label.image =  west_photo
    west_label.place(x=950, y=500)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\btnwest3.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play10).place(x=1075, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\west2.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=950, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\btnwest1.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play11).place(x=1075, y=680)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\west2.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=360, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\west22.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play9).place(x=490, y=680)

    # StopButtonMusic
    btn_stop = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop = btn_stop.resize((50, 50))
    btn_stop = ImageTk.PhotoImage(btn_stop)
    btnstop_label = Label(image=btn_stop)
    btnstop_label.image = btn_stop
    Button(window, image=btn_stop, highlightthickness=0, bd=0, command=stop).place(x=305, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=305, y=675)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=680)
def weeknd_new():
    tab1_control = Notebook(window)
    tab_1 = Frame(tab1_control)
    tab1_control.add(tab_1, text="Weeknd")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\gray.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #Banner_code
    west_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\weknd.png')
    west_img = west_img.resize((900, 400))
    west_img = ImageTk.PhotoImage(west_img)
    west_img_label = Label(image=west_img, bd=0)
    west_img_label.image = west_img
    west_img_label.place(x=460, y=50)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\blood.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    west1_label.place(x=360, y=500)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\heart.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bd=0, activebackground='gray', command=play12).place(x=490, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\blood.png')
    west_photo =  west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage( west_photo)
    west_label = Label(image= west_photo, bg='#1F2735')
    west_label.image =  west_photo
    west_label.place(x=950, y=500)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\light1.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play13).place(x=1075, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\star.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=950, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\starboy.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play14).place(x=1075, y=680)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\star.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=360, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\alarm.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play15).place(x=490, y=680)

    # StopButtonMusic
    btn_stop = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop = btn_stop.resize((50, 50))
    btn_stop = ImageTk.PhotoImage(btn_stop)
    btnstop_label = Label(image=btn_stop)
    btnstop_label.image = btn_stop
    Button(window, image=btn_stop, highlightthickness=0, bd=0, command=stop).place(x=305, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=305, y=675)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=680)
def dimashh_new():
    tab1_control = Notebook(window)
    tab_1 = Frame(tab1_control)
    tab1_control.add(tab_1, text="Dimash")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\gray.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #Banner_code
    west_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\dimabanner.png')
    west_img = west_img.resize((900, 400))
    west_img = ImageTk.PhotoImage(west_img)
    west_img_label = Label(image=west_img, bd=0)
    west_img_label.image = west_img
    west_img_label.place(x=460, y=50)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\bannerr.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    west1_label.place(x=360, y=500)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\olimp.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bd=0, activebackground='gray', command=play16).place(x=490, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\bannerr.png')
    west_photo =  west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage( west_photo)
    west_label = Label(image= west_photo, bg='#1F2735')
    west_label.image =  west_photo
    west_label.place(x=950, y=500)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stranger.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play17).place(x=1075, y=520)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\fly.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=950, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\flyaway.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play19).place(x=1075, y=680)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\crownbanner.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=360, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\cc.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play18).place(x=490, y=680)

    # StopButtonMusic
    btn_stop = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop = btn_stop.resize((50, 50))
    btn_stop = ImageTk.PhotoImage(btn_stop)
    btnstop_label = Label(image=btn_stop)
    btnstop_label.image = btn_stop
    Button(window, image=btn_stop, highlightthickness=0, bd=0, command=stop).place(x=305, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=305, y=675)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=680)
def scyptonit_new():
    tab1_control = Notebook(window)
    tab_1 = Frame(tab1_control)
    tab1_control.add(tab_1, text="Scryptonit")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\gray.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #Banner_code
    west_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\scrypbanner.png')
    west_img = west_img.resize((900, 400))
    west_img = ImageTk.PhotoImage(west_img)
    west_img_label = Label(image=west_img, bd=0)
    west_img_label.image = west_img
    west_img_label.place(x=460, y=50)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\36.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    west1_label.place(x=360, y=500)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\animal.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bd=0, activebackground='gray', command=play20).place(x=480, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\36.png')
    west_photo =  west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage( west_photo)
    west_label = Label(image= west_photo, bg='#1F2735')
    west_label.image =  west_photo
    west_label.place(x=950, y=500)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\polo.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play21).place(x=1075, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\svistki.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=950, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\ramoknet.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play22).place(x=1075, y=680)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\svistki.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=360, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\jitkak.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play23).place(x=490, y=680)

    # StopButtonMusic
    btn_stop = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop = btn_stop.resize((50, 50))
    btn_stop = ImageTk.PhotoImage(btn_stop)
    btnstop_label = Label(image=btn_stop)
    btnstop_label.image = btn_stop
    Button(window, image=btn_stop, highlightthickness=0, bd=0, command=stop).place(x=305, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=305, y=675)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=680)
def kair_new():
    tab1_control = Notebook(window)
    tab_1 = Frame(tab1_control)
    tab1_control.add(tab_1, text="Kairat_Nurtas")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\gray.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #Banner_code
    west_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\kairbanner.png')
    west_img = west_img.resize((900, 400))
    west_img = ImageTk.PhotoImage(west_img)
    west_img_label = Label(image=west_img, bd=0)
    west_img_label.image = west_img
    west_img_label.place(x=460, y=50)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\kaircover.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    west1_label.place(x=360, y=500)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\olsenemes.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bd=0, activebackground='gray', command=play24).place(x=480, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\kaircover.png')
    west_photo =  west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage( west_photo)
    west_label = Label(image= west_photo, bg='#1F2735')
    west_label.image =  west_photo
    west_label.place(x=950, y=500)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\jurek.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play25).place(x=1075, y=530)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\coverkair2.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=950, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\almaty.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play26).place(x=1075, y=680)

    west_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\coverkair1.png')
    west_photo = west_photo.resize((100, 100))
    west_photo = ImageTk.PhotoImage(west_photo)
    west_label = Label(image=west_photo, bg='#1F2735')
    west_label.image = west_photo
    west_label.place(x=360, y=650)
    btn_west = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\univers.png')
    btn_west = ImageTk.PhotoImage(btn_west)
    btn_west_label = Label(image=btn_west)
    btn_west_label.image = btn_west
    Button(window, image=btn_west, highlightthickness=0, bd=0, activebackground='gray', command=play27).place(x=490, y=680)

    # StopButtonMusic
    btn_stop = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop = btn_stop.resize((50, 50))
    btn_stop = ImageTk.PhotoImage(btn_stop)
    btnstop_label = Label(image=btn_stop)
    btnstop_label.image = btn_stop
    Button(window, image=btn_stop, highlightthickness=0, bd=0, command=stop).place(x=305, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=305, y=675)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=530)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, command=stop).place(x=895, y=680)
#Чарты
def new_vidjet2():
    tab1_control = Notebook(window)
    tab2 = Frame(tab1_control)
    tab1_control.add(tab2, text="Чарты")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img,bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\fonchart.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet3).place(x=80, y=290)

    #Лого2
    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    text3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\topchart.png')
    text3 = ImageTk.PhotoImage(text3)
    text3_label = Label(image=text3, bg='#1F2735')
    text3_label.image = text3
    text3_label.place(x=500, y=20)

    #ЧартыМузыка
    eminem1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\cover1.png')
    eminem1_photo = ImageTk.PhotoImage(eminem1_photo)
    eminem1_label = Label(image=eminem1_photo, bg='#1F2735')
    eminem1_label.image = eminem1_photo
    eminem1_label.place(x=500, y=130)
    btn_eminem1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\songchart1.png')
    btn_eminem1 = ImageTk.PhotoImage(btn_eminem1)
    btneminem1_label = Label(image=btn_eminem1)
    btneminem1_label.image = btn_eminem1
    Button(window, image=btn_eminem1, highlightthickness=0, bd=0, activebackground='#1F2735', bg='#1F2735', command=play1).place(x=670, y=170)


    drake_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\cover2.png')
    drake_photo = ImageTk.PhotoImage(drake_photo)
    drake_label = Label(image=drake_photo, bg='#1F2735')
    drake_label.image = drake_photo
    drake_label.place(x=500, y=300)
    btn_drake = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\songchart2.png')
    btn_drake = ImageTk.PhotoImage(btn_drake)
    btndrake_label = Label(image=btn_drake)
    btndrake_label.image = btn_drake
    Button(window, image=btn_drake, highlightthickness=0, bd=0, activebackground='#1F2735', bg='#1F2735', command=play2).place(x=670, y=340)

    weeknd1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\cover3.png')
    weeknd1_photo = ImageTk.PhotoImage(weeknd1_photo)
    weeknd1_label = Label(image=weeknd1_photo,bg='#1F2735')
    weeknd1_label.image = weeknd1_photo
    weeknd1_label.place(x=500, y=470)
    btn_weeknd1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\songchart3.png')
    btn_weeknd1 = ImageTk.PhotoImage(btn_weeknd1)
    btnweeknd1_label = Label(image=btn_weeknd1)
    btnweeknd1_label.image = btn_weeknd1
    Button(window, image=btn_weeknd1, highlightthickness=0, bd=0, activebackground='#1F2735', bg='#1F2735', command=play3).place(x=670, y=510)

    stay_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\cover4.png')
    stay_photo = ImageTk.PhotoImage(stay_photo)
    stay_label = Label(image=stay_photo, bg='#1F2735')
    stay_label.image = stay_photo
    stay_label.place(x=500, y=640)
    btn_stay = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\songchart4.png')
    btn_stay = ImageTk.PhotoImage(btn_stay)
    btnstay_label = Label(image=btn_stay)
    btnstay_label.image = btn_stay
    Button(window, image=btn_stay, highlightthickness=0, bd=0, activebackground='#1F2735', bg='#1F2735', command=play4).place(x=670, y=670)

    #StopButtonMusic
    btn_stop = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop = btn_stop.resize((50, 50))
    btn_stop = ImageTk.PhotoImage(btn_stop)
    btnstop_label = Label(image=btn_stop)
    btnstop_label.image = btn_stop
    Button(window,image=btn_stop, highlightthickness=0, bd=0, bg='#1F2735', activebackground='#1F2735', command=stop).place(x=430, y=175)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, bg='#1F2735', activebackground='#1F2735', command=stop).place(x=430, y=350)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, bg='#1F2735', activebackground='#1F2735',command=stop).place(x=430, y=525)

    btn_stop1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\stop.png')
    btn_stop1 = btn_stop1.resize((50, 50))
    btn_stop1 = ImageTk.PhotoImage(btn_stop1)
    btnstop1_label = Label(image=btn_stop1)
    btnstop1_label.image = btn_stop1
    Button(window, image=btn_stop1, highlightthickness=0, bd=0, bg='#1F2735', activebackground='#1F2735', command=stop).place(x=430, y=680)

#Плейлисты
def new_vidjet3():
    tab1_control = Notebook(window)
    tab3 = Frame(tab1_control)
    tab1_control.add(tab3, text="Плейлисты")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\whitefon.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #PlaylistMain
    text3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\textPlaylist.png')
    text3 = ImageTk.PhotoImage(text3)
    text3_label = Label(image=text3, bg='white')
    text3_label.image = text3
    text3_label.place(x=400, y=40)

    synthwave = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Synthwaveclassic.png')
    synthwave = ImageTk.PhotoImage(synthwave)
    synthwave_label = Label(image=synthwave, bg='#1F2735')
    synthwave_label.image = synthwave
    synthwave_label.place(x=400, y=130)
    btn_synthwave= Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\SynthwavePlaylist.png')
    btn_synthwave = ImageTk.PhotoImage(btn_synthwave)
    btnsynthwave_label = Label(image=btn_synthwave)
    btnsynthwave_label.image = btn_synthwave
    Button(window, image=btn_synthwave, highlightthickness=0, bd=0, bg='white', activebackground='white', command=new_synthwave).place(x=440, y=380)

    qazaq = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\qazaqclassic.png')
    qazaq = ImageTk.PhotoImage(qazaq)
    qazaq_label = Label(image=qazaq, bg='#1F2735')
    qazaq_label.image = qazaq
    qazaq_label.place(x=800, y=130)
    btn_qazaq = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\QazaqClassiPlaylist.png')
    btn_qazaq = ImageTk.PhotoImage(btn_qazaq)
    btnqazaq_label = Label(image=btn_qazaq)
    btnqazaq_label.image = btn_qazaq
    Button(window, image=btn_qazaq, highlightthickness=0, bd=0, bg='white', activebackground='white', command=new_qazaq).place(x=820, y=380)

    classic = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\classic.png')
    classic = ImageTk.PhotoImage(classic)
    classic_label = Label(image=classic, bg='#1F2735')
    classic_label.image = classic
    classic_label.place(x=1200, y=130)
    btn_classic = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\ClassicalMusicPlaylist.png')
    btn_classic= ImageTk.PhotoImage(btn_classic)
    btnclassic_label = Label(image=btn_classic)
    btnclassic_label.image = btn_classic
    Button(window, image=btn_classic, highlightthickness=0, bd=0, bg='white', activebackground='white', command=new_classic).place(x=1200, y=380)
def new_classic():
    tab1_control = Notebook(window)
    tab3 = Frame(tab1_control)
    tab1_control.add(tab3, text="Classic")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\whitefon.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #PlayList
    text3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\textPlaylist.png')
    text3 = ImageTk.PhotoImage(text3)
    text3_label = Label(image=text3, bg='white')
    text3_label.image = text3
    text3_label.place(x=400, y=40)
    classic = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\classic.png')
    classic = classic.resize((350, 350))
    classic = ImageTk.PhotoImage(classic)
    classic_label = Label(image=classic, bg='#1F2735')
    classic_label.image = classic
    classic_label.place(x=400, y=130)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\classic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=130)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\class1.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white",  command=play28).place(x=930, y=140)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\classic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=280)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\class2.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white", command=play29).place(x=930, y=315)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\classic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=430)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\class3.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white",command=play30).place(x=930, y=450)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\classic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=580)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\class4.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white", command=play31).place(x=930, y=620)
def new_synthwave():
    tab1_control = Notebook(window)
    tab3 = Frame(tab1_control)
    tab1_control.add(tab3, text="Synthwave")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\whitefon.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #PlayList
    text3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\textPlaylist.png')
    text3 = ImageTk.PhotoImage(text3)
    text3_label = Label(image=text3, bg='white')
    text3_label.image = text3
    text3_label.place(x=400, y=40)
    classic = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Synthwaveclassic.png')
    classic = classic.resize((350, 350))
    classic = ImageTk.PhotoImage(classic)
    classic_label = Label(image=classic, bg='#1F2735')
    classic_label.image = classic
    classic_label.place(x=400, y=130)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Synthwaveclassic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=130)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\synt1.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white",  command=play32).place(x=930, y=165)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Synthwaveclassic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=280)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\synt2.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white", command=play33).place(x=930, y=315)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Synthwaveclassic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=430)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\synt3.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white",command=play34).place(x=930, y=450)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Synthwaveclassic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=580)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\synt4.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white", command=play35).place(x=930, y=595)
def new_qazaq():
    tab1_control = Notebook(window)
    tab3 = Frame(tab1_control)
    tab1_control.add(tab3, text="Qazaq")
    tab1_control.pack(expand=1, fill='both')

    kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
    kvadrat_img = kvadrat_img.resize((300, 1200))
    kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
    kvadrat_label = Label(image=kvadrat_img, bd=0)
    kvadrat_label.image = kvadrat_img
    kvadrat_label.place(x=0, y=0)

    kvadrat1_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\whitefon.png')
    kvadrat1_img = kvadrat1_img.resize((2500, 1100))
    kvadrat1_img = ImageTk.PhotoImage(kvadrat1_img)
    kvadrat1_label = Label(image=kvadrat1_img, bd=0)
    kvadrat1_label.image = kvadrat1_img
    kvadrat1_label.place(x=300, y=0)

    logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
    logo_img = logo_img.resize((80, 80))
    logo_img = ImageTk.PhotoImage(logo_img)
    logo_label = Label(image=logo_img, bg='#101E33')
    logo_label.image = logo_img
    logo_label.place(x=40, y=30)
    logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
    logo_img1 = ImageTk.PhotoImage(logo_img1)
    logo_label1 = Label(image=logo_img1, bg='#101E33')
    logo_label1.image = logo_img1
    logo_label1.place(x=120, y=40)

    btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
    btn1 = ImageTk.PhotoImage(btn1)
    btn1_label = Label(image=btn1)
    btn1_label.image = btn1
    Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet1).place(x=80, y=170)
    btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
    btn2 = ImageTk.PhotoImage(btn2)
    btn2_label = Label(image=btn2)
    btn2_label.image = btn2
    Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet2).place(x=80, y=230)
    btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
    btn3 = ImageTk.PhotoImage(btn3)
    btn3_label = Label(image=btn3)
    btn3_label.image = btn3
    Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0,
           command=new_vidjet3).place(x=80, y=290)

    logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
    logo_btn = ImageTk.PhotoImage(logo_btn)
    logo_label_btn = Label(image=logo_btn, bg='#101E33')
    logo_label_btn.image = logo_btn
    logo_label_btn.place(x=30, y=165)
    logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
    logo_btn1 = ImageTk.PhotoImage(logo_btn1)
    logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
    logo_label_btn1.image = logo_btn1
    logo_label_btn1.place(x=30, y=220)
    logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
    logo_btn2 = ImageTk.PhotoImage(logo_btn2)
    logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
    logo_label_btn2.image = logo_btn2
    logo_label_btn2.place(x=30, y=280)

    #PlayList
    text3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\textPlaylist.png')
    text3 = ImageTk.PhotoImage(text3)
    text3_label = Label(image=text3, bg='white')
    text3_label.image = text3
    text3_label.place(x=400, y=40)
    classic = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\qazaqclassic.png')
    classic = classic.resize((350, 350))
    classic = ImageTk.PhotoImage(classic)
    classic_label = Label(image=classic, bg='#1F2735')
    classic_label.image = classic
    classic_label.place(x=400, y=130)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\qazaqclassic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=130)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\adai1.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white",  command=play36).place(x=930, y=165)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\qazaqclassic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=280)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\qamajai.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white", command=play37).place(x=930, y=315)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\qazaqclassic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=430)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\3song.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white",command=play38).place(x=930, y=450)

    west1_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\qazaqclassic.png')
    west1_photo = west1_photo.resize((100, 100))
    west1_photo = ImageTk.PhotoImage(west1_photo)
    west1_label = Label(image=west1_photo, bg='#1F2735')
    west1_label.image = west1_photo
    Button(window, image=west1_photo, activebackground="white", highlightthickness=0, bd=0, command=stop).place(x=800, y=580)
    btn_west1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\song23.png')
    btn_west1 = ImageTk.PhotoImage(btn_west1)
    btnwest1_label = Label(image=btn_west1)
    btnwest1_label.image = btn_west1
    Button(window, image=btn_west1, highlightthickness=0, bg="white", bd=0, activebackground="white", command=play39).place(x=930, y=595)


window = Tk()
window.title("Esey Muisc")
window.geometry('1920x1080')
window.iconbitmap(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')

pygame.mixer.init()

kvadrat_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\rectangle.png')
kvadrat_img = kvadrat_img.resize((300, 1200))
kvadrat_img = ImageTk.PhotoImage(kvadrat_img)
kvadrat_label = Label(image=kvadrat_img,bd=0)
kvadrat_label.image =kvadrat_img
kvadrat_label.place(x=0, y=0)


#logo
logo_img = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\icons.png')
logo_img = logo_img.resize((80, 80))
logo_img = ImageTk.PhotoImage(logo_img)
logo_label = Label(image=logo_img, bg='#101E33')
logo_label.image = logo_img
logo_label.place(x=40, y=30)

logo_img1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logoEsey.png')
logo_img1 = ImageTk.PhotoImage(logo_img1)
logo_label1 = Label(image=logo_img1, bg='#101E33')
logo_label1.image =logo_img1
logo_label1.place(x=120, y=40)


#Button
btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\main.png')
btn1 = ImageTk.PhotoImage(btn1)
btn1_label = Label(image=btn1)
btn1_label.image = btn1
Button(window, image=btn1, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet1).place(x=80, y=170)

btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\charts.png')
btn2 = ImageTk.PhotoImage(btn2)
btn2_label = Label(image=btn2)
btn2_label.image = btn2
Button(window, image=btn2, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet2).place(x=80, y=230)

btn3 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\playlist.png')
btn3 = ImageTk.PhotoImage(btn3)
btn3_label = Label(image=btn3)
btn3_label.image = btn3
Button(window, image=btn3, bg='#101E33', highlightthickness=0, activebackground='#1F2735', bd=0, command=new_vidjet3).place(x=80, y=290)


#Logo_Button
logo_btn = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn.png')
logo_btn = ImageTk.PhotoImage(logo_btn)
logo_label_btn = Label(image=logo_btn, bg='#101E33')
logo_label_btn.image =logo_btn
logo_label_btn.place(x=30, y=165)

logo_btn1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn2.png')
logo_btn1 = ImageTk.PhotoImage(logo_btn1)
logo_label_btn1 = Label(image=logo_btn1, bg='#101E33')
logo_label_btn1.image =logo_btn1
logo_label_btn1.place(x=30, y=220)

logo_btn2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\logobtn3.png')
logo_btn2 = ImageTk.PhotoImage(logo_btn2)
logo_label_btn2 = Label(image=logo_btn2, bg='#101E33')
logo_label_btn2.image =logo_btn2
logo_label_btn2.place(x=30, y=280)


text1 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\text1.png')
text1 = ImageTk.PhotoImage(text1)
text1_label = Label(image=text1)
text1_label.image = text1
text1_label.place(x=400, y=30)
text2 = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\text2.png')
text2 = ImageTk.PhotoImage(text2)
text2_label = Label(image=text2)
text2_label.image = text2
text2_label.place(x=400, y=420)

eminem_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\eminem.png')
eminem_photo = ImageTk.PhotoImage(eminem_photo)
eminem_label = Label(image=eminem_photo)
eminem_label.image = eminem_photo
eminem_label.place(x=400, y=100)
btn_eminem = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Eminem1.png')
btn_eminem = ImageTk.PhotoImage(btn_eminem)
btneminem_label = Label(image=btn_eminem)
btneminem_label.image = btn_eminem
Button(window, image=btn_eminem, highlightthickness=0, bd=0, command=eminem_new).place(x=470, y=350)

kanye_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Kanye.png')
kanye_photo = ImageTk.PhotoImage(kanye_photo)
kanye_label = Label(image=kanye_photo)
kanye_label.image = kanye_photo
kanye_label.place(x=730, y=100)
btn_kanye = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Kanye1.png')
btn_kanye = ImageTk.PhotoImage(btn_kanye)
btnkanye_label = Label(image=btn_kanye)
btnkanye_label.image = btn_kanye
Button(window, image=btn_kanye, highlightthickness=0, bd=0, command=kanye_new).place(x=770, y=350)

weeknd_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Weeknd.png')
weeknd_photo = ImageTk.PhotoImage(weeknd_photo)
weeknd_label = Label(image=weeknd_photo)
weeknd_label.image = weeknd_photo
weeknd_label.place(x=1060, y=100)
btn_weeknd = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Weeknd1.png')
btn_weeknd = ImageTk.PhotoImage(btn_weeknd)
btnweeknd_label = Label(image=btn_weeknd)
btnweeknd_label.image = btn_weeknd
Button(window, image=btn_weeknd, highlightthickness=0, bd=0,  command=weeknd_new).place(x=1090, y=350)

dimash_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\dimash.png')
dimash_photo = ImageTk.PhotoImage(dimash_photo)
dimash_label = Label(image=dimash_photo)
dimash_label.image = dimash_photo
dimash_label.place(x=400, y=490)
btn_dimash= Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Dimash1.png')
btn_dimash = ImageTk.PhotoImage(btn_dimash)
btndimash_label = Label(image=btn_dimash)
btndimash_label.image = btn_dimash
Button(window, image=btn_dimash, highlightthickness=0, bd=0, command=dimashh_new).place(x=420, y=740)

scryp_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Scryp.png')
scryp_photo = ImageTk.PhotoImage(scryp_photo)
scryp_label = Label(image=scryp_photo)
scryp_label.image = scryp_photo
scryp_label.place(x=730, y=490)
btn_scryp= Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Scryp1.png')
btn_scryp = ImageTk.PhotoImage(btn_scryp)
btnscryp_label = Label(image=btn_scryp)
btnscryp_label.image = btn_scryp
Button(window, image=btn_scryp, highlightthickness=0, bd=0, command=scyptonit_new).place(x=760, y=740)

nurtas_photo = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\Kairat.png')
nurtas_photo = ImageTk.PhotoImage(nurtas_photo)
nurtas_label = Label(image=nurtas_photo)
nurtas_label.image = nurtas_photo
nurtas_label.place(x=1060, y=490)
btn_nurtas = Image.open(r'C:\Users\bossa\Downloads\PhotoMusic\kairat1.png')
btn_nurtas = ImageTk.PhotoImage(btn_nurtas)
btnnurtas_label = Label(image=btn_nurtas)
btnnurtas_label.image = btn_nurtas
Button(window, image=btn_nurtas, highlightthickness=0, bd=0,command=kair_new).place(x=1070, y=740)




window.mainloop()
