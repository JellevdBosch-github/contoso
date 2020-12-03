# contoso
IIPBDAM2 Herkansing webapp over fictief bedrijf contoso b.v.

Installatie Guide:
1. Clone project
2. Installeer dependancies
  - conda:
    cd naar requirements dir,
    type in terminal: conda create --name foobar_env --file conda-requirements.txt
  - pip:
    cd naar requirements directory,
    in terminal: pip install -r requirements.txt
3. Activeer env
  - conda:
      - conda activate foobar_env
3. maak database genaamd 'contoso' aan (mysql)
4. run de applicatie (db tabellen worden aangemaakt)
5. maak een medewerker account aan op /account/employee/signup
6. maak een klant account aan op /account/signup

Overige info:
- Je hebt een categorie nodig om een product te kunnen maken, dit doe je door de naam vd categorie te gebruiken als identificatie
- Je kan producten/categorieen beheren op het dashboard, mits je een employee bent
