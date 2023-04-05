from PIL import Image


def ukryj_dane_w_obrazie(obraz, dane):
    binarne_dane = ''.join(format(ord(i), '08b') for i in dane)
    piksele = obraz.load()
    index_danych = 0

    for row in range(obraz.size[0]):
        for col in range(obraz.size[1]):
            piksel = piksele[row, col]
            nowy_piksel = []

            for i in range(3):
                if index_danych < len(binarne_dane):
                    nowy_bit = int(binarne_dane[index_danych])
                    nowy_piksel.append(piksel[i] & ~1 | nowy_bit)
                    index_danych += 1
                else:
                    nowy_piksel.append(piksel[i])

            piksele[row, col] = tuple(nowy_piksel)

    return obraz


def odczytaj_dane_z_obrazu(obraz, dlugosc_danych):
    piksele = obraz.load()
    binarne_dane = []

    for row in range(obraz.size[0]):
        for col in range(obraz.size[1]):
            for i in range(3):
                binarne_dane.append(str(piksele[row, col][i] & 1))

    odczytane_dane = ''.join(chr(int(''.join(binarne_dane[i:i + 8]), 2)) for i in range(0, len(binarne_dane), 8))

    return odczytane_dane[:dlugosc_danych]


def main():
    obraz = Image.open("obrazek.png")
    dane = "Tajna"
    obraz_z_danymi = ukryj_dane_w_obrazie(obraz, dane)
    obraz_z_danymi.save("obraz_wyjsciowy.png")

    odczytane_dane = odczytaj_dane_z_obrazu(Image.open("obraz_wyjsciowy.png"), len(dane))
    print("Odczytane dane:", odczytane_dane)


if __name__ == "__main__":
    main()
