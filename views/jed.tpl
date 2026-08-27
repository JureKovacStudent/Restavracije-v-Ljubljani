<!DOCTYPE html>
<html lang="sl">

<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/style.css">
    <title>{{ime_jedi}}</title>
</head>

<body>

    <h1>{{ime_jedi}}</h1>

    <div class="podrobnosti-jedi">

        <section class="sestavine">
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
        </section>


        <section class="alergeni">
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
        </section>

    </div>


    <div class="navigacija">

        <a href="/restavracija/{{id_restavracije}}?izvor={{izvor}}&vrednost={{vrednost}}" class="gumb-nazaj">
            ← Nazaj na meni {{ime_restavracije}}
        </a>


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