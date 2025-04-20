import math
from tkinter import *
import tkinter.font as font

root = Tk()
root.title("Calculator")
root["bg"] = "#d1d1d1"
root.geometry("305x380")  # Ukuran tetap
root.resizable(False, False)  # Ukuran tidak bisa diubah-ubah

myfont = font.Font(size=15)

# Menampilkan tombol history kecil di atas kanan
frame_top = Frame(root, bg="#d1d1d1")
frame_top.grid(row=0, column=0, columnspan=4, padx=10, pady=(10, 5), sticky="ew")

e = Entry(frame_top, width=22, borderwidth=0, font=myfont, bg="#d1d1d1")
e.grid(row=0, column=0, padx=(0, 5))

history_button = Button(frame_top, text="📜", width=3, height=1, bg="#ffa500", fg="white", command=lambda: toggle_history())
history_button.grid(row=0, column=1)

# Riwayat/History
history_data = []
history_visible = False
history_text = Text(root, height=7, width=35, state=DISABLED, bg="white")

def toggle_history():
    global history_visible
    if history_visible:
        history_text.grid_forget()
        root.geometry("305x380")  # Ukuran layout kembali normal ketika history ditutup
        history_visible = False
    else:
        history_text.grid(row=7, column=0, columnspan=4, pady=5)
        root.geometry("305x510")  # Ukuran layout akan memrbesar ketika history dibuka
        history_visible = True


def update_history(ekspresi, hasil):
    history_data.append(f"{ekspresi} = {hasil}")
    history_text.config(state=NORMAL)
    history_text.delete("1.0", END)
    for item in history_data[-10:]:
        history_text.insert(END, item + "\n")
    history_text.config(state=DISABLED)

def cetak(nilai):
    current = e.get()
    if nilai == "." and "." in current:
        return
    elif nilai == "0" and current == "0":
        return
    e.insert(END, nilai)

def operasi(simbol):
    current = e.get()
    if current and current[-1] in "+-x/":
        return
    e.insert(END, simbol)

def persen():
    try:
        angka = float(e.get())
        hasil = angka * 0.01
        update_history(f"{angka}%", hasil)
        e.delete(0, END)
        e.insert(0, hasil)
    except ValueError:
        e.delete(0, END)
        e.insert(0, "ERROR")

def hapus():
    e.delete(0, END)

def hapus_satu():
    current_text = e.get()
    if len(current_text) > 0:
        e.delete(len(current_text)-1, END)

def koma():
    current = e.get()
    last_number = ""
    for char in reversed(current):
        if char in "+-x/":
            break
        last_number = char + last_number
    if "." not in last_number:
        e.insert(END, ".")

def akar():
    e.insert(END, "√")

def samadengan():
    try:
        ekspresi = e.get()
        ekspresi_asli = ekspresi
        ekspresi = ekspresi.replace("x", "*")
        while "√" in ekspresi:
            idx = ekspresi.index("√")
            kiri = ""
            i = idx - 1
            while i >= 0 and (ekspresi[i].isdigit() or ekspresi[i] == "."):
                kiri = ekspresi[i] + kiri
                i -= 1
            kanan = ""
            j = idx + 1
            while j < len(ekspresi) and (ekspresi[j].isdigit() or ekspresi[j] == "."):
                kanan += ekspresi[j]
                j += 1
            if kanan == "":
                raise ValueError("Akar tanpa angka")
            sqrt_expr = f"math.sqrt({kanan})"
            if kiri != "":
                ekspresi = ekspresi[:i+1] + kiri + "*" + sqrt_expr + ekspresi[j:]
            else:
                ekspresi = ekspresi[:idx] + sqrt_expr + ekspresi[j:]
        hasil = eval(ekspresi, {"math": math})
        e.delete(0, END)
        e.insert(0, hasil)
        update_history(ekspresi_asli, hasil)
    except Exception:
        e.delete(0, END)
        e.insert(0, "ERROR")

# Tombol angka
btn_numbers = [Button(root, text=str(i), padx=30, bg="#3d3d3d", fg="white", pady=20, command=lambda i=i: cetak(i)) for i in range(10)]

# Tombol operasi
btn_operations = [
    Button(root, text="+", padx=30, bg="#878787", fg="white", pady=20, command=lambda: operasi("+")),
    Button(root, text="-", padx=30, bg="#878787", fg="white", pady=20, command=lambda: operasi("-")),
    Button(root, text="/", padx=30, bg="#878787", fg="white", pady=20, command=lambda: operasi("/")),
    Button(root, text="x", padx=30, bg="#878787", fg="white", pady=20, command=lambda: operasi("x")),
    Button(root, text="C", padx=30, bg="#878787", fg="white", pady=20, command=hapus),
    Button(root, text="=", padx=30, bg="skyblue", pady=20, command=samadengan),
    Button(root, text="<-", padx=27, bg="#878787", fg="white", pady=20, command=hapus_satu),
    Button(root, text="√", padx=30, bg="#878787", fg="white", pady=20, command=akar),
    Button(root, text=",", padx=30, bg="#878787", fg="white", pady=20, command=koma),
    Button(root, text="%", padx=30, bg="#878787", fg="white", pady=20, command=persen),
]

# Grid angka
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

# Grid operasi
btn_operations[0].grid(row=3, column=3, pady=2) # tambah
btn_operations[1].grid(row=2, column=3, pady=2) # kurang
btn_operations[2].grid(row=1, column=1, pady=2) # bagi
btn_operations[3].grid(row=1, column=2, pady=2) # kali
btn_operations[4].grid(row=1, column=0, pady=2) # hapus
btn_operations[5].grid(row=4, column=3, pady=2) # samadengan
btn_operations[6].grid(row=1, column=3, pady=2) # hapus_satu
btn_operations[7].grid(row=5, column=0, pady=2) # akar
btn_operations[8].grid(row=5, column=2, pady=2) # koma
btn_operations[9].grid(row=5, column=3, pady=2) # persen

root.mainloop()
