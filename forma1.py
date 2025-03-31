"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""
versenyzok = []
legtobb_gyozelem = 0
legeredmenyesebb_versenyzo = None
legtobb_futam = 0
legtobb_futamot_teljesitett_versenyzo = None
osszes_futam = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        csapat = adatok[1]
        gyozelmek_szama = int(adatok[2])
        futamok_szama = int(adatok[3])
        osszes_futam.append(futamok_szama)
        versenyzok.append(adatok)
        if gyozelmek_szama > legtobb_gyozelem:
            legtobb_gyozelem = gyozelmek_szama
            legeredmenyesebb_versenyzo = nev
        if futamok_szama > legtobb_futam:
            legtobb_futam = futamok_szama
            legtobb_futamot_teljesitett_versenyzo = nev

atlagos_futamszam = sum(osszes_futam) / len(osszes_futam)

with open('kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as celfajl:

    celfajl.write(f"A beolvasott fájlban összesen {len(versenyzok)} versenyző szerepel.\n")
    celfajl.write(f"A legtöbb futamot nyert versenyző: {legeredmenyesebb_versenyzo}\n")
    celfajl.write(f"A legtöbb futamot teljesített versenyző: {legtobb_futamot_teljesitett_versenyzo}\n")
    celfajl.write(f"Az átlagos futamszám: {atlagos_futamszam:.2f}")