<!DOCTYPE html>
<html lang="sl">

<head>
    <meta charset="UTF-8">
    <title>Meni {{ime_restavracije}}</title>
</head>

<body>

    <h1>Meni {{ime_restavracije}}</h1>

    <ul>

        % for jed in jedi:

            <li>
                <a href="/jed/{{jed[0]}}?izvor={{izvor}}&vrednost={{vrednost}}">
                    {{jed[1]}}
                </a>
            </li>

        % end

    </ul>


    % if izvor == "predel":

        <p>
            <a href="/predel/{{vrednost}}">
                ← Nazaj na restavracije – {{vrednost}}
            </a>
        </p>

    % elif izvor == "kuhinja":

        <p>
            <a href="/kuhinja?tip={{vrednost}}">
                ← Nazaj na restavracije – {{vrednost}} kuhinja
            </a>
        </p>

    % end


    <p>
        <a href="/">
            ← Nazaj na začetno stran
        </a>
    </p>

</body>

</html>