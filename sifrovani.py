import random
import tkinter as tk
from tkinter import filedialog, messagebox

abeceda = ["a", "á", "b", "c", "č", "d", "ď", "e", "ě", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "n", "ň", "o", "ó", "p", "q", "r", "ř", "s", "š", "t", "ť", "u", "ú", "ů", "v", "w", "x", "y", "ý", "z", "ž", "A", "Á", "B", "C", "Č", "D", "Ď", "E", "Ě", "É", "F", "G", "H", "I", "Í", "J", "K", "L", "M", "N", "Ň", "O", "Ó", "P", "Q", "R", "Ř", "S", "Š", "T", "Ť", "U", "Ú", "Ů", "V", "W", "X", "Y", "Ý", "Z", "Ž" , " ", ".", ",", "!", "?", "-", "_", ":", ";", "'", '"', "(", ")", "[", "]", "{", "}", "@", "#", "$", "%", "^", "&", "*", "+", "=", "<", ">", "/","\\","|","~","`", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
abec = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def genklic():
    klic = ""
    i = 0
    while i < 15:
        klic += random.choice(abec)
        i += 1
    return klic

def cteni(cesta):
    try:
        with open(cesta, 'r', encoding='utf-8') as soubor:
            obsah = soubor.read()
        return obsah
    except Exception as e:
        print(f"nastala chyba: {e}")
        return None

def zapsat(cesta, data):
    try:
        with open(cesta, 'w', encoding='utf-8') as soubor:
            soubor.write(data)
        print("operace dokoncena")
    except Exception as e:
        print(f"Došlo k chybě při zápisu: {e}")

def sifrovani(text, klic):
    delka = len(text)
    delkaklic = len(klic)
    poradi = 0
    output = ""
    i = 0
    while i < delka:
        x = 0
        while x < delkaklic and poradi < delka:
            obsah_cislo = ord(text[poradi])
            klic_cislo = ord(klic[x])
            vysledek = obsah_cislo + klic_cislo
            output += chr(vysledek)
            x += 1
            poradi +=1
        i += delkaklic
    return output

def desifrovani(text, klic):
    delka = len(text)
    delkaklic = len(klic)
    poradi = 0
    output = ""
    i = 0
    while i < delka:
        x = 0
        while x < delkaklic and poradi < delka:
            obsah_cislo = ord(text[poradi])
            klic_cislo = ord(klic[x])
            vysledek = obsah_cislo - klic_cislo
            output += chr(vysledek)
            x += 1
            poradi +=1
        i += delkaklic
    return output


def akce_sifrovat():
    klic_z_okna = vstup_klic.get()
    if not klic_z_okna:
        messagebox.showwarning("Varování", "Nejprve zadej nebo vygeneruj klíč!")
        return
        
    cesta = filedialog.askopenfilename(title="Vyber soubor k šifrování", filetypes=[("Textové soubory", "*.txt")])
    if cesta:
        obsah = cteni(cesta)
        if obsah is not None:
            vysledek = sifrovani(list(obsah), list(klic_z_okna))
            zapsat(cesta, vysledek)
            messagebox.showinfo("Úspěch", "Soubor byl zašifrován!")

def akce_desifrovat():
    klic_z_okna = vstup_klic.get()
    if not klic_z_okna:
        messagebox.showwarning("Varování", "Pro dešifrování musíš zadat klíč!")
        return
        
    cesta = filedialog.askopenfilename(title="Vyber soubor k dešifrování", filetypes=[("Textové soubory", "*.txt")])
    if cesta:
        obsah = cteni(cesta)
        if obsah is not None:
            vysledek = desifrovani(list(obsah), list(klic_z_okna))
            zapsat(cesta, vysledek)
            messagebox.showinfo("Úspěch", "Soubor byl dešifrován!")

def tlacitko_genklic():
    novy_klic = genklic()
    vysledny_text = "".join(novy_klic)
    print(vysledny_text)
    vstup_klic.delete(0, tk.END)
    vstup_klic.insert(0, novy_klic)

root = tk.Tk()
root.title("Šifrovací program")
root.geometry("700x500")
tk.Label(root, text="Šifrovací klíč:").pack(pady=5)
vstup_klic = tk.Entry(root, width=30)
vstup_klic.pack(pady=2)
tk.Button(root, text="Vygenerovat náhodný klíč", command=tlacitko_genklic).pack(pady=5)
tk.Button(root, text="Vybrat soubor a ZAŠIFROVAT", bg="red", fg="white", command=akce_sifrovat).pack(pady=5)
tk.Button(root, text="Vybrat soubor a DEŠIFROVAT", bg="green", fg="white", command=akce_desifrovat).pack(pady=5)

root.mainloop()