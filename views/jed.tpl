<!DOCTYPE html>
<html lang="sl">

<head>
    <meta charset="UTF-8">
    <title>{{ime_jedi}}</title>
</head>

<body>

    <h1>{{ime_jedi}}</h1>


    <h2>Sestavine</h2>

    <ul>
        % if sestavine:

            % for sestavina in sestavine:
                <li>{{sestavina[0]}}</li>
            % end

        % else:

            <li>
                Za izbrano jed ni navedenih sestavin.
                Za dodatne informacije se obrnite na ponudnika.
            </li>

        % end
    </ul>


    <h2>Alergeni</h2>

    <ul>
        % if alergeni:

            % for alergen in alergeni:
                <li>{{alergen[0]}}</li>
            % end

        % else:

            <li>
                Za izbrano jed ni navedenih alergenov.
                Za dodatne informacije se obrnite na ponudnika.
            </li>

        % end
    </ul>


    <p>
        <a href="/restavracija/{{id_restavracije}}?izvor={{izvor}}&vrednost={{vrednost}}">
            ← Nazaj na meni {{ime_restavracije}}
        </a>
    </p>


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