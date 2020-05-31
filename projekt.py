ZNAKI_NA_MORSE = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': '    '
}

ZNAKI_NA_CEZAR = {
    'A': '0',
    'B': '1',
    'C': '2',
    'D': '3',
    'E': '4',
    'F': '5',
    'G': '6',
    'H': '7',
    'I': '8',
    'J': '9',
    'K': '10',
    'L': '11',
    'M': '12',
    'N': '13',
    'O': '14',
    'P': '15',
    'Q': '16',
    'R': '17',
    'S': '18',
    'T': '19',
    'U': '20',
    'V': '21',
    'W': '22',
    'X': '23',
    'Y': '24',
    'Z': '25'
}

MORSE_NA_ZNAKI = {value: key for key, value in ZNAKI_NA_MORSE.items()}
CEZAR_NA_ZNAKI = {value: key for key, value in ZNAKI_NA_CEZAR.items()}


def wczytaj_kod_z_pliku(nazwa_pliku):
    caly_plik = []
    with open(nazwa_pliku) as plik:
        for linia in plik.readlines():
            caly_plik.append(linia.strip())
    return caly_plik


def zamien_tekst_na_morse(linijka):
    zakodowana_linijka = ''
    for znak in linijka:
        zakodowana_linijka += ZNAKI_NA_MORSE[znak.upper()]
        if znak != ' ':
            zakodowana_linijka += ' '
    return zakodowana_linijka.strip()


def zamien_morsa_na_tekst(linijka):
    odkodowana_linijka = ''
    for znaki in linijka.split(' '):
        if znaki == '':
            odkodowana_linijka += ' '
        else:
            odkodowana_linijka += MORSE_NA_ZNAKI[znaki.upper()]
    return odkodowana_linijka


def zapisz_plik(nazwa_pliku, zawartosc):
    with open(nazwa_pliku, 'w+') as plik:
        for linia in zawartosc:
            plik.writelines(linia + '\n')


def wczytaj_tekst_i_zamien_na_morsa(nazwa_pliku_do_kodowania):
    caly_tekst = wczytaj_kod_z_pliku(nazwa_pliku_do_kodowania)
    zamieniony_tekst = []
    for linijka in caly_tekst:
        zamienione = zamien_tekst_na_morse(linijka)
        zamieniony_tekst.append(zamienione)
    return zamieniony_tekst


def zakoduj_morsem_dane_z_pliku(nazwa_pliku_do_kodowania, nazwa_pliku_zakodowanego):
    zakodowany_tekst = wczytaj_tekst_i_zamien_na_morsa(nazwa_pliku_do_kodowania)
    zapisz_plik(nazwa_pliku_zakodowanego, zakodowany_tekst)


def wczytaj_tekst_i_odkoduje_morsa(nazwa_pliku_do_odkodowania):
    caly_tekst = wczytaj_kod_z_pliku(nazwa_pliku_do_odkodowania)
    odkodowany_tekst = []
    for linijka in caly_tekst:
        odkodowane = zamien_morsa_na_tekst(linijka)
        odkodowany_tekst.append(odkodowane)
    return odkodowany_tekst


def odkoduj_morsem_dane_z_pliku(nazwa_pliku_do_odkodowania, nazwa_pliku_do_zapisu):
    odkodowane = wczytaj_tekst_i_odkoduje_morsa(nazwa_pliku_do_odkodowania)
    zapisz_plik(nazwa_pliku_do_zapisu, odkodowane)


def zamien_tekst_na_cezara(linijka):
    zakodowane = ''
    for znak in linijka:
        if znak.strip() != '':  # usuwam spacje bo nie ma w slowniku odpowiednika numerkowego
            numer_literki = int(ZNAKI_NA_CEZAR[znak.upper()])
            cezarowy_indeks = numer_literki + 3

            if cezarowy_indeks > 25:
                cezarowy_indeks = cezarowy_indeks - 26
            zakodowane += CEZAR_NA_ZNAKI[str(cezarowy_indeks)]
        else:
            zakodowane += ' '
    return zakodowane


def wczytaj_tekst_i_zakoduj_cezara(nazwa_pliku_do_zakodowania):
    caly_tekst = wczytaj_kod_z_pliku(nazwa_pliku_do_zakodowania)
    zakodowany_tekst = []
    for linijka in caly_tekst:
        zakodowane = zamien_tekst_na_cezara(linijka)
        zakodowany_tekst.append(zakodowane)
    return zakodowany_tekst


def zakoduj_cezarem_dane_z_pliku(nazwa_pliku_do_zakodowania, nazwa_pliku_do_zapisu):
    zakodowany_tekst = wczytaj_tekst_i_zakoduj_cezara(nazwa_pliku_do_zakodowania)
    zapisz_plik(nazwa_pliku_do_zapisu, zakodowany_tekst)


def zamien_cezara_na_tekst(linijka):
    odkodowane = ''
    for znak in linijka:
        if znak.strip() != '':  # usuwam spacje bo nie ma w slowniku odpowiednika numerkowego
            numer_literki = int(ZNAKI_NA_CEZAR[znak.upper()])
            cezarowy_indeks = numer_literki - 3
            if cezarowy_indeks < 0:
                cezarowy_indeks = cezarowy_indeks + 26
            odkodowane += CEZAR_NA_ZNAKI[str(cezarowy_indeks)]
        else:
            odkodowane += ' '
    return odkodowane


def wczytaj_tekst_i_odkoduje_cezarem(nazwa_pliku_do_odkodowania):
    caly_tekst = wczytaj_kod_z_pliku(nazwa_pliku_do_odkodowania)
    odkodowany_tekst = []
    for linijka in caly_tekst:
        odkodowane = zamien_cezara_na_tekst(linijka)
        odkodowany_tekst.append(odkodowane)
    return odkodowany_tekst


def odkoduj_cezarem_dane_z_pliku(nazwa_pliku_do_odkodowania, nazwa_pliku_do_zapisu):
    odkodowane = wczytaj_tekst_i_odkoduje_cezarem(nazwa_pliku_do_odkodowania)
    zapisz_plik(nazwa_pliku_do_zapisu, odkodowane)


def main():
    print('Witaj w moim programie')
    print('Co chcesz zrobic?')
    print('1. Zakodowac plik morsem')
    print('2. Odkodowan plik morsem')
    print('3. Zakodowac Cezarem')
    print('4. Odkodowac Cezarem')
    wybor = input()
    if wybor == '1':
        zakoduj_morsem_dane_z_pliku('pliczek.txt', 'zakodowany_mors.txt')
        print('Zrobione')
    elif wybor == '2':
        odkoduj_morsem_dane_z_pliku('zakodowany_mors.txt', 'odkodany_mors.txt')
        print('Zrobione')
    elif wybor == '3':
        zakoduj_cezarem_dane_z_pliku('pliczek.txt', 'zakodowane_cezar.txt')
        print('Zrobione')
    elif wybor == '4':
        odkoduj_cezarem_dane_z_pliku('zakodowane_cezar.txt', 'odkodowany_cezar.txt')
        print('Zrobione')

if __name__ == "__main__":
    main()
