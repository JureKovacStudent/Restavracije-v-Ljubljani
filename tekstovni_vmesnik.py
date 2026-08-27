import model


# --------------------------------------------------
# GLAVNI MENI
# --------------------------------------------------

def meni():
    print("\n--- RESTAVRACIJE V LJUBLJANI ---")
    print("1 - Izpis vseh restavracij")
    print("2 - Prikaz jedi za restavracijo")
    print("3 - Prikaz sestavin in alergenov za jed")
    print("0 - Izhod")


# --------------------------------------------------
# GLAVNA ZANKA PROGRAMA
# --------------------------------------------------

while True:

    meni()

    izbira = input("Izberi možnost: ")


    # --------------------------------------------------
    # 1 - IZPIS VSEH RESTAVRACIJ
    # --------------------------------------------------

    if izbira == "1":

        restavracije = model.vse_restavracije()

        print("\n--- RESTAVRACIJE ---")

        for r in restavracije:
            print(f"{r[0]} - {r[1]} ({r[2]})")


    # --------------------------------------------------
    # 2 - PRIKAZ JEDI ZA RESTAVRACIJO
    # --------------------------------------------------

    elif izbira == "2":

        id_r = input("Vnesi ID restavracije: ")

        # Preverimo, ali restavracija obstaja
        ime_restavracije = model.ime_restavracije(id_r)

        if ime_restavracije is None:

            print(f"\nRestavracija z ID {id_r} ne obstaja.")

        else:

            jedi = model.jedi_po_restavraciji(id_r)

            print(f"\n--- MENI RESTAVRACIJE {ime_restavracije} ---")

            if jedi:

                for j in jedi:
                    print(f"{j[0]} - {j[1]}")

            else:

                print("Za izbrano restavracijo ni navedenih jedi.")


    # --------------------------------------------------
    # 3 - PRIKAZ SESTAVIN IN ALERGENOV
    # --------------------------------------------------

    elif izbira == "3":

        id_j = input("Vnesi ID jedi: ")

        # Preverimo, ali jed obstaja
        podatki_jedi = model.podatki_o_jedi(id_j)

        if podatki_jedi is None:

            print(f"\nJed z ID {id_j} ne obstaja.")

        else:

            ime_jedi = podatki_jedi[0]

            sestavine = model.sestavine_za_jed(id_j)
            alergeni = model.alergeni_za_jed(id_j)

            print(f"\n--- {ime_jedi} ---")


            # SESTAVINE

            print("\nSestavine:")

            if sestavine:

                for s in sestavine:
                    print("-", s[0])

            else:

                print(
                    "Za izbrano jed ni navedenih sestavin. "
                    "Za dodatne informacije se obrnite na ponudnika."
                )


            # ALERGENI

            print("\nAlergeni:")

            if alergeni:

                for a in alergeni:
                    print("-", a[0])

            else:

                print(
                    "Za izbrano jed ni navedenih alergenov. "
                    "Za dodatne informacije se obrnite na ponudnika."
                )


    # --------------------------------------------------
    # 0 - IZHOD
    # --------------------------------------------------

    elif izbira == "0":

        print("\nIzhod iz programa.")
        break


    # --------------------------------------------------
    # NEVELJAVNA IZBIRA
    # --------------------------------------------------

    else:

        print(
            "\nNeveljavna izbira. "
            "Izberi 0, 1, 2 ali 3."
        )