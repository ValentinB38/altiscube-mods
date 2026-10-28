# Playbook 03 : créas

Sources : AC = Adam Citron, NOUS = ce qu'on a produit et appris sur unlined.

## C1. Du volume dès le lancement
- Environ 25 créas par test : 25 vidéos pour le produit 1, 23 pour le produit 2, puis 12 et 30 statiques. (AC J2, J7, J8, J10)
- « Avec l'IA, 100 créas, ça se fait en une journée. » (AC vidéo J1)

## C2. Un mélange de vidéos IA et de vidéos UGC, de 20 à 45 s
Plusieurs formats différents dans la même CBO. (AC vidéo J7)

## C3. La vidéo d'abord, la statique en renfort
- « Un produit se scale avant tout en vidéo. Si les vidéos ne prennent pas, ça ne marchera pas. »
- Une statique peut pourtant devenir gagnante : 4 ventes sur 13 dès son premier jour.
- Les statiques vont dans un adset à part, vers J4-J5 (M5). (AC vidéo J7, J8)

## C4. Pour monter en budget, ajouter des vidéos
Plus de budget = plus de créas nécessaires pour laisser du choix à Meta. (AC vidéo J7)

## C5. Le signal qu'une créa est bonne
Le CPM baisse et le CTR tient. Chez Adam : CTR stable autour de 4 %, CPM divisé par 2 en une semaine. (AC vidéo J7)

## C6. Nos recettes de production (coûts Higgsfield au 28/10/2026)

| Format | Recette | Coût |
|---|---|---|
| **UGC face caméra 30 s** (recommandé) | Actrice FLUX 3 en prompt JSON (environ 3 crédits par image), puis Wan 3.0 en 720p avec le texte exact dans le prompt (52,5), puis voice change vers une voix ElevenLabs (environ 4), puis `outils/filtre-iphone.sh`, puis `outils/sous-titres-ugc.py` | **≈ 63 crédits** |
| UGC Seedance 2.5, 30 s | Même principe, plus cher, et une fois la voix a dit « sixty minutes » | 210 crédits (brouillon 480p : 90) |
| Vidéo animée en voix off | Voix off, images clés, clips Kling 3.0 (1,25 crédit par seconde sans son), montage ffmpeg, sous-titres | à recalculer |
| Statique | Photo réaliste FLUX 3 ou GPT Image, puis mise en page PIL (Bodoni et DM Sans, couleurs unlined) | 2-3 crédits |
| Voix seule | ElevenLabs v4 : Opal (Botox, 58 ans), Nora (plus grave, 62 ans) | 0,23 crédit par prise |

**Pièges connus :**
- Wan 3.0 n'accepte pas une voix off complète de 30 s : la génération échoue. Avec un extrait de 8 s, il s'en sert seulement pour imiter le timbre et réenregistre le texte. Pour avoir exactement la voix ElevenLabs : laisser Wan générer avec son propre son (bonne synchro des lèvres), puis appliquer un `voice_change` vers la voix voulue. Le minutage est conservé.
- Une génération Wan de 30 s prend 15 à 20 minutes.
- Higgsfield propose parfois un preset hors sujet (« IN THE DARK ») : relancer avec `declined_preset_id`.
- L'IA rend trop net : le filtre iPhone adoucit l'image, ajoute du grain, une légère respiration d'exposition et une recompression façon réseaux sociaux, plus un peu d'écho de pièce sur le son.
- L'actrice applique souvent sur la lèvre plutôt que juste au-dessus : le préciser dans le prompt et vérifier.
- Pour diversifier aux yeux de Meta, chaque UGC a une actrice et un décor différents : cuisine (brune, 63 ans), voiture (cheveux argentés, 62 ans), salle de bain le soir (blonde cendrée, 58 ans).

## C7. Les accroches qui marchent chez les concurrents (Eline Paris, blooe)

| Accroche | Portée | Où on en est |
|---|---|---|
| « Non-smoker with smoker's lines? » | 277k, Royaume-Uni | refaite avec Seedance |
| « Botox for lip lines is dead » | 92k | refaite avec Wan |
| « If the skin above your lip looks like a barcode… » | 84k, en forte hausse | refaite avec Wan |
| « Please be careful with Botox… 400 $ » | 64k | à faire |
| Format animé type Pixar « ended creams » | 75k | à faire |

Toutes reposent sur la même idée : une ride de la lèvre est un creux, pas un manque d'hydratation. « Comme une fissure dans un mur : la crème repeint, il faut combler. »

## C8. Ce qu'on ne met jamais dans une créa
Les faux chiffres de clientes, les fausses notes, les faux dermatologues, les fausses ruptures de stock, les fausses notifications, et une actrice IA qui dit « ça a marché sur moi ». Voir `07-conformite-us.md`.
