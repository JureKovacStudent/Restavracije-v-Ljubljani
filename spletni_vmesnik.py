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

    html = """
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>Restavracije v Ljubljani</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin: 0;
                padding: 20px;
            }

            h1 {
                margin-bottom: 10px;
            }

            #zemljevid {
                width: 1200px;
                max-width: 90%;
                height: 650px;
                border: none;
            }

            select, button {
                font-size: 16px;
                padding: 8px;
            }

            .kuhinja {
                margin-top: 25px;
            }
        </style>
    </head>

    <body>

        <h1>Restavracije v Ljubljani</h1>

        <p>
            Izberi predel Ljubljane:
        </p>


        <!-- SVG ZEMLJEVID -->

        <object
            id="zemljevid"
            type="image/svg+xml"
            data="/static/ljubljana.svg">
        </object>


        <!-- IZBIRA TIPA KUHINJE -->

        <div class="kuhinja">

            <p>Ali izberi tip kuhinje:</p>

            <form action="/kuhinja" method="get">

                <select name="tip" required>

                    <option value="">
                        -- Izberi tip kuhinje --
                    </option>

                    <option value="Italijanska">
                        Italijanska
                    </option>

                    <option value="Azijska">
                        Azijska
                    </option>

                    <option value="Ameriška">
                        Ameriška
                    </option>

                    <option value="Mediteranska">
                        Mediteranska
                    </option>

                    <option value="Veganska">
                        Veganska
                    </option>

                </select>

                <button type="submit">
                    Poišči
                </button>

            </form>

        </div>


        <!-- KLIKI NA SVG -->

        <script>

            const zemljevid = document.getElementById("zemljevid");

            zemljevid.addEventListener("load", function() {

                const svg =
                    zemljevid.contentDocument;


                // Povezava med ID-jem v SVG in predelom v bazi

                const predeli = {
                    "siska": "Šiška",
                    "bezigrad": "Bežigrad",
                    "jarse": "Jarše",
                    "center": "Center",
                    "moste": "Moste",
                    "vic": "Vič",
                    "rudnik": "Rudnik"
                };


                // Vsak predel naredimo klikljiv

                for (const id in predeli) {

                    const element =
                        svg.getElementById(id);

                    if (element) {

                        element.style.cursor = "pointer";


                        // Klik na predel

                        element.addEventListener(
                            "click",
                            function() {

                                window.location.href =
                                    "/predel/" +
                                    encodeURIComponent(predeli[id]);

                            }
                        );


                        // Ko gremo z miško čez predel

                        element.addEventListener(
                            "mouseenter",
                            function() {
                                element.style.opacity = "0.7";
                            }
                        );


                        // Ko miško umaknemo

                        element.addEventListener(
                            "mouseleave",
                            function() {
                                element.style.opacity = "1";
                            }
                        );

                    }

                }

            });

        </script>

    </body>
    </html>
    """

    return html


# --------------------------------------------------
# RESTAVRACIJE PO PREDELU
# --------------------------------------------------

@bottle.get("/predel/<predel>")
def prikazi_predel(predel):

    restavracije = model.restavracije_po_predelu(predel)

    html = f"""
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>{predel}</title>
    </head>

    <body>

        <h1>Restavracije - {predel}</h1>

        <ul>
    """

    for r in restavracije:

        html += f"""
        <li>
            <a href="/restavracija/{r[0]}">
                {r[1]}
            </a>

            - {r[2]}
        </li>
        """

    if not restavracije:
        html += "<li>V tem predelu ni restavracij.</li>"

    html += """
        </ul>

        <p>
            <a href="/">Nazaj na začetno stran</a>
        </p>

    </body>
    </html>
    """

    return html


# --------------------------------------------------
# RESTAVRACIJE PO TIPU KUHINJE
# --------------------------------------------------

@bottle.get("/kuhinja")
def prikazi_po_kuhinji():

    tip = bottle.request.query.tip

    restavracije = model.restavracije_po_kuhinji(tip)

    html = f"""
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>{tip}</title>
    </head>

    <body>

        <h1>Restavracije - {tip} kuhinja</h1>

        <ul>
    """

    for r in restavracije:

        html += f"""
        <li>
            <a href="/restavracija/{r[0]}">
                {r[1]}
            </a>

            - {r[2]}
        </li>
        """

    if not restavracije:
        html += "<li>Ni restavracij s tem tipom kuhinje.</li>"

    html += """
        </ul>

        <p>
            <a href="/">Nazaj na začetno stran</a>
        </p>

    </body>
    </html>
    """

    return html


# --------------------------------------------------
# POSAMEZNA RESTAVRACIJA
# --------------------------------------------------

@bottle.get("/restavracija/<id_restavracije:int>")
def prikazi_restavracijo(id_restavracije):

    jedi = model.jedi_po_restavraciji(id_restavracije)

    html = """
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>Meni</title>
    </head>

    <body>

        <h1>Meni restavracije</h1>

        <ul>
    """

    for jed in jedi:

        html += f"""
        <li>
            <a href="/jed/{jed[0]}">
                {jed[1]}
            </a>
        </li>
        """

    html += """
        </ul>

        <p>
            <a href="/">Nazaj na začetno stran</a>
        </p>

    </body>
    </html>
    """

    return html


# --------------------------------------------------
# POSAMEZNA JED
# --------------------------------------------------

@bottle.get("/jed/<id_jedi:int>")
def prikazi_jed(id_jedi):

    sestavine = model.sestavine_za_jed(id_jedi)
    alergeni = model.alergeni_za_jed(id_jedi)

    html = """
    <!DOCTYPE html>
    <html>

    <head>
        <meta charset="UTF-8">
        <title>Podatki o jedi</title>
    </head>

    <body>

        <h1>Podatki o jedi</h1>

        <h2>Sestavine</h2>

        <ul>
    """

    for sestavina in sestavine:
        html += f"<li>{sestavina[0]}</li>"

    html += """
        </ul>

        <h2>Alergeni</h2>

        <ul>
    """

    if alergeni:

        for alergen in alergeni:
            html += f"<li>{alergen[0]}</li>"

    else:
        html += "<li>Ni navedenih alergenov.</li>"

    html += """
        </ul>

        <p>
            <a href="/">Nazaj na začetno stran</a>
        </p>

    </body>
    </html>
    """

    return html


# --------------------------------------------------
# ZAGON
# --------------------------------------------------

bottle.run(
    host="localhost",
    port=8080,
    debug=True,
    reloader=True
)