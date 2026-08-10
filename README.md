# Restavracije v Ljubljani

Seminarska naloga pri predmetu Podatkovne baze 1.

## Namen projekta

Namen projekta je izdelava podatkovne baze restavracij v Ljubljani in
aplikacije, ki uporabniku omogoča pregledovanje restavracij, njihovih
menijev in jedi.

Pri posamezni jedi so shranjeni tudi podatki o sestavinah, alergenih
in tipu kuhinje.

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

Za zagon tekstovnega vmesnika:

    python tekstovni_vmesnik.py

Za zagon spletnega vmesnika:

    python spletni_vmesnik.py

Nato v brskalniku odpremo:

    http://localhost:8080/

## Avtorja

[VAJINI IMENI]
