<!DOCTYPE html>
<html lang="sl">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/style.css">
    <title>{{naslov}}</title>
</head>

<body>

    <h1>{{naslov}}</h1>

    <ul>

        % if restavracije:

            % for r in restavracije:

                <li>
                    <a href="/restavracija/{{r[0]}}?izvor={{izvor}}&vrednost={{vrednost}}">
                        {{r[1]}}
                    </a>

                    <br>
                    <span class="podatek">{{r[2]}}</span>
                </li>

            % end

        % else:

            <li>Ni najdenih restavracij.</li>

        % end

    </ul>

    <div class="navigacija">
        <a href="/" class="gumb-nazaj">← Nazaj na začetno stran</a>
    </div>

    <footer>
        Restavracije v Ljubljani · Podatkovne baze 1 · 2025/26
    </footer>

</body>

</html>