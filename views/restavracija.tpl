<!DOCTYPE html>
<html lang="sl">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/style.css">
    <title>Meni {{ime_restavracije}}</title>
</head>

<body>

    <h1>Meni {{ime_restavracije}}</h1>

    <p class="uvod">Izberi jed za več informacij.</p>

    <ul>

        % for jed in jedi:

            <li>
                <a href="/jed/{{jed[0]}}?izvor={{izvor}}&vrednost={{vrednost}}">
                    {{jed[1]}}
                </a>
            </li>

        % end

    </ul>

    <div class="navigacija">

        % if izvor == "predel":

            <a href="/predel/{{vrednost}}" class="gumb-nazaj">
                ← Nazaj na restavracije – {{vrednost}}
            </a>

        % elif izvor == "kuhinja":

            <a href="/kuhinja?tip={{vrednost}}" class="gumb-nazaj">
                ← Nazaj na restavracije – {{vrednost}} kuhinja
            </a>

        % end

        <a href="/" class="gumb-nazaj">
            ← Nazaj na začetno stran
        </a>

    </div>

    <footer>
        Restavracije v Ljubljani · Podatkovne baze 1 · 2025/26
    </footer>

</body>

</html>