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
| `srt-vers-texte.py` | Transforme des sous-titres automatiques YouTube en texte lisible, avec un repère par minute. |

Les sous-titres utilisent la police DM Sans : télécharge-la sur Google Fonts et place `DMSans-Bold.ttf` dans `outils/polices/`.
