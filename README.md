# Restavracije v Ljubljani

Seminarska naloga pri predmetu Podatkovne baze 1.

## Namen projekta

Namen projekta je izdelava podatkovne baze restavracij v Ljubljani in
aplikacije, ki uporabniku omogoča pregledovanje restavracij, njihovih
menijev in jedi.

Pri posamezni jedi so shranjeni tudi podatki o sestavinah, alergenih
in tipu kuhinje.

## ER diagram

Spodnji diagram prikazuje strukturo podatkovne baze in povezave med tabelami.

![ER diagram](diagram.png)

## Funkcionalnosti

Projekt omogoča:

- pregled restavracij v Ljubljani,
- pregled jedi posamezne restavracije,
- pregled sestavin posamezne jedi,
- pregled alergenov posamezne jedi,
- iskanje restavracij glede na predel Ljubljane,
- iskanje restavracij glede na tip kuhinje.

## Podatkovna baza

Podatkovna baza je izdelana v SQLite.

Glavne tabele so:

- `Restavracija`
- `Meni`
- `Jed`
- `Tip_Kuhinje`
- `Sestavina`
- `Alergen`
- `Jed_Sestavina`
- `Jed_Alergen`

Tabeli `Jed_Sestavina` in `Jed_Alergen` predstavljata povezovalni
tabeli za relaciji mnogo-proti-mnogo.

Restavracije vsebujejo tudi podatek o predelu Ljubljane, kar omogoča
iskanje restavracij s pomočjo zemljevida.

## Tekstovni vmesnik

Program `tekstovni_vmesnik.py` omogoča osnovno delo z bazo preko
terminala.

Uporabnik lahko:

- izpiše vse restavracije,
- prikaže jedi izbrane restavracije,
- prikaže sestavine in alergene izbrane jedi.

## Spletni vmesnik

Program `spletni_vmesnik.py` uporablja knjižnico Bottle.

Spletni vmesnik omogoča izbiro restavracij glede na predel Ljubljane
s pomočjo interaktivnega SVG zemljevida.

Uporabnik lahko restavracije išče tudi glede na tip kuhinje.

Po izbiri restavracije lahko pregleda njene jedi, pri posamezni jedi
pa sestavine in alergene.

## Struktura projekta

- `RestavracijeVLjubljani.db` - podatkovna baza SQLite
- `model.py` - povezava s podatkovno bazo in SQL poizvedbe
- `tekstovni_vmesnik.py` - tekstovni uporabniški vmesnik
- `spletni_vmesnik.py` - spletni uporabniški vmesnik
- `static/ljubljana.svg` - interaktivni zemljevid Ljubljane

## Zagon programa

### 1. Prenos projekta

Prenesi oziroma kloniraj celoten repozitorij. Pomembno je, da struktura
datotek ostane nespremenjena:

    Restavracije-v-Ljubljani/
    │
    ├── RestavracijeVLjubljani.db
    ├── model.py
    ├── tekstovni_vmesnik.py
    ├── spletni_vmesnik.py
    │
    └── static/
        └── ljubljana.svg

Datoteke `model.py`, `tekstovni_vmesnik.py`, `spletni_vmesnik.py` in
`RestavracijeVLjubljani.db` morajo biti shranjene v isti mapi.

Datoteka `ljubljana.svg` mora ostati v podmapi `static`, saj jo spletni
vmesnik od tam naloži za prikaz interaktivnega zemljevida Ljubljane.


### 2. Namestitev knjižnice Bottle

Za delovanje spletnega vmesnika je potrebna knjižnica Bottle.

V ukazni vrstici oziroma terminalu zaženi:

    pip install bottle

Knjižnica `sqlite3`, ki jo program uporablja za delo s podatkovno bazo,
je že vključena v Python in je ni treba dodatno nameščati.


### 3. Tekstovni vmesnik

Za uporabo tekstovnega vmesnika odpri terminal v mapi projekta in zaženi:

    python tekstovni_vmesnik.py

Program se bo zagnal neposredno v terminalu in ponudil možnosti za
pregled restavracij, jedi, sestavin in alergenov.

Za izhod iz tekstovnega vmesnika izberi možnost `0`.


### 4. Spletni vmesnik

Tekstovnega vmesnika ni treba zagnati pred spletnim vmesnikom.
Programa sta med seboj neodvisna in oba uporabljata isto podatkovno bazo.

Za zagon spletnega vmesnika v terminalu v mapi projekta zaženi:

    python spletni_vmesnik.py

Po zagonu se zažene lokalni Bottle strežnik.

Nato v spletnem brskalniku odpri:

    http://localhost:8080/

Na začetni strani je mogoče izbrati predel Ljubljane s klikom na
interaktivni zemljevid ali poiskati restavracije glede na tip kuhinje.

Po izbiri restavracije je mogoče pregledati njene jedi, pri posamezni
jedi pa tudi sestavine in alergene.


### 5. Zaustavitev spletnega vmesnika

Spletni strežnik ustaviš v terminalu s kombinacijo tipk:

    Ctrl + C

## Avtorja

Jure Kovač, Vanja Stanojević
