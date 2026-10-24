# ecodesignagency.com → henryandco.it/en/

Il vecchio dominio ecodesignagency.com è servito da GitHub Pages solo per reindirizzare
ogni vecchia pagina alla pagina equivalente su https://www.henryandco.it/en/.

- `redirects.json`: vecchio percorso → nuova pagina (più alcune regole per famiglie di percorsi).
- `build.py`: genera le pagine di reindirizzamento in `_site/`.
- Il workflow pubblica `_site/` su GitHub Pages a ogni modifica.
