# Lot 5 (23/11) : statiques pyjama, formats repris de la veille Domelyah (sans leur « −40 % » ni leur avis invérifiable).
# 1080x1350, bulles natives, aucun prix barré. « La 3e est offerte » = l'offre 2 achetés + 1 offert (77,98 € = 2 × 38,99 €).
import os, sys
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from captions import caption, _emoji
ROOT = os.path.join(HERE, '..'); RAW = os.path.join(ROOT, 'pubs', 'raw', 'lot5'); OUT = os.path.join(ROOT, 'pubs', 'out', 'lot5'); FO = os.path.join(ROOT, 'fonts')
os.makedirs(OUT, exist_ok=True)
W, H = 1080, 1350
FRAMB, BLANC, ENCRE = (158, 59, 75, 245), (255, 255, 255), (43, 31, 30)
PILL = '2 achetés + 1 offert · Livraison offerte'
def F(name, size): return ImageFont.truetype(os.path.join(FO, name), size)
def cover(im, fy=.5):
    s = max(W / im.width, H / im.height); im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x = (im.width - W) // 2; y = int((im.height - H) * fy); return im.crop((x, y, x + W, y + H))
def base(src, fy=.5): return cover(Image.open(os.path.join(RAW, src)).convert('RGB'), fy).convert('RGBA')
def save(im, name): im.convert('RGB').save(os.path.join(OUT, name), quality=92); print('ok', name)
def bubble_static(src, name, top, top_y=110, bottom=PILL, fy=.5, size=48):
    im = base(src, fy)
    if top:
        c = caption(list(top), size=size); im.alpha_composite(c, ((W - c.width) // 2, top_y))
    if bottom:
        c2 = caption([bottom], size=34, bg=FRAMB, fg=BLANC); im.alpha_composite(c2, ((W - c2.width) // 2, H - 150))
    save(im, name)
def big_type(src, name):
    im = base(src); d = ImageDraw.Draw(im); f = F('fraunces-latin-900-italic.woff', 190)
    txt = '1 + 1 + '; tw = int(f.getlength(txt)); e = _emoji('🎁', 165)
    x0 = (W - tw - e.width) // 2; y = 70
    d.text((x0, y), txt, font=f, fill=ENCRE); im.alpha_composite(e, (x0 + tw, y + 40))
    c2 = caption(['2 achetés = le 3e offert 🎁'], size=44, bg=FRAMB, fg=BLANC); im.alpha_composite(c2, ((W - c2.width) // 2, H - 170))
    save(im, name)
if __name__ == '__main__':
    bubble_static('301-lit-ruban.png', 'S19-la-3e-offerte.jpg', ['Ta chérie, ta mère, ta sœur :', 'la 3e est offerte 🎁'])
    bubble_static('302-post-it.png', 'S20-post-it.jpg', ['Tous ses cadeaux', 'dans un seul colis 📦'], bottom='Livraison offerte en France', fy=.4)
    big_type('303-coffret.png', 'S21-1-plus-1-plus-cadeau.jpg')
    bubble_static('304-cintres.png', 'S22-laquelle-elle-va-choisir.jpg', ['Laquelle elle va choisir ? 🤔'], top_y=90)
    bubble_static('305-pile.png', 'S23-une-couleur-pour-chacune.jpg', ['Une couleur pour chacune 🎁'], top_y=90)
    bubble_static('306-pere-noel.png', 'S24-pere-noel.jpg', ['Le père Noël a déjà', 'réglé son cadeau 🎅'], top_y=90)
    bubble_static('307-cocon-creme.jpg', 'S25-produit-seul.jpg', None, bottom=None)
    bubble_static('303-coffret.png', 'S26-elle-sa-soeur-sa-mere.jpg', ['Un pour elle, sa sœur', 'et sa mère 🎁'], top_y=120)
    bubble_static('304-cintres.png', 'S27-messieurs.jpg', ['Messieurs, choisissez sa couleur,', 'on s’occupe du reste 🎁'], top_y=90, size=44)
