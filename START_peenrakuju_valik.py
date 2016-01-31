from tkinter import *
from tkinter import font
from tkinter import messagebox

import nurgapeenar_def
import nelinurkpeenar_def
import ringpeenar_def

def vali_kuju():
    valik = v.get()
    if valik == 1:
        # Peale nupule vajutamist sulgub ka esimene nö. sissejuhatav aken.
        raam.destroy()
        nurgapeenar_def.nurgapeenar()     
    elif valik == 2:
        raam.destroy()
        nelinurkpeenar_def.nelinurkpeenar()
    elif valik == 3:
        raam.destroy()
        ringpeenar_def.ringpeenar()
    else:
        teade = 'Vali missuguse kujuga peenart soovid kujundama hakata!'
        messagebox.showinfo(message = teade)

raam = Tk()
raam.title('Kujunda oma peenar!')
raam.geometry('620x500')
raam.configure(background = 'snow')

# Teksti stiilid.
pealkiri_font = font.Font(family = 'Nirmala UI Semilight', size = 18, weight = 'bold')
alapealkiri_font = font.Font(family = 'Papyrus', size = 16, weight = 'bold')
tavakiri_font = font.Font(family = 'Papyrus', size = 14)

lilled = PhotoImage(file = 'siilikybar.gif')
Label(raam, image = lilled, width = 300, bg = 'snow').grid(row = 0, rowspan = 2, column = 0, padx = 20, pady = 20)

Label(raam, text = 'Tere tulemast peenrakujundamise programmi!',
      wraplength = 300, justify = LEFT, font = pealkiri_font,
      fg = 'magenta4', bg = 'snow').grid(row = 0, column = 1, pady = 20, sticky = W)
Label(raam, text = 'Ideed ja abi algajale aiahuvilisele oma lillepeenra kujundamisel.',
      wraplength = 250, justify = LEFT, font = tavakiri_font,
      bg = 'snow').grid(row = 1, column = 1, sticky = W)
Label(raam, text = '', bg = 'snow').grid(row = 2)
Label(raam, text = '    Alustuseks vali, missuguse kujuga peenart soovid teha:',
      font = tavakiri_font,
      bg = 'snow').grid(row = 3, columnspan = 2, sticky = W)

# Valikuvariantide kuvamine.
v = IntVar()
v.set(1)
peenrakujud = [('Nurgapeenar (kolmnurkne)', 1), ('Nelinurkne peenar', 2), ('Ümmargune peenar', 3)]
r = 4
for txt, val in peenrakujud:
    Radiobutton(raam, 
                text = txt, 
                variable = v,
                value = val,
                font = tavakiri_font,
                bg = 'snow').grid(row = r, column = 1, sticky = W)
    r += 1

# Nupp oma valiku kinnitamiseks ja akna sulgemiseks.
Button(raam, text = 'Jätka', command =  vali_kuju,
       font = alapealkiri_font, bg = 'magenta4', fg = 'snow').grid(row = r + 1, column = 1, sticky = W+E)

mainloop()
