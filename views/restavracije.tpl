<!DOCTYPE html>
<html lang="sl">

<head>
    <meta charset="UTF-8">
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

                    - {{r[2]}}
                </li>

            % end

        % else:

            <li>Ni najdenih restavracij.</li>

        % end

    </ul>

    <p>
        <a href="/">← Nazaj na začetno stran</a>
    </p>

</body>
</html>