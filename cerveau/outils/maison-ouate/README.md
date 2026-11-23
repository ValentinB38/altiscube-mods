# Outils de production des pubs Maison Ouate

Copiés ici le 23/11/2026 : le dossier de travail de la session a été vidé ce week-end, avec tous les scripts, polices, clips et musiques. Ils survivent désormais dans le dépôt.

- `captions.py` : les légendes façon TikTok/Reels (bulle blanche, texte gras, emojis en couleur).
- `montage_lot5.py` : les vidéos d'essayage de 11,5 s, au montage de la gagnante V1 (8 plans, gros plan puis miroir, accroche puis appel à l'action). Pour une nouvelle série, changer seulement le dictionnaire `VIDEOS`.
- `statics_lot5.py` : les statiques 4:5 (bulles, pastille d'offre, grand titre).

**Ce qu'il faut à côté (pas dans le dépôt) :**
- **Polices** DM Sans et Fraunces, en .woff, à récupérer avec `npm pack @fontsource/dm-sans @fontsource/fraunces`.
- **Police emoji** : Noto Color Emoji du système.
- **Clips d'essayage** : les 12 clips wan3_0 du 06/11, à retrouver dans l'historique Higgsfield (vidéos, prompts « try-on », 6 gros plans et 6 plans au miroir : crème, noir, bleu, lilas, rose, Noël).
- **Musique** : instrumentale générée sur Higgsfield (elevenlabs_music).

**Leçon :** télécharger les images servies par Shopify avec l'en-tête `Accept: image/jpeg`, sinon le CDN renvoie de l'AVIF ou du WebP (piège du 11/11).
