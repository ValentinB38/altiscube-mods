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
J12 à J15 : après 12-13 jours sur les 25 vidéos du lancement, il ajoute de nouveaux formats et angles : 37 créas au J14 (27 vidéos, 10 images), puis 29 pour le P1 et 25 pour le P2 au J15. Les nouvelles vendent dès le premier jour (3 des 23 commandes du P1). « Plus je rajoute de créas dans les CBO, plus les performances montent. » (AC J12-J15)
J26 à J30 : plus d'une semaine sans nouvelles créas sur le P1, alors il les fait passer avant le lancement du P4. Nouvel adset de 15 vidéos (J29), puis 40 vidéos et 20 statiques (J30). « Une seule créa fait la majorité des performances » : pour 5 000 à 10 000 $/jour, il faut d'autres gagnantes, donc d'autres angles et concepts (C9). (AC J26-J30)

## C5. Le signal qu'une créa est bonne
Le CPM baisse et le CTR tient. Chez Adam : CTR stable autour de 4 %, CPM divisé par 2 en une semaine. (AC vidéo J7)
@MurpazECOM (28/10) : « make ads that facebook will like », sans dire comment. Notre lecture, à tester : une pub que les gens regardent et cliquent coûte moins cher à diffuser, et c'est ce signal qui le montre (voir `sources/conseils-x/`).

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
- Pour diversifier aux yeux de Meta, chaque UGC a une actrice et un décor différents : cuisine (brune, 63 ans), voiture (cheveux argentés, 62 ans), salle de bain le soir (blonde cendrée, 58 ans), salon (femme noire, 61 ans), coiffeuse (rousse, 57 ans), cuisine avec sac cadeau (fille, 36 ans).
- Voix ElevenLabs utilisées en voice change : Nora (barcode), Opal (Botox is dead), Vera (careful Botox), Helena (lipstick), Ainsley (gift mom, choisie par Valentin pour les pubs animées).
- L'IA invente parfois de faux logos sur les objets du décor (un sac cadeau marqué « Con »). Il faut les repérer à la relecture et les effacer avec `outils/effacer-logo.py`, une reconstruction OpenCV.
- Rejeter les images de référence dont l'étiquette du tube est en miroir.
- **Variantes d'accroche gratuites** pour les vidéos animées : seul le bandeau du début change (`hook_variant.py` dans le dossier de production). Elles comptent comme des créas en plus pour Meta.
- **Variantes de statiques gratuites** : même format, texte ou angle différent (M16).

**Testé chez unlined le 28-29/10 (ancien compte) :** les 2 UGC Wan à rendu iPhone et voix ElevenLabs, ajoutées le 28/10, font les 3 ventes de la période : « Botox is dead » (salle de bain) 2 ventes et ROAS 1,64, « barcode » v2 (voiture) 1 vente et CTR 8,8 %. L'UGC Seedance non-smoker : ≈ 115 € sans vente depuis le 27/10. Petit échantillon : un premier signal pour la recette Wan et pour les angles Botox et barcode, à confirmer sur le compte US (C9). (NOUS)

## C7. Les accroches qui marchent chez les concurrents (Eline Paris, blooe)

| Accroche | Portée | Où on en est |
|---|---|---|
| « Non-smoker with smoker's lines? » | 277k, Royaume-Uni | refaite avec Seedance |
| « Botox for lip lines is dead » | 92k | refaite avec Wan |
| « If the skin above your lip looks like a barcode… » | 84k, en forte hausse | refaite avec Wan |
| « Please be careful with Botox… 400 $ » | 64k | à faire |
| Format animé type Pixar « ended creams » | 75k | à faire |

Toutes reposent sur la même idée : une ride de la lèvre est un creux, pas un manque d'hydratation. « Comme une fissure dans un mur : la crème repeint, il faut combler. »

8lab (28/10) : parler à l'émotion derrière l'achat (« une femme qui achète une robe veut avant tout se sentir plus belle et plus confiante »). Nos accroches expliquent surtout le mécanisme. **À tester :** l'émotion, se sentir de nouveau à l'aise avec son rouge à lèvres, de près et en photo (voir `sources/conseils-x/8lab-2026-10-28.md`).

## C9. Des angles d'abord, puis des déclinaisons des gagnants
- Au début, on ajoute des créas pour **tester des angles et des concepts**, pas « contre la fatigue » : à 500-1 000 $/jour, la fatigue des créas n'existe pas.
- Quand un angle gagne, on le décline : autres formats, variantes, sous-cibles (« pour ta mère », « non-fumeuse »…).
- À 10 k$/jour, Adam produit des lots de 30 à 100 créas, environ 100 par semaine. Une seule créa fait 40 % de ses ventes : il en faut toujours d'autres en préparation.
(AC vidéos J30, J45)
8lab (28/10) confirme : le marché est saturé, pas le produit ; lister un maximum d'angles et d'avatars (exemple Fincut : un angle niché pour les hommes de 35-45 ans, élargi ensuite). **Pistes à tester :** la mère de la mariée, les photos de famille des fêtes (voir `sources/conseils-x/8lab-2026-10-28.md`).

## C10. La chaîne de production d'Adam (à reprendre pour unlined)
1. Un document « avatar » et un document « voice of customer » (les mots exacts des clientes), construits à partir d'avis Amazon, Reddit et TikTok.
2. Claude propose des angles, **validés par un humain**, puis écrit le script (accroche, corps, appel à l'action).
3. Voix ElevenLabs, puis montage à partir d'une banque de plans. Chez nous, les plans sont uniquement générés par IA ou tournés : jamais ceux d'un concurrent.
4. Raisonner en système : itérer sur 2-3 vidéos jusqu'à un rendu propre, puis en faire un workflow qui en sort des dizaines (Claude Code branché à Seedance et Google Omni). Une centaine de pubs en 2 jours, seul. (AC J12, J15)
5. Au J29, son temps devient le goulot (10 à 14 h par jour) : il prévoit d'embaucher un monteur vidéo. (AC J29)
(AC vidéo J30)

## C8. Ce qu'on ne met jamais dans une créa
Les faux chiffres de clientes, les fausses notes, les faux dermatologues, les fausses ruptures de stock, les fausses notifications, et une actrice IA qui dit « ça a marché sur moi ». Voir `07-conformite-us.md`.
