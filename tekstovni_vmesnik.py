import model

# Izpis glavnega menija aplikacije
def meni():
    print("\n--- RESTAVRACIJE V LJUBLJANI ---")
    print("1 - Izpis vseh restavracij")
    print("2 - Prikaz jedi za restavracijo")
    print("3 - Prikaz sestavin in alergenov za jed")
    print("0 - Izhod")


# Glavna zanka programa (tekstovni vmesnik)
while True:
    meni()
    izbira = input("Izberi možnost: ")

    # Izpis vseh restavracij
    if izbira == "1":
        restavracije = model.vse_restavracije()
        for r in restavracije:
            print(f"{r[0]} - {r[1]} ({r[2]})")

    # Prikaz jedi za izbrano restavracijo
    elif izbira == "2":
        id_r = input("Vnesi ID restavracije: ")
        jedi = model.jedi_po_restavraciji(id_r)
        for j in jedi:
            print(f"{j[0]} - {j[1]}")


    # Prikaz sestavin in alergenov za izbrano jed
    elif izbira == "3":
        id_j = input("Vnesi ID jedi: ")

        sestavine = model.sestavine_za_jed(id_j)
        alergeni = model.alergeni_za_jed(id_j)

        print("\nSestavine:")
        for s in sestavine:
            print("-", s[0])

        print("\nAlergeni:")
        if alergeni:
            for a in alergeni:
                print("-", a[0])
        else:
            print("Ni alergenov.")

    # Izhod iz programa
    elif izbira == "0":
        print("Izhod...")
        break

    else:
        print("Neveljavna izbira.")