# Outils réutilisables

Scripts écrits pendant la production des pubs unlined. Ils demandent `ffmpeg` (avec libass pour les sous-titres) et, pour la transcription, `faster-whisper` (modèle « small », sur CPU).

| Script | Rôle |
|---|---|
| `filtre-iphone.sh` | Donne un rendu « vraie vidéo iPhone » à une vidéo IA trop nette : image adoucie, grain, légère respiration d'exposition, recompression, son de pièce. Options : tremblement de caméra, son de pièce. |
| `sous-titres-ugc.py` | Transcrit la vidéo mot à mot et incruste des sous-titres façon UGC (DM Sans blanc, 4 mots maximum, au tiers bas). |
| `horodatage-mots.py` | Horodatage mot à mot d'une voix off (JSON), pour caler des plans ou vérifier qu'une voix dit exactement le script. |
| `raccourcir-silences.py` | Raccourcit des silences précis d'une voix off pour la faire tenir dans une durée (par exemple sous 30 s pour Wan). |
| `comparer-voix.py` | Compare plusieurs voix candidates : durée, hauteur de voix (plus grave = plus mature), expressivité, transcription. |
| `effacer-logo.py` | Efface un faux logo inventé par l'IA sur un objet du décor, image par image (reconstruction OpenCV). |
| `accroche-medaillon.py` | Accroche « médaillon » : gros plan macro des rides, feutre rouge animé et actrice en médaillon sur les premières secondes, puis la vidéo d'origine, avec ses sous-titres (fichier ASS). Polices Bodoni Moda et DM Sans dans `polices/`. |
| `accroche-garantie.py` | Bandeau « Smoother-looking lip lines in about 60 seconds. Or your money back » sur les 3,6 premières secondes d'une vidéo sous-titrée. |
| `accroche-bandeau.py` | Même bandeau, avec ses propres textes : 2 lignes et une pastille rouge (ex. « Before your next / Botox appointment… / watch this »). |
| `cart-drawer.liquid` | Panier tiroir Shopify autonome (balisage, style et script) : à mettre dans `snippets/` et à rendre avant `</body>`. |
| `srt-vers-texte.py` | Transforme des sous-titres automatiques YouTube en texte lisible, avec un repère par minute. |

Les sous-titres utilisent la police DM Sans : télécharge-la sur Google Fonts et place `DMSans-Bold.ttf` dans `outils/polices/`. Les accroches demandent aussi `DMSans-Regular.ttf`, `BodoniModa-Bold.ttf` et `BodoniModa-Black.ttf`.
