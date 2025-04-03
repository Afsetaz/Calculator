import math
from tkinter import *
import tkinter.font as font

root = Tk()
root.title("calculator")
root["bg"] = "#d1d1d1"
root.geometry("310x400")

myfont = font.Font(size=15)

e = Entry(root, width=25, borderwidth=0)
e["font"] = myfont
e["bg"] = "#d1d1d1"
e.grid(row=0, columnspan=4, pady=20, padx=20)

def cetak(nilai):
    current = e.get()
    if nilai == ".":
        nilai == "."
    e.delete(0, END)
    e.insert(0, str(current) + str(nilai))

def tambah():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "penjumlahan"
    e.delete(0, END)

def kurang():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "pengurangan"
    e.delete(0, END)

def bagi():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "pembagian"
    e.delete(0, END)

def kali():
    global n_awal, mtk
    n_awal = float(e.get())
    mtk = "perkalian"
    e.delete(0, END)

def persen():
    try:
        angka = float(e.get())
        e.delete(0, END)
        e.insert(0, angka / 100)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "ERROR")

def hapus():
    e.delete(0, END)

def hapus_satu():
    current_text = e.get()
    e.delete(0, END)
    e.insert(0, current_text[:-1])

def koma():
    current = e.get()
    if "." not in current:
        e.insert(END, ".")

def akar():
    try:
        angka = float(e.get()) 
        if angka < 0:
            e.delete(0, END)
            e.insert(0, "ERROR") 
        else:
            e.delete(0, END)
            e.insert(0, str(math.sqrt(angka)))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "ERROR")

def samadengan():
    nomor_akhir = e.get()
    e.delete(0, END)
    if mtk == "penjumlahan":
        e.insert(0, n_awal + float(nomor_akhir))
    elif mtk == "pengurangan":
        e.insert(0, n_awal - float(nomor_akhir))
    elif mtk == "pembagian":
        try:
            e.insert(0, n_awal / float(nomor_akhir))
        except ZeroDivisionError:
            e.insert(0, "ERROR")
    elif mtk == "perkalian":
        e.insert(0, n_awal * float(nomor_akhir))

btn_numbers = []
for i in range(10):
    btn_numbers.append(Button(root, text=str(i), padx=30, bg="#3d3d3d", fg="white", pady=20, command=lambda i=i: cetak(i)))

btn_operations = [
    Button(root, text="+", padx=30, bg="#878787", fg="white", pady=20, command=tambah),
    Button(root, text="-", padx=30, bg="#878787", fg="white", pady=20, command=kurang),
    Button(root, text="/", padx=30, bg="#878787", fg="white", pady=20, command=bagi),
    Button(root, text="x", padx=30, bg="#878787", fg="white", pady=20, command=kali),
    Button(root, text="C", padx=30, bg="#878787", fg="white", pady=20, command=hapus),
    Button(root, text="=", padx=30, bg="skyblue", pady=20, command=samadengan),
    Button(root, text="<-", padx=27, bg="#878787", fg="white", pady=20, command=hapus_satu),
    Button(root, text="√", padx=30, bg="#878787", fg="white", pady=20, command=akar),
    Button(root, text=",", padx=30, bg="#878787", fg="white", pady=20, command=koma),
    Button(root, text="%", padx=30, bg="#878787", fg="white", pady=20, command=persen)
]

btn_numbers[7].grid(row=2, column=0, pady=2)
btn_numbers[8].grid(row=2, column=1, pady=2)
btn_numbers[9].grid(row=2, column=2, pady=2)
btn_numbers[4].grid(row=3, column=0, pady=2)
btn_numbers[5].grid(row=3, column=1, pady=2)
btn_numbers[6].grid(row=3, column=2, pady=2)
btn_numbers[1].grid(row=4, column=0, pady=2)
btn_numbers[2].grid(row=4, column=1, pady=2)
btn_numbers[3].grid(row=4, column=2, pady=2)
btn_numbers[0].grid(row=5, column=1, pady=2)

btn_operations[0].grid(row=3, column=3, pady=2) #tambah
btn_operations[1].grid(row=2, column=3, pady=2) #kurang
btn_operations[2].grid(row=1, column=1, pady=2) #bagi
btn_operations[3].grid(row=1, column=2, pady=2) #kali
btn_operations[4].grid(row=1, column=0, pady=2) #hapus
btn_operations[5].grid(row=4, column=3, pady=2) # samadengan
btn_operations[6].grid(row=1, column=3, pady=2) # hapus_satu
btn_operations[7].grid(row=5, column=0, pady=2) # akar
btn_operations[8].grid(row=5, column=2, pady=2) # koma
btn_operations[9].grid(row=5, column=3, pady=2) # persen

root.mainloop()
