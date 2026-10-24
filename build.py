"""Genera il sito statico di reindirizzamento di ecodesignagency.com verso henryandco.it/en/.
Ogni vecchio indirizzo ha la sua pagina con reindirizzamento immediato (meta refresh 0 + canonical),
che Google tratta come un redirect permanente. Gli indirizzi non mappati passano da 404.html."""
import html, json, os

cfg = json.load(open('redirects.json', encoding='utf-8'))
OUT = '_site'

def pagina(dest):
    d = html.escape(dest, quote=True)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>HENRY &amp; CO. – ecodesign agency</title>
<link rel="canonical" href="{d}">
<meta http-equiv="refresh" content="0; url={d}">
<script>location.replace({json.dumps(dest)} + location.hash)</script>
</head><body><p>This page has moved to <a href="{d}">{d}</a>.</p></body></html>
'''

for path, dest in cfg['redirect'].items():
    cartella = os.path.join(OUT, path.strip('/'))
    os.makedirs(cartella, exist_ok=True)
    with open(os.path.join(cartella, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(pagina(dest))

js = json.dumps({'r': cfg['redirect'], 'p': cfg['prefissi'], 'd': cfg['default']}, ensure_ascii=False)
with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
    f.write(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>HENRY &amp; CO. – ecodesign agency</title>
<meta name="robots" content="noindex">
<script>
(function () {{
  var c = {js};
  var p = location.pathname.replace(/\\/+$/, '') + '/';
  var dest = c.r[p];
  if (!dest) {{ var s = p.split('/')[1]; dest = c.p[s] || c.d; }}
  location.replace(dest);
}})();
</script>
<meta http-equiv="refresh" content="2; url={html.escape(cfg['default'])}">
</head><body><p>HENRY &amp; CO. – <a href="{html.escape(cfg['default'])}">www.henryandco.it/en/</a></p></body></html>
''')

with open(os.path.join(OUT, 'robots.txt'), 'w') as f:
    f.write('User-agent: *\nAllow: /\n')
open(os.path.join(OUT, '.nojekyll'), 'w').close()
print('pagine:', len(cfg['redirect']))
