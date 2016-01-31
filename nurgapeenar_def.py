from tkinter import *
from tkinter import font
from tkinter import messagebox
import time

import veebiotsing_def
import soovitused_def


def nurgapeenar():
    def ruudustik(laius, korgus):
        for i in range(0, korgus, 50):
            hor_id = tahvel.create_line(0, i, laius, i, fill = 'light grey', tags = 'ruudustik')
        for i in range(0, laius, 50):
            ver_id = tahvel.create_line(i, 0, i, korgus, fill = 'light grey', tags = 'ruudustik')

    def tyhjad_read(arv):
        for i in range(arv):
            Label(frame_alus, text = ' ', bg = 'snow').grid(row = i, column = 4)

    # Algandmete korjamine kasutaja poolt sisestatud väljadelt ja arvutamine.
    def algandmed():
        # Mõõtude paremaks tajumiseks joonistatakse peenrale ruudustik (sammuga 0,5m).
        ruudustik(laius, korgus)
        # Ruudu suuruse näitaja.
        moot1_id = tahvel.create_polygon(2, 51, 50, 51, 50, 100, 2, 100, fill = 'light grey', outline = 'black', tags = 'ruudustik')
        vaike_font = font.Font(family = 'Papyrus', weight = 'bold', size = 11)
        moot2_id = tahvel.create_text(25, 75, text = '0,5 m', font = vaike_font, tags = 'ruudustik')
        
        kylg1_kasutaja = kylg1_nr.get()
        kylg2_kasutaja = kylg2_nr.get()

        if kylg1_kasutaja == '' or kylg2_kasutaja == '':
            viga = 'Sisesta peenra mõõdud!'
            messagebox.showinfo(message = viga)
        elif kylg1_kasutaja != '' or kylg2_kasutaja != '':
            # Juhul kui kasutaja on sisestanud komakoha märkimiseks koma, siis asendatakse see punktiga.
            if kylg1_kasutaja.count(',') > 0 or kylg2_kasutaja.count(',') > 0:
                if kylg1_kasutaja.count(',') > 0:
                    kylg1_kasutaja = kylg1_kasutaja.replace(',', '.')
                    if kylg2_kasutaja.count(',') > 0:
                        kylg2_kasutaja = kylg2_kasutaja.replace(',', '.')
                else:
                    kylg2_kasutaja = kylg2_kasutaja.replace(',', '.')
            try:
                kylg1 = float(kylg1_kasutaja)
                kylg2 = float(kylg2_kasutaja)
                if kylg1 >= 1 and kylg1 <= 10 and kylg2 >= 1 and kylg2 <= 10:
                    # Joonistamiseks vajalikud punktide koordinaadid.
                    global x_algus
                    global y_algus
                    global x_kylg1
                    global y_kylg1
                    global x_kylg2
                    global y_kylg2
                    
                    x_algus = 50
                    y_algus = 50
                    x_kylg1 = 50 + kylg1*100
                    y_kylg1 = y_algus
                    x_kylg2 = x_algus
                    y_kylg2 = 50 + kylg2*100
                    valisaar_nurgapeenar(x_algus, y_algus, x_kylg1, y_kylg1, x_kylg2, y_kylg2)
                    
                    tekst_id = tahvel.create_text(x_algus, y_algus - 20,
                                                  text = 'Mis küljest Sa peenart vaatad? Kliki sellel küljel või külgedel ja vajuta nuppu "Näita peenraplaani".',
                                                  font = alapealkiri_font, fill = 'red', anchor = W, tags = 'peenar')

                    # Nupp peenraplaani joonistamiseks.
                    Button(frame_alus,
                           text = 'Näita peenraplaani',
                           command =  peenraplaan_nurgapeenar,
                           font = alapealkiri_font,
                           bg = 'magenta4', fg = 'snow').grid(row = 4, column = 3, padx = 10, pady = 10, sticky = W+E)

                    kujundussoovitused(kylg1,kylg2)
                else:
                    viga = 'Viga! Programmiga saab kujundada vaid peenart, mille küljepikkused jäävad vahemikku 1 - 10 meetrit.'
                    messagebox.showinfo(message = viga)
            except:
                viga = 'Viga! Sisestada saab vaid numbreid!'
                messagebox.showinfo(message = viga)

    # Alternatiiv - nupu asemel kasutatakse peenra joonistamiseks Enter-klahvi.
    # Algandmete korjamine kasutaja poolt sisestatud väljadelt ja arvutamine.
    def algandmed1(event):
        algandmed()
        
    # Peenra väliskülje loomine.
    def valisaar_nurgapeenar(x0, y0, x1, y1, x2, y2):
        joon1_id = tahvel.create_line(x0, y0, x1, y1, width=4, activefill = 'grey', tags = 'peenar')
        joon2_id = tahvel.create_line(x0, y0, x2, y2, width=4, activefill = 'grey', tags = 'peenar')
        joon3_id = tahvel.create_line(x1, y1, x2, y2, width=4, activefill = 'grey', tags = 'peenar')

        def joone_markimine1(event):
            joon1_id = tahvel.create_line(x0, y0, x1, y1, width=4, fill = 'red', tags = 'peenar')
            loenda_vaade_kylg1()
        
        def joone_markimine2(event):
            joon2_id = tahvel.create_line(x0, y0, x2, y2, width=4, fill = 'red', tags = 'peenar')
            loenda_vaade_kylg2()

        def joone_markimine3(event):
            joon3_id = tahvel.create_line(x1, y1, x2, y2, width=4, fill = 'red', tags = 'peenar')
            loenda_vaade_kylg3()

        # Abimuutujad, mis aitavad määratleda vaadeldavaid külgi (0 - külg ei ole vaadeldav, 1- külg on vaadeldav)
        global vaade_kylg1
        vaade_kylg1 = 0
        global vaade_kylg2
        vaade_kylg2 = 0
        global vaade_kylg3
        vaade_kylg3 = 0

        # Hiirekliki sidumine vaadete ära märkimisega.
        tahvel.tag_bind(joon1_id, '<1>', joone_markimine1)
        tahvel.tag_bind(joon2_id, '<1>', joone_markimine2)
        tahvel.tag_bind(joon3_id, '<1>', joone_markimine3)

    def loenda_vaade_kylg1():
        global vaade_kylg1
        vaade_kylg1 = 1

    def loenda_vaade_kylg2():
        global vaade_kylg2
        vaade_kylg2 = 1

    def loenda_vaade_kylg3():
        global vaade_kylg3
        vaade_kylg3 = 1

    def kujundussoovitused(kylg1, kylg2):
        # Kauguse väärtus
        kaugus_txt = v.get()
        if kaugus_txt == kaugused_lst[0]:
            kaugus = 1
        elif kaugus_txt == kaugused_lst[1]:
            kaugus = 2 
        elif kaugus_txt == kaugused_lst[2]:
            kaugus = 3 
        elif kaugus_txt == kaugused_lst[3]:
            kaugus = 4 
        else:
            kaugus = 5 
        
        # Programm arvutab peenra esikülje (diagonaali).
        diagonaal = (kylg1**2 + kylg2**2)**0.5
        
        # Sobivaimad peenra kõrgused.
        global korge_peenar
        if kaugus < 2:
            korge_peenar = 0.6
        elif kaugus < diagonaal:
            korge_peenar = kaugus 
        else:
            korge_peenar = diagonaal 

        keskmine_peenar = korge_peenar * 2/3
        madal_peenar = korge_peenar * 1/3
        pindala = (kylg1*kylg2) / 2

        # Soovitused istutusmustris kasutatava taimematerjali kohta.
        igihaljad = round(pindala*1/3, 1)
        suvehaljad = round(pindala * 2/3, 1)
        pysikud = round(suvehaljad * 2/3, 1)
        lehtpuud_poosad = round(suvehaljad - pysikud, 1)

        info = 'Peenra pindala on: ' + str(round(pindala, 1)) + ' m2.' +'\n' + \
            'Peenra esikülje pikkus on: ' + str(round(diagonaal, 1)) + ' m.' + '\n' + \
            'Sobivaimad peenra kõrgused on: ' + '\n' + \
              '- lopsakas ja kõrge peenar: ' + str(round(korge_peenar, 1)) + ' m' +'\n' + \
              '- keskmine peenar: ' + str(round(keskmine_peenar, 1)) + ' m' +'\n' + \
              '- madal peenar: ' + str(round(madal_peenar, 1)) + ' m'
        info1 = 'Soovitused taimede valikuks!'
        info2 = 'Igihaljaid puid ja põõsaid ' + str(igihaljad) + ' m2' + '\n' + \
              'Lehtpuid ja -põõsaid ' + str(lehtpuud_poosad) + ' m2' + '\n' + \
              'Püsililli ' + str(pysikud) + ' m2'

        tekst_id = tahvel_tekst.create_text(10, 20, text = info, font = tavakiri_font, anchor = N+W)
        if pindala > 1:
            tekst_id1 = tahvel_tekst.create_text(580, 80, text = info1, font = alapealkiri_font, fill = 'yellow green', justify = RIGHT, anchor = N+E)
            tekst_id2 = tahvel_tekst.create_text(580, 110, text = info2, font = tavakiri_font, justify = RIGHT, anchor = N+E)

    def peenraplaan_nurgapeenar():
        # Enne plaani joonistamist kustutatakse eelmises etapis joonistatud jooned.
        puhasta_tahvel()
        # Funktsioon, mis joonistab peenraplaani vastavalt vaadeldavale küljele.
        def nurgapeenra_pealtvaade(x0, y0, x1, y1, x2, y2, x3, y3, varv, taht, xA, peenra_korgus):
            # Rekursiooni lõpu määratlemine.
            if (x1 - x0)*3/5 < 50 or (y2 - y0)*3/5 < 50:
                return
            # Paremaks istutustsoonide eristamiseks kasutatakse värvi.
            rgb = "#%02x%02x%02x" % varv
            tahvel.create_polygon(x0, y0, x1, y1, x2, y2, x3, y3, fill = rgb, outline = 'black', tags = 'peenar')
            # Peenrajaotustsoonide eristamiseks lisaks värvile on kasutusel ka tähed, mis kuvatakse joonise kohale.
            taht_uus = taht + 1
            tsoonide_tahed.append(chr(taht_uus))
            tsoon_id = tahvel.create_text(x0 + 10, y0 + 15, text = chr(taht_uus), font = alapealkiri_font, anchor=W, tags = 'peenar')
            
            peenra_korgus = peenra_korgus*2/3
            # Taimesoovituste tegemiseks kogutakse soovitatavad kõrgused eraldi listi.
            peenra_korgused.append(round(peenra_korgus, 1))
            
            selgitus = chr(taht_uus) + ' - taimede kõrgus '  # Selleks, et väiksemad numbrid kuvataks esimesena, lisatakse numbrilised kõrgused hiljem.
            xA_uus = xA + 225
            tsoon_id_selgitus = tahvel.create_text(xA_uus, y_algus - 20, text = selgitus, font = tavakiri_font, anchor=W, tags = 'peenar')

            if vaade_kylg1 == vaade_kylg2 == vaade_kylg3:
                x0_uus = x0 + (x1)*1/5
                y0_uus = y0 + (y2)*1/5
                x1_uus = x1 - 2*(x1)*1/5
                y1_uus = y1 + (y2)*1/5
                x2_uus = x2 + (x1)*1/5
                y2_uus = y2 - 2*(y2)*1/5
            
            elif vaade_kylg1 == vaade_kylg3 == 1:
                x0_uus = x0
                y0_uus = y0 + (y2)*1/5
                x1_uus = x1 - 2*((x1-x0)/(y2-y0)*(y2)*1/5)
                y1_uus = y1 + (y2)*1/5
                x2_uus = x2
                y2_uus = y2 - (y2)*1/5   
            
            elif vaade_kylg2 == vaade_kylg3 == 1:
                x0_uus = x0 + (x1)*1/5
                y0_uus = y0
                x1_uus = x1 - (x1)*1/5
                y1_uus = y1
                x2_uus = x2 + (x1)*1/5
                y2_uus = y2 - 2*((y2-y0)/(x1-x0) * (x1)*1/5)
            
            elif vaade_kylg1 == vaade_kylg2 == 1:
                x0_uus = x0 + (x1)*1/5
                y0_uus = y0 + (y2)*1/5
                x1_uus = x1 - ((x1-x0)/(y2-y0)*(y2)*1/5)
                y1_uus = y1 + (y2)*1/5
                x2_uus = x2 + (x1)*1/5
                y2_uus = y2 - ((y2-y0)/(x1-x0) * (x1)*1/5)

            elif vaade_kylg3 == 1:
                x0_uus = x0
                y0_uus = y0
                x1_uus = x1 - (x1)*2/5
                y1_uus = y1
                x2_uus = x2
                y2_uus = y2 - (y2)*2/5
                # Antud vaate puhul tuleksid tsooni märgistavad tähed ühe koha peale.
                # Seetõttu tuleb eelnevalt kirjutatud tekst kustutada ning kirjutada see uuele positsioonile.
                tahvel.delete(tsoon_id)
                tsoon_id2 = tahvel.create_text(x1 - 20, y1 + 15, text = chr(taht_uus), font = alapealkiri_font, anchor=E, tags = 'peenar')
            
            elif vaade_kylg1 == 1:
                x0_uus = x0
                y0_uus = y0 + (y2)*1/5
                x1_uus = x1 - ((x1-x0)/(y2-y0)*(y2)*1/5)
                y1_uus = y1 + (y2)*1/5
                x2_uus = x2
                y2_uus = y2
                        
            elif vaade_kylg2 == 1:
                x0_uus = x0 + (x1)*1/5
                y0_uus = y0
                x1_uus = x1
                y1_uus = y1
                x2_uus = x2 + (x1)*1/5
                y2_uus = y2 - ((y2-y0)/(x1-x0) * (x1)*1/5)

            # Uue värvi loomine järgmise peenratsooni jaoks.
            r = varv[0]
            g = varv[1]
            b = varv[2]
            r_tume = round(r * 0.75)
            g_tume = round(g * 0.75)
            b_tume = round(b * 0.75)
            varv_uus = (r_tume, g_tume, b_tume)
            
            # Rekursioon järgmise (väiksema) tsooni loomiseks.
            nurgapeenra_pealtvaade(x0_uus, y0_uus, x1_uus, y1_uus, x2_uus, y2_uus, x2_uus, y2_uus, varv_uus, taht_uus, xA_uus, peenra_korgus)
            ruudustik(laius, korgus)
            
        # Järjendid rekursiooni käigus tekkivate andmete kogumiseks ja säilitamiseks.
        peenra_korgused = []
        tsoonide_tahed = []
        nurgapeenra_pealtvaade(x_algus, y_algus, x_kylg1, y_kylg1, x_kylg2, y_kylg2, x_kylg2, y_kylg2, (195, 253, 51), 64, x_algus - 250, korge_peenar)

        # Peenra kõrguste lisamine tahvli ülaääres olevate tsoonide tähtede juurde.
        peenra_korgused.reverse()
        x_nr = 185
        for e in peenra_korgused:
            nr = str(e) + ' m;'
            tsoon_id_selgitus2 = tahvel.create_text(x_nr, y_algus - 20, text = nr, font = tavakiri_font, anchor=W, tags = 'peenar')
            x_nr += 225

        # Sõltuvalt tekkinud info suurusest muudetakse keritava tekstikasti laiust ja kõrgust.
        tahvel.config(scrollregion = (0, 0, x_nr + 100, y_kylg2 + 100))
        # Selleks, et värvi "alt" oleks ka ruudustik näha, joonistatakse ruudustik uuesti värvitud peenraosade peale.
        ruudustik(x_nr + 100, round(y_kylg2) + 100)

        def otsi():
            # Funktsioon taimeinfo kogumiseks veebist. Kuna veebist andmete tõmbamine on ajamahukas, siis kogutakse andmed faili.
            # Juhul kui samal päeval on juba otsing teostatud, siis saadakse taimeinfo loodud failist.
            # Kui otsingut pole veel üldse tehtud või on seda tehtud eelnevatel päevadel, teostatakse andmete kogumine veebist uuesti.
            kuupäev = time.strftime("%d/%m/%Y")
            failinimi = 'PeenraprogrammiTaimedeAndmebaas.txt'
            try:
                f = open(failinimi)
                Irida = f.readline().strip()
                f.close()
                if Irida != kuupäev:
                    raise ValueError
            except:
                veebiandmed = veebiotsing_def.veebiotsing()
                f = open(failinimi, mode = 'w')
                f.write(kuupäev + '\n')
                for i in range(len(veebiandmed[0])):
                    andmerida = '{0};{1};{2}'.format(veebiandmed[0][i], veebiandmed[1][i], veebiandmed[2][i])
                    f.write(andmerida + '\n')
                f.close()
            # Soovituste aken ja taimesoovitused veebist.
            soovitused_def.taimesoovitused(failinimi, peenra_korgused, frame_alus, tsoonide_tahed)

        # Nupp veebiotsingu teostamiseks Hansaplanti koduleheküljel asuvate taimede seast.
        Button(frame_alus,
               text = 'Näita taimesoovitusi',
               command = otsi,
               font = alapealkiri_font,
               fg = 'snow', bg = 'magenta4',
               width = 23).grid(row=0, column=5, columnspan=2, padx = 10, pady = 10, sticky=W+E)
        
    # Joonistatud peenra kustutamine tahvlilt.
    def puhasta_tahvel():
        tahvel.delete('peenar')
        
    # Nupu "Alusta uuesti" tegevused.
    def puhasta():
        tahvel.delete('peenar')
        Button(frame_alus,
               text = 'Näita peenraplaani',
               command = teade_loo_peenar,
               font = alapealkiri_font,
               bg = 'light grey', fg = 'snow').grid(row=4, column=3, padx = 10, pady = 10, sticky=W+E)
        Button(frame_alus,
               text = 'Näita taimesoovitusi',
               command = teade_taimesoovitused,
               font = alapealkiri_font,
               fg = 'snow', bg = 'light grey',
               width = 23).grid(row=0, column=5, columnspan=2, padx = 10, pady = 10, sticky=W+E)
        tahvel_tekst.delete('all')  

    # Veateated.    
    def teade_loo_peenar():
        viga = 'Sisesta peenra mõõdud ja vajuta nupule "Loo peenar"!'
        messagebox.showinfo(message = viga)

    def teade_taimesoovitused():
        viga = 'Pole veel andmeid, mille järgi soovitusi anda.' + '\n' +\
               'Tee nii:' + '\n' +\
               '1. Sisesta peenra mõõdud.'+ '\n' +\
               '2. Vajuta nupule "Loo peenar".' + '\n' +\
               '3. Vajuta nupule "Näita peenraplaani".' + '\n' + '\n' +\
               'Ja siis proovi uuesti seda nuppu :)'
        messagebox.showinfo(message = viga)

    # Raami loomine.
    raam = Tk()
    raam.title('Sinu peenar')
    raam.geometry('620x500') 
    raam.configure(background = 'snow')

    # Kerimisribad suurele aknale. 
    tahvel_alus = Canvas(raam, background='snow', highlightbackground = 'snow', scrollregion = (0, 0, 1700, 900))
    frame_alus = Frame(tahvel_alus, background='snow', highlightbackground = 'snow')
    frame_alus.pack()
    tahvel_alus.create_window(0, 0, window = frame_alus, anchor='nw')
    vbar_alus = Scrollbar(tahvel_alus, orient = VERTICAL)
    vbar_alus.pack(side = RIGHT, fill = Y)
    vbar_alus.config(command = tahvel_alus.yview)
    hbar_alus = Scrollbar(tahvel_alus, orient = HORIZONTAL)
    hbar_alus.pack(side = BOTTOM, fill = X)
    hbar_alus.config(command = tahvel_alus.xview)
    tahvel_alus.config(xscrollcommand = hbar_alus.set, yscrollcommand = vbar_alus.set)
    tahvel_alus.pack(side = LEFT, expand = True, fill = BOTH)

    # Hilisema päisesse tuleva teksti alus.
    tahvel_tekst = Canvas(frame_alus, background = 'snow', highlightbackground = 'snow', width = 600, height = 200)
    tahvel_tekst.grid(row = 0, rowspan = 4, column = 2, columnspan = 2, sticky= N + E + S + W)

    # Tahvli loomine. Kerimisriba kasutamiseks luuakse see frame'ile. 
    frame = Frame(frame_alus, width = 1000, height = 500) 
    frame.grid(row = 5, rowspan = 25, column = 0, columnspan = 4, sticky= N + E + S + W)
    laius = 1500
    korgus = 1200
    tahvel = Canvas(frame, width = 1000, height = 550, background='snow', scrollregion = (0, 0, laius, korgus))

    # Tahvli kerimisribad
    vbar = Scrollbar(tahvel, orient = VERTICAL)
    vbar.pack(side = RIGHT, fill = Y)
    vbar.config(command = tahvel.yview)
    hbar = Scrollbar(tahvel, orient = HORIZONTAL)
    hbar.pack(side = BOTTOM, fill = X)
    hbar.config(command = tahvel.xview)
    tahvel.config(xscrollcommand = hbar.set, yscrollcommand = vbar.set)
    tahvel.pack(side = LEFT, expand = True, fill = BOTH)

    # Tahvlile vajaliku kõrguse andmiseks on raami paigutatud ka tühjad read.
    tyhjad_read(28)

    # Teksti stiilid.
    pealkiri_font = font.Font(family = 'Nirmala UI Semilight', size = 18, weight = 'bold')
    alapealkiri_font = font.Font(family = 'Papyrus', size = 16, weight = 'bold')
    tavakiri_font = font.Font(family = 'Papyrus', size = 14)

    # Tekstikastide nimetused (sildid).
    Label(frame_alus, text = 'Sisesta parempoolse külje pikkus (max 10 meetrit):',
          justify = RIGHT, font = tavakiri_font, bg = 'snow').grid(row=0, column=0, sticky=E)
    Label(frame_alus, text = 'Sisesta vasakpoolse külje pikkus (max 10 meetrit):',
          justify = RIGHT, font = tavakiri_font, bg = 'snow').grid(row=1, column=0, sticky=E)
    Label(frame_alus, text = 'Vali peenra kaugus kohast, kus seda kõige rohkem vaadatakse/nähakse:',
          wraplength = 400, justify = RIGHT, font = tavakiri_font, bg = 'snow').grid(row=2, rowspan = 2, column=0, sticky=E)

    # Tekstikastid andmete sisestamiseks.
    kylg1_nr = Entry(frame_alus)
    kylg2_nr = Entry(frame_alus)
    kylg1_nr.grid(row=0, column=1)
    kylg2_nr.grid(row=1, column=1)

    # Kauguse sisestamiseks on drop-down list.
    kaugused_lst = ['vähem kui 2 meetrit', '2-4 meetrit', '5-7 meetrit', '8-10 meetrit', 'rohkem kui 10 meetrit']
    v = StringVar()
    v.set(kaugused_lst[0])
    drop = OptionMenu(frame_alus, v, *kaugused_lst)
    drop.configure(background = 'white', highlightbackground = 'snow')
    drop.grid(row=3, column=1, padx=10, pady=10, sticky=W+E)
            
    # Peenra joonistamiseks nupu loomine.
    Button(frame_alus,
           text = 'Loo peenar',
           command = algandmed,
           font = alapealkiri_font,
           fg = 'snow', bg = 'magenta4').grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=W+E)
    # Alternatiivne peenra joonistamine vajutades nupule Enter.
    tahvel.bind_all("<Return>", algandmed1)

    # Joonistuse kustutamiseks nupu loomine.
    Button(frame_alus,
           text = 'Alusta uuesti',
           command = puhasta,
           font = alapealkiri_font,
           fg = 'snow', bg = 'magenta4').grid(row=4, column=2, padx=10, pady=10, sticky=W+E)

    raam.mainloop()
