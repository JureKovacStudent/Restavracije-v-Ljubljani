import sqlite3

# Ime SQLite baze
BAZA = "RestavracijeVLjubljani.db"

# Funkcija ustvari povezavo na bazo
# in vklopi preverjanje tujih ključev
def povezava():
    conn = sqlite3.connect(BAZA)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


# Vrne seznam vseh restavracij
def vse_restavracije():
    conn = povezava()
    cursor = conn.cursor()

    # Poizvedba za pridobitev osnovnih podatkov
    cursor.execute("SELECT id_restavracije, ime, naslov FROM Restavracija;")

    podatki = cursor.fetchall()
    conn.close()
    return podatki


# Vrne vse jedi, ki pripadajo izbrani restavraciji
def jedi_po_restavraciji(id_restavracije):
    conn = povezava()
    cursor = conn.cursor()

    # Vrne ID in ime jedi
    cursor.execute("""
        SELECT j.id_jedi, j.ime
        FROM Jed j
        JOIN Meni m ON j.id_menija = m.id_menija
        WHERE m.id_restavracije = ?;
    """, (id_restavracije,))

    podatki = cursor.fetchall()
    conn.close()
    return podatki


# Vrne sestavine za izbrano jed
def sestavine_za_jed(id_jedi):
    conn = povezava()
    cursor = conn.cursor()

    # Povezovalna tabela Jed_Sestavina
    cursor.execute("""
        SELECT s.naziv
        FROM Sestavina s
        JOIN Jed_Sestavina js ON s.id_sestavine = js.id_sestavine
        WHERE js.id_jedi = ?;
    """, (id_jedi,))

    podatki = cursor.fetchall()
    conn.close()
    return podatki


# Vrne alergene za izbrano jed
def alergeni_za_jed(id_jedi):
    conn = povezava()
    cursor = conn.cursor()

    # Povezovalna tabela Jed_Alergen
    cursor.execute("""
        SELECT a.naziv
        FROM Alergen a
        JOIN Jed_Alergen ja ON a.id_alergena = ja.id_alergena
        WHERE ja.id_jedi = ?;
    """, (id_jedi,))

    podatki = cursor.fetchall()
    conn.close()
    return podatki