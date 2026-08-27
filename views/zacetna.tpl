<!DOCTYPE html>
<html lang="sl">

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

        select,
        button {
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

    <p>Izberi predel Ljubljane:</p>

    <!-- SVG zemljevid Ljubljane -->
    <object
        id="zemljevid"
        type="image/svg+xml"
        data="/static/ljubljana.svg">
    </object>


    <!-- Izbira tipa kuhinje -->
    <div class="kuhinja">

        <p>Ali izberi tip kuhinje:</p>

        <form action="/kuhinja" method="get">

            <select name="tip" required>

                <option value="">
                    -- Izberi tip kuhinje --
                </option>

                <option value="Italijanska">Italijanska</option>
                <option value="Azijska">Azijska</option>
                <option value="Ameriška">Ameriška</option>
                <option value="Mediteranska">Mediteranska</option>
                <option value="Veganska">Veganska</option>

            </select>

            <button type="submit">Poišči</button>

        </form>

    </div>


    <!-- Omogočimo klikanje na posamezne predele SVG zemljevida -->
    <script>

        const zemljevid = document.getElementById("zemljevid");

        zemljevid.addEventListener("load", function() {

            const svg = zemljevid.contentDocument;

            // ID elementa v SVG -> ime predela v podatkovni bazi
            const predeli = {
                "siska": "Šiška",
                "bezigrad": "Bežigrad",
                "jarse": "Jarše",
                "center": "Center",
                "moste": "Moste",
                "vic": "Vič",
                "rudnik": "Rudnik"
            };

            for (const id in predeli) {

                const element = svg.getElementById(id);

                if (element) {

                    element.style.cursor = "pointer";

                    // Klik na predel odpre seznam restavracij
                    element.addEventListener("click", function() {

                        window.location.href =
                            "/predel/" +
                            encodeURIComponent(predeli[id]);

                    });

                    // Vizualni odziv ob premiku miške čez predel
                    element.addEventListener("mouseenter", function() {
                        element.style.opacity = "0.7";
                    });

                    element.addEventListener("mouseleave", function() {
                        element.style.opacity = "1";
                    });
                }
            }
        });

    </script>

</body>
</html>