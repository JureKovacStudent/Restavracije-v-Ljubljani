import sqlite3

BAZA = "RestavracijeVLjubljani.db"


# Povezava s podatkovno bazo
def povezava():
    conn = sqlite3.connect(BAZA)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


# Vrne vse restavracije
def vse_restavracije():
    conn = povezava()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_restavracije, ime, naslov
        FROM Restavracija;
    """)

    podatki = cursor.fetchall()
    conn.close()
    return podatki


def ime_restavracije(id_restavracije):
    conn = povezava()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ime
        FROM Restavracija
        WHERE id_restavracije = ?;
    """, (id_restavracije,))

    podatek = cursor.fetchone()
    conn.close()

    if podatek:
        return podatek[0]

    return None


# Vrne jedi posamezne restavracije
def jedi_po_restavraciji(id_restavracije):
    conn = povezava()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT j.id_jedi, j.ime
        FROM Jed j
        JOIN Meni m ON j.id_menija = m.id_menija
        WHERE m.id_restavracije = ?;
    """, (id_restavracije,))

    podatki = cursor.fetchall()
    conn.close()
    return podatki

# Vrne podatke o posamezni jedi
def podatki_o_jedi(id_jedi):
    conn = povezava()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT j.ime, m.id_restavracije
        FROM Jed j
        JOIN Meni m ON j.id_menija = m.id_menija
        WHERE j.id_jedi = ?;
    """, (id_jedi,))

    podatek = cursor.fetchone()
    conn.close()

    return podatek


# Vrne sestavine posamezne jedi
def sestavine_za_jed(id_jedi):
    conn = povezava()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.naziv
        FROM Sestavina s
        JOIN Jed_Sestavina js
            ON s.id_sestavine = js.id_sestavine
        WHERE js.id_jedi = ?;
    """, (id_jedi,))

    podatki = cursor.fetchall()
    conn.close()
    return podatki


# Vrne alergene posamezne jedi
def alergeni_za_jed(id_jedi):
    conn = povezava()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.naziv
        FROM Alergen a
        JOIN Jed_Alergen ja
            ON a.id_alergena = ja.id_alergena
        WHERE ja.id_jedi = ?;
    """, (id_jedi,))

    podatki = cursor.fetchall()
    conn.close()
    return podatki


# Vrne restavracije iz izbranega predela Ljubljane
def restavracije_po_predelu(predel):
    conn = povezava()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id_restavracije, ime, naslov
        FROM Restavracija
        WHERE predel = ?;
    """, (predel,))

    podatki = cursor.fetchall()
    conn.close()
    return podatki


# Vrne restavracije glede na izbrani tip kuhinje
def restavracije_po_kuhinji(tip_kuhinje):
    conn = povezava()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT r.id_restavracije, r.ime, r.naslov
        FROM Restavracija r
        JOIN Meni m
            ON r.id_restavracije = m.id_restavracije
        JOIN Jed j
            ON m.id_menija = j.id_menija
        JOIN Tip_Kuhinje t
            ON j.id_tipa_kuhinje = t.id_tipa_kuhinje
        WHERE t.naziv = ?;
    """, (tip_kuhinje,))

    podatki = cursor.fetchall()
    conn.close()
    return podatki