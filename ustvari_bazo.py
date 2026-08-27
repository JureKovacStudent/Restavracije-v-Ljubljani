import sqlite3
import csv
import os

BAZA = "RestavracijeVLjubljani.db"
MAPA_PODATKI = "podatki"


def preberi_csv(ime_datoteke):
    pot = os.path.join(MAPA_PODATKI, ime_datoteke)

    with open(pot, "r", encoding="utf-8-sig", newline="") as datoteka:
        return list(csv.DictReader(datoteka))


def ustvari_bazo():
    # Če baza že obstaja, jo odstranimo in ustvarimo na novo.
    if os.path.exists(BAZA):
        os.remove(BAZA)

    conn = sqlite3.connect(BAZA)
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    # Ustvarjanje tabel
    cursor.executescript("""
        CREATE TABLE Restavracija (
            id_restavracije INTEGER PRIMARY KEY AUTOINCREMENT,
            ime TEXT NOT NULL,
            naslov TEXT NOT NULL,
            predel TEXT
        );

        CREATE TABLE Meni (
            id_menija INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv TEXT NOT NULL,
            id_restavracije INTEGER NOT NULL UNIQUE,
            FOREIGN KEY (id_restavracije)
                REFERENCES Restavracija(id_restavracije)
        );

        CREATE TABLE Tip_kuhinje (
            id_tipa_kuhinje INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv TEXT NOT NULL
        );

        CREATE TABLE Jed (
            id_jedi INTEGER PRIMARY KEY AUTOINCREMENT,
            ime TEXT NOT NULL,
            cena REAL NOT NULL,
            id_menija INTEGER NOT NULL,
            id_tipa_kuhinje INTEGER NOT NULL,
            FOREIGN KEY (id_menija)
                REFERENCES Meni(id_menija),
            FOREIGN KEY (id_tipa_kuhinje)
                REFERENCES Tip_kuhinje(id_tipa_kuhinje)
        );

        CREATE TABLE Sestavina (
            id_sestavine INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv TEXT NOT NULL
        );

        CREATE TABLE Alergen (
            id_alergena INTEGER PRIMARY KEY AUTOINCREMENT,
            naziv TEXT NOT NULL
        );

        CREATE TABLE Jed_Sestavina (
            id_jedi INTEGER,
            id_sestavine INTEGER,
            PRIMARY KEY (id_jedi, id_sestavine),
            FOREIGN KEY (id_jedi)
                REFERENCES Jed(id_jedi),
            FOREIGN KEY (id_sestavine)
                REFERENCES Sestavina(id_sestavine)
        );

        CREATE TABLE Jed_Alergen (
            id_jedi INTEGER,
            id_alergena INTEGER,
            PRIMARY KEY (id_jedi, id_alergena),
            FOREIGN KEY (id_jedi)
                REFERENCES Jed(id_jedi),
            FOREIGN KEY (id_alergena)
                REFERENCES Alergen(id_alergena)
        );
    """)

    # Vnos restavracij
    for r in preberi_csv("restavracije.csv"):
        cursor.execute("""
            INSERT INTO Restavracija
                (id_restavracije, ime, naslov, predel)
            VALUES (?, ?, ?, ?);
        """, (
            int(r["id_restavracije"]),
            r["ime"],
            r["naslov"],
            r["predel"]
        ))

    # Vnos menijev
    for m in preberi_csv("meniji.csv"):
        cursor.execute("""
            INSERT INTO Meni
                (id_menija, naziv, id_restavracije)
            VALUES (?, ?, ?);
        """, (
            int(m["id_menija"]),
            m["naziv"],
            int(m["id_restavracije"])
        ))

    # Vnos tipov kuhinje
    for t in preberi_csv("tipi_kuhinje.csv"):
        cursor.execute("""
            INSERT INTO Tip_kuhinje
                (id_tipa_kuhinje, naziv)
            VALUES (?, ?);
        """, (
            int(t["id_tipa_kuhinje"]),
            t["naziv"]
        ))

    # Vnos jedi
    for j in preberi_csv("jedi.csv"):
        cursor.execute("""
            INSERT INTO Jed
                (id_jedi, ime, cena, id_menija, id_tipa_kuhinje)
            VALUES (?, ?, ?, ?, ?);
        """, (
            int(j["id_jedi"]),
            j["ime"],
            float(j["cena"]),
            int(j["id_menija"]),
            int(j["id_tipa_kuhinje"])
        ))

    # Vnos sestavin
    for s in preberi_csv("sestavine.csv"):
        cursor.execute("""
            INSERT INTO Sestavina
                (id_sestavine, naziv)
            VALUES (?, ?);
        """, (
            int(s["id_sestavine"]),
            s["naziv"]
        ))

    # Vnos alergenov
    for a in preberi_csv("alergeni.csv"):
        cursor.execute("""
            INSERT INTO Alergen
                (id_alergena, naziv)
            VALUES (?, ?);
        """, (
            int(a["id_alergena"]),
            a["naziv"]
        ))

    # Povezave med jedmi in sestavinami
    for js in preberi_csv("jed_sestavina.csv"):
        cursor.execute("""
            INSERT INTO Jed_Sestavina
                (id_jedi, id_sestavine)
            VALUES (?, ?);
        """, (
            int(js["id_jedi"]),
            int(js["id_sestavine"])
        ))

    # Povezave med jedmi in alergeni
    for ja in preberi_csv("jed_alergen.csv"):
        cursor.execute("""
            INSERT INTO Jed_Alergen
                (id_jedi, id_alergena)
            VALUES (?, ?);
        """, (
            int(ja["id_jedi"]),
            int(ja["id_alergena"])
        ))

    conn.commit()
    conn.close()

    print("Baza RestavracijeVLjubljani.db je bila uspešno ustvarjena.")


if __name__ == "__main__":
    ustvari_bazo()
