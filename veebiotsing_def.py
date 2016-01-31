from urllib.request import urlopen
from tkinter import messagebox

def veebiotsing():

    def veebiparing(url, liik):
        vastus = urlopen(url)
        baidid = vastus.read()
        tekst = baidid.decode().split('<td valign="top"><h5>')
        # Esimene listi element on ebaoluline osa veebi päises, mis eemaldatakse.
        del tekst[0]
        
        for rida in tekst:
            osad = rida.split('>')
            # Kuna mõningatel juhtudel on esitatud cm-tes ka kõrgus, siis on lisatud kontroll, et antud numbri ees oleks märgitud "height".
            i = 0
            for e in osad:
                if e[0].isnumeric() and ('m' in e) and ('height' in osad[i-3]):
                    if 'cm' in e:
                        I = e.index('c')
                        nr = e[:I]
                        if '-' in nr:
                            II = nr.index('-')
                            nr1 = int(nr[:II])/100
                            nr2 = int(nr[II+1:])/100
                            keskmine = (nr1 + nr2) / 2
                            keskmised_korgused.append(round(keskmine, 2))
                            # Kuna veebilehel on vahemike vormistus ebaühtlane, siis korrigeeritakse hilisemaks programmis kuvamiseks ka seda.
                            korgused.append(str(nr1) + '-' + str(nr2))

                        else:
                            keskmised_korgused.append(int(nr)/100)
                            nr = nr.strip()
                            korgused.append(int(nr)/100)
                         
                        # Juhul kui sobiv taimekõrgus on olemas, siis võetakse veebist ka taime nimi.
                        nimi = osad[1][:-3]
                        taimenimed.append((nimi, liik))
                    else:
                        I = e.index('m')
                        nr = e[:I].strip()
                        if '(' in nr:
                            i1 = nr.index('(')
                            nr = nr[:i1]

                        if ',' in nr:
                            nr = nr.replace(',', '.')
                            if ',' in nr:
                                nr = nr.replace(',', '.')
                                
                        if '-' in nr:
                            II = nr.index('-')
                            nr1 = float(nr[:II])
                            nr2 = float(nr[II+1:])
                            keskmine = (nr1 + nr2) / 2
                            keskmised_korgused.append(round(keskmine, 2))
                            # Kuna veebilehel on vahemike vormistus ebaühtlane, siis korrigeeritakse hilisemaks programmis kuvamiseks ka seda.
                            korgused.append(str(nr1) + '-' + str(nr2))
                        else:
                            keskmised_korgused.append(float(nr))
                            korgused.append(nr.strip())

                        # Juhul kui sobiv taimekõrgus on olemas, siis võetakse veebist ka taime nimi.
                        nimi = osad[1][:-3]
                        taimenimed.append((nimi, liik))
                i += 1

        vastus.close()

    urlid_okaspuud = [
        'http://hansaplant.ee/?op=body&id=130&cgid=&b=0#catalog',
        'http://hansaplant.ee/?op=body&id=130&b=24#catalog',
        'http://hansaplant.ee/?op=body&id=130&b=48#catalog',
        'http://hansaplant.ee/?op=body&id=130&b=72#catalog',
        'http://hansaplant.ee/?op=body&id=130&b=96#catalog',
        'http://hansaplant.ee/?op=body&id=130&b=120#catalog',
        'http://hansaplant.ee/?op=body&id=130&b=144#catalog',
        'http://hansaplant.ee/?op=body&id=130&b=168#catalog'
        ]

    urlid_lehtpuud = [
        'http://hansaplant.ee/?op=body&id=59&b=0#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=24#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=48#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=72#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=96#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=120#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=144#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=168#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=192#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=216#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=240#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=264#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=288#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=312#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=336#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=360#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=384#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=408#catalog',
        'http://hansaplant.ee/?op=body&id=59&b=432#catalog',
        'http://www.hansaplant.ee/?op=body&id=127', # Roosid
        'http://www.hansaplant.ee/?op=body&id=127&b=24#catalog', # Roosid
        'http://www.hansaplant.ee/?op=body&id=127&b=48#catalog' # Roosid
        ]

    urlid_pysikud = [
        'http://www.hansaplant.ee/?op=body&id=129&cgid=&b=0#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=24#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=48#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=72#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=96#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=120#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=144#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=168#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=192#catalog',
        'http://www.hansaplant.ee/?op=body&id=129&b=216#catalog',
        ]
    
    taimenimed = []
    korgused = []
    keskmised_korgused = []

    for i in range(len(urlid_okaspuud)):
        try:
            veebiparing(urlid_okaspuud[i], 1)
        except:
            print('Lehekülje "' + urlid_okaspuud[i] + '" avamine ei õnnestunud.')
            continue

    for i in range(len(urlid_lehtpuud)):
        try:
            veebiparing(urlid_lehtpuud[i], 2)
        except:
            print('Lehekülje "' + urlid_lehtpuud[i] + '" avamine ei õnnestunud.')
            continue

    for i in range(len(urlid_pysikud)):
        try:
            veebiparing(urlid_pysikud[i], 3)
        except:
            print('Lehekülje "' + urlid_pysikud[i] + '" avamine ei õnnestunud.')
            continue

    return [taimenimed, korgused, keskmised_korgused]

