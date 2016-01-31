from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter import messagebox

def taimesoovitused(failinimi, peenra_korgused, raam, tsoonide_tahed):
    def puhasta():
        tahvel2.delete('peenar')
        del salvestamiseks[:]

    def salvesta():
        if len(salvestamiseks) == 0:
            viga = 'Taimesoovituste aken on tühi! Vajuta nuppu "Näita taimesoovitusi" ja proovi uuesti!'
            messagebox.showinfo(message = viga)
        else:
            f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
            if f is None:  # asksaveasfile tagastab None kui kasutaja vajutab "cancel".
                return
            for e in salvestamiseks:
                if type(e) == list:
                    rida = '-' + e[0] + e[1] + '\n'
                    f.write(rida)
                elif e == 0:
                    rida = '\n'
                    f.write(rida)
                else:
                    f.write(e + '\n')
            f.close()
    
    # Veebist saadavate taimesoovituste jaoks tahvli loomine.
    frame2 = Frame(raam, width = 340, height = 700)
    frame2.grid(row = 1, rowspan = 27, column = 5, columnspan = 2, sticky= N + E + S + W)
    tahvel2 = Canvas(frame2, width = 340, height = 700, background='snow', scrollregion = (0, 0, 600, 5000))
    # Kerimisribad
    vbar2 = Scrollbar(tahvel2, orient = VERTICAL)
    vbar2.pack(side=RIGHT, fill=Y)
    vbar2.config(command = tahvel2.yview)
    hbar2 = Scrollbar(tahvel2, orient = HORIZONTAL)
    hbar2.pack(side=BOTTOM, fill=X)
    hbar2.config(command = tahvel2.xview)
    tahvel2.config(xscrollcommand = hbar2.set, yscrollcommand = vbar2.set)
    tahvel2.pack(side=LEFT, expand=True, fill=BOTH)

    # Teksti stiilid.
    pealkiri_font = font.Font(family = 'Nirmala UI Semilight', size = 18, weight = 'bold')
    alapealkiri_font = font.Font(family = 'Papyrus', size = 16, weight = 'bold')
    tavakiri_font = font.Font(family = 'Papyrus', size = 14)
    vaike_font = font.Font(family = 'Papyrus', size = 11)

    f = open(failinimi) 
    read = f.readlines() 
    f.close() 
    taimenimed = []
    korgused = []
    keskmised_korgused = []
    liik = []
    
    for i in range(1, len(read)):  
        i0 = read[i].index(';')
        taimenimed.append(read[i][2:i0-5]) 
        liik.append(read[i][i0-2:i0-1])
        rida = read[i].strip().split(';') 
        korgused.append(rida[1]) 
        keskmised_korgused.append(rida[2]) 
    
    salvestamiseks = []
    y_kaugus = 5
    tahe_i = 0
    
    for e in peenra_korgused:
        y_kaugus += 27
        tekst = tsoonide_tahed[tahe_i] + ' taimed (' + str(peenra_korgused[tahe_i]) + ' m):'
        tahvel2.create_text(5, y_kaugus, text = tekst, font = alapealkiri_font, anchor = W, tags = 'peenar')
        salvestamiseks.append(tekst)
        
        tahe_i += 1

        i2 = 0
        loendur = 0
        liigi_loendur = 0
        for i in keskmised_korgused:
            i_arv = float(i)
            if i_arv >= (e - 0.05) and i_arv <= (e + 0.05):
                if liik[i2] == '1' and liigi_loendur < 1:
                    y_kaugus += 22
                    liiginimi = 'Igihaljad puud ja põõsad'
                    tahvel2.create_text(5, y_kaugus, text = liiginimi, font = tavakiri_font, fill = 'magenta4', anchor = W, tags = 'peenar')
                    salvestamiseks.append(liiginimi)
                    liigi_loendur += 1
                elif liik[i2] == '2' and liigi_loendur < 2:
                    y_kaugus += 22
                    liiginimi = 'Lehtpuud ja -põõsad'
                    tahvel2.create_text(5, y_kaugus, text = liiginimi, font = tavakiri_font, fill = 'magenta4', anchor = W, tags = 'peenar')
                    salvestamiseks.append(liiginimi)
                    if liigi_loendur == 0:
                        liigi_loendur += 2
                    else:
                        liigi_loendur += 1
                elif liik[i2] == '3' and liigi_loendur < 3:
                    y_kaugus += 22
                    liiginimi = 'Püsililled'
                    tahvel2.create_text(5, y_kaugus, text = liiginimi, font = tavakiri_font, fill = 'magenta4', anchor = W, tags = 'peenar')
                    salvestamiseks.append(liiginimi)
                    liigi_loendur += 3
                else:
                    pass

                nimi = taimenimed[i2]
                taimekorgus = korgused[i2]
                taimekorguse_kirje = '  (' + taimekorgus + ' m)'
                y_kaugus += 22
                tahvel2.create_text(5, y_kaugus, text = '* '+ nimi + taimekorguse_kirje, font = tavakiri_font, anchor = W, tags = 'peenar')
                salvestamiseks.append([nimi, taimekorguse_kirje])
                
                i2 += 1
                loendur += 1
                
            else:
                i2 +=1
        if loendur == 0:
                y_kaugus += 22
                teade = '-- Sobiva kõrgusega taimi hetkel pole --'
                tahvel2.create_text(5, y_kaugus, text = teade, font = tavakiri_font, anchor = W, tags = 'peenar')
                salvestamiseks.append(teade)
        salvestamiseks.append(0)

    # Veebiallika kuvamine.
    y_kaugus += 35
    allikas = 'Taimeinfo allikas: www.hansaplant.ee'
    tahvel2.create_text(5, y_kaugus, text = allikas, font = tavakiri_font, anchor = W, tags = 'peenar')
    salvestamiseks.append(allikas)

    # Sõltuvalt taimenimekira pikkusest muudetakse keritava tekstikasti kõrgust.
    tahvel2.config(scrollregion = (0, 0, 600, y_kaugus + 100))

    # Nimekirja kustutamiseks nupu loomine.
    Button(raam,
           text = 'Tühjenda nimekiri',
           command = puhasta,
           font = tavakiri_font,
           bg = 'yellow green').grid(row=28, column=5, pady=1, sticky=W+E)
    # Nimekirja salvestamiseks nupu loomine.
    Button(raam,
           text = 'Salvesta nimekiri',
           command = salvesta,
           font = tavakiri_font,
           bg = 'magenta4', fg = 'snow').grid(row=28, column=6, pady=1, sticky=W+E)
  
