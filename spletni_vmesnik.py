import bottle
import model


# Omogoči prikaz datotek iz mape static
@bottle.get("/static/<filename>")
def staticna_datoteka(filename):
    return bottle.static_file(filename, root="./static")


# --------------------------------------------------
# GLAVNA STRAN
# --------------------------------------------------

@bottle.get("/")
def zacetna_stran():

    return bottle.template("zacetna")


# --------------------------------------------------
# RESTAVRACIJE PO PREDELU
# --------------------------------------------------

@bottle.get("/predel/<predel>")
def prikazi_predel(predel):

    restavracije = model.restavracije_po_predelu(predel)

    naslov = "Restavracije - " + predel

    return bottle.template(
        "restavracije",
        restavracije=restavracije,
        naslov=naslov,
        izvor="predel",
        vrednost=predel
    )


# --------------------------------------------------
# RESTAVRACIJE PO TIPU KUHINJE
# --------------------------------------------------

@bottle.get("/kuhinja")
def prikazi_po_kuhinji():

    tip = bottle.request.query.tip

    restavracije = model.restavracije_po_kuhinji(tip)

    naslov = "Restavracije - " + tip + " kuhinja"

    return bottle.template(
        "restavracije",
        restavracije=restavracije,
        naslov=naslov,
        izvor="kuhinja",
        vrednost=tip
    )


# --------------------------------------------------
# POSAMEZNA RESTAVRACIJA
# --------------------------------------------------

@bottle.get("/restavracija/<id_restavracije:int>")
def prikazi_restavracijo(id_restavracije):

    jedi = model.jedi_po_restavraciji(id_restavracije)
    ime_restavracije = model.ime_restavracije(id_restavracije)

    izvor = bottle.request.query.izvor
    vrednost = bottle.request.query.vrednost

    return bottle.template(
        "restavracija",
        jedi=jedi,
        ime_restavracije=ime_restavracije,
        id_restavracije=id_restavracije,
        izvor=izvor,
        vrednost=vrednost
    )


# --------------------------------------------------
# POSAMEZNA JED
# --------------------------------------------------

@bottle.get("/jed/<id_jedi:int>")
def prikazi_jed(id_jedi):

    podatki_jedi = model.podatki_o_jedi(id_jedi)

    sestavine = model.sestavine_za_jed(id_jedi)
    alergeni = model.alergeni_za_jed(id_jedi)

    ime_jedi = podatki_jedi[0]
    id_restavracije = podatki_jedi[1]

    ime_restavracije = model.ime_restavracije(id_restavracije)

    izvor = bottle.request.query.izvor
    vrednost = bottle.request.query.vrednost

    return bottle.template(
        "jed",
        ime_jedi=ime_jedi,
        id_restavracije=id_restavracije,
        ime_restavracije=ime_restavracije,
        izvor=izvor,
        vrednost=vrednost,
        sestavine=sestavine,
        alergeni=alergeni
    )


# --------------------------------------------------
# ZAGON
# --------------------------------------------------

bottle.run(
    host="localhost",
    port=8080,
    debug=True,
    reloader=True
)