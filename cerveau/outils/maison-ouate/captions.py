# Légendes façon TikTok (bulle blanche, texte noir gras, emojis en couleur) pour les pubs Maison Ouate.
# Recréé le 23/11 (le dossier de travail avait été vidé) ; polices DM Sans en .woff (fontsource).
import os, re
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); FO = os.path.join(HERE, '..', 'fonts')
EMOJI_FONT = '/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf'
EMOJI_RE = re.compile('([\U0001F300-\U0001FAFF☀-➿⭐❤️‍]+)')


def _font(size, bold=True):
    return ImageFont.truetype(os.path.join(FO, 'dm-sans-latin-700-normal.woff' if bold else 'dm-sans-latin-400-normal.woff'), size)


def _emoji(e, size):
    f = ImageFont.truetype(EMOJI_FONT, 109)
    tmp = Image.new('RGBA', (160 * max(1, len(e)), 160), (0, 0, 0, 0))
    ImageDraw.Draw(tmp).text((0, 0), e, font=f, embedded_color=True)
    bb = tmp.getbbox() or (0, 0, 1, 1)
    tmp = tmp.crop(bb)
    s = size / 109 * 1.05
    return tmp.resize((max(1, int(tmp.width * s)), max(1, int(tmp.height * s))), Image.LANCZOS)


def _runs(line):
    return [p for p in EMOJI_RE.split(line) if p]


def _line_size(line, f, size):
    w = 0
    for r in _runs(line):
        if EMOJI_RE.fullmatch(r):
            w += _emoji(r, size).width + 4
        else:
            w += int(f.getlength(r))
    return int(w)


def caption(lines, size=36, pad=(22, 12), radius=14, bg=(255, 255, 255, 245), fg=(17, 17, 17), bold=True, gap=4):
    """Une bulle par ligne, centrées, comme les légendes natives de TikTok/Reels."""
    f = _font(size, bold)
    asc, desc = f.getmetrics()
    lh = asc + desc
    bubbles = []
    for line in lines:
        w = _line_size(line, f, size) + 2 * pad[0]
        h = lh + 2 * pad[1]
        im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, w - 1, h - 1), radius, fill=bg)
        x = pad[0]
        for r in _runs(line):
            if EMOJI_RE.fullmatch(r):
                e = _emoji(r, size)
                im.alpha_composite(e, (x, pad[1] + (lh - e.height) // 2))
                x += e.width + 4
            else:
                d.text((x, pad[1]), r, font=f, fill=fg)
                x += int(f.getlength(r))
        bubbles.append(im)
    W = max(b.width for b in bubbles)
    H = sum(b.height for b in bubbles) - (len(bubbles) - 1) * gap
    out = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    y = 0
    for b in bubbles:
        out.alpha_composite(b, ((W - b.width) // 2, y))
        y += b.height - gap
    return out


def overlay_png(path, frame_size, items):
    """items : liste de (image RGBA, y_centre_relatif). Écrit un PNG transparent de la taille de la vidéo."""
    W, H = frame_size
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    for im, yc in items:
        canvas.alpha_composite(im, ((W - im.width) // 2, int(H * yc - im.height / 2)))
    canvas.save(path)
