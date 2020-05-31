import projekt


def test_zamiany_na_morsa():
    slowa = ['ala ma kota', 'mama mnie bardzo lubi']
    odpowiedzi = ['.- .-.. .-     -- .-     -.- --- - .-',
                  '-- .- -- .-     -- -. .. .     -... .- .-. -.. --.. ---     .-.. ..- -... ..']
    for ind, slowo in enumerate(slowa):
        zakodowane = projekt.zamien_tekst_na_morse(slowo)
        assert zakodowane == odpowiedzi[ind]


def test_odkodowania_morsa():
    slowo = '.... --- .--.'
    odpowiedz = 'hop'
    odkodowane = projekt.zamien_morsa_na_tekst(slowo)

    assert odkodowane.lower() == odpowiedz


def test_kodowanie_cezarem():
    slowo = 'VENI'
    odpowiedz = 'YHQL'
    zakodowane = projekt.zamien_tekst_na_cezara(slowo)
    assert odpowiedz == zakodowane


def test_odkodowanie_cezarem():
    slowo = 'YHQL'
    odpowiedz = 'VENI'
    odkodowane = projekt.zamien_cezara_na_tekst(slowo)
    assert odpowiedz == odkodowane


test_zamiany_na_morsa()
test_odkodowania_morsa()
test_kodowanie_cezarem()
test_odkodowanie_cezarem()
