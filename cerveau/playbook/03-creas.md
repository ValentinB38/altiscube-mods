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
J41 : à 4 000 $ de pub par jour, la fatigue d'une créa unique devient un vrai risque. Son plan : déclinaisons de la gagnante, angles et sous-avatars radicalement différents, et plus de statiques (rapides à décliner, très bons ROAS en bid cap). (AC J41) (voir `sources/adam-citron/journal-j31-j44.md`)
J57-J60 : « les statiques, c'est souvent du bottom of funnel : ça close beaucoup de ventes » derrière le trafic des vidéos. Au J59, 100 statiques (35 formats × 3 variantes), dont certaines à 3 ou 4 de ROAS dès le lendemain. (voir `sources/adam-citron/journal-j45-j63.md`)

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
| **Photo « vraie » (site, statique, actrice de référence)** | Nano Banana 2.1 en 2k, prompt « A real, unedited iPhone photo, not a photoshoot » + défauts de téléphone, décor encombré, peau réelle, liste de refus (modèles : `outils/prompts-realisme.json`) | 2 crédits |
| Voix seule | ElevenLabs v4 : Opal (Botox, 58 ans), Nora (plus grave, 62 ans) | 0,23 crédit par prise |

**Pièges connus :**
- Wan 3.0 n'accepte pas une voix off complète de 30 s : la génération échoue. Avec un extrait de 8 s, il s'en sert seulement pour imiter le timbre et réenregistre le texte. Pour avoir exactement la voix ElevenLabs : laisser Wan générer avec son propre son (bonne synchro des lèvres), puis appliquer un `voice_change` vers la voix voulue. Le minutage est conservé.
- Une génération Wan de 30 s prend 15 à 20 minutes.
- Higgsfield propose parfois un preset hors sujet (« IN THE DARK ») : relancer avec `declined_preset_id`.
- **Photos : FLUX fait « IA », Nano Banana 2.1 non (verdict de Valentin, 05/11).** Le shooting FLUX de la page Eye Smoother « fait trop IA » ; la photo Nano Banana d'un repas de famille (flash, verres, assiettes entamées, cadrage raté) « ne se remarque pas ». Toutes les photos de personnes du site sont refaites ainsi le 05/11. FLUX reste bon pour les packshots studio. Ce qui fait vrai : dire « real, unedited iPhone photo, not a photoshoot », un défaut d'appareil (grand-angle 24 mm, flou léger, grain, HDR), deux lumières mélangées, un décor vécu et encombré, la peau avec pores et ridules, une expression en pleine phrase, puis la liste de refus. Une image d'une actrice (job Higgsfield) en référence garde le même visage d'une photo à l'autre (étapes 1 à 3). Pour l'appel final du thème, laisser le côté gauche calme : le titre s'y affiche sans fond sur ordinateur.
- L'IA rend trop net : le filtre iPhone adoucit l'image, ajoute du grain, une légère respiration d'exposition et une recompression façon réseaux sociaux, plus un peu d'écho de pièce sur le son.
- L'actrice applique souvent sur la lèvre plutôt que juste au-dessus : le préciser dans le prompt et vérifier. Encore arrivé sur l'UGC filler (lot 3, 02/11), malgré la consigne. **Correctif sans relancer Wan :** un plan de coupe FLUX de la même actrice (son image en référence) qui applique au-dessus de la lèvre, avec un léger zoom, pendant la phrase d'application (environ 3 crédits). Une 2e image « tapote » a raté (doigt en travers des lèvres) : vérifier chaque plan de coupe. **Lot 5 (04/11) : 2 UGC sur 2 appliquent encore sur les lèvres** ; le plan de coupe est devenu une étape normale de la recette. Ce qui marche dans le prompt FLUX : « tip pressed against the skin directly UNDER HER NOSTRILS… one centimeter above the border of the upper lip… clearly visible bare skin between the tip and the lip », et 2 variantes par actrice (une sur deux était bonne). Cadrer le zoom pour que le nez et la lèvre soient tous deux visibles.
- Pour diversifier aux yeux de Meta, chaque UGC a une actrice et un décor différents : cuisine (brune, 63 ans), voiture (cheveux argentés, 62 ans), salle de bain le soir (blonde cendrée, 58 ans), salon (femme noire, 61 ans), coiffeuse (rousse, 57 ans), cuisine avec sac cadeau (fille, 36 ans), bureau à la maison (latina, 59 ans, voix Marisol, lot 3), table de salle à manger (américaine d'origine coréenne, 63 ans, carré argenté, voix Elena, lot 5, angle maquillage), cuisine décorée pour les fêtes (blanche, 66 ans, cheveux bouclés poivre et sel, pull vert, voix Tallulah, lot 5, angle photos des fêtes).
- Voix ElevenLabs utilisées en voice change : Nora (barcode), Opal (Botox is dead), Vera (careful Botox), Helena (lipstick), Ainsley (gift mom, choisie par Valentin pour les pubs animées), Marisol (filler), Elena (maquillage), Tallulah (photos des fêtes). Pour choisir une voix sans l'écouter : hauteur moyenne de l'extrait (Nora et Tallulah autour de 150 Hz, plus mûres ; Elena et Mabel autour de 215 Hz).
- L'IA invente parfois de faux logos sur les objets du décor (un sac cadeau marqué « Con »). Il faut les repérer à la relecture et les effacer avec `outils/effacer-logo.py`, une reconstruction OpenCV.
- Rejeter les images de référence dont l'étiquette du tube est en miroir.
- **Produit personnalisé (plaid de lecture, 11/11) : donner en référence le rendu exact du configurateur** (le dessin à plat et la photo portée du site), et écrire dans le prompt le prénom exact et « elegant italic serif font exactly like image 1 ». Nano Banana 2.1 a alors reproduit le dessin et les prénoms justes (Sophie, Martine, Léa) sur 14 images sur 14. Sans la précision « italique », 2 visuels sur 4 avaient le prénom en lettres droites. En animation (Wan 3.0, Kling 3.0, 5 s), le prénom reste lisible, mais la police peut dériver en fin de clip : garder les 3 premières secondes. Pour la démo du configurateur, filmer la vraie fiche dans Playwright avec une capture d'écran par images (CDP screencast, 1080 px de large), pas avec l'enregistrement vidéo intégré, qui est flou.
- **Variantes d'accroche gratuites** pour les vidéos animées : seul le bandeau du début change (`hook_variant.py` dans le dossier de production). Elles comptent comme des créas en plus pour Meta.
- **Variantes de statiques gratuites** : même format, texte ou angle différent (M16).
- **Accroche « médaillon » (lot 3, d'après le format gagnant d'Eline)** : pendant les 6 à 8 premières secondes, un gros plan macro des rides (FLUX, environ 3 crédits), un feutre rouge qui entoure la zone, l'actrice dans un médaillon rond en bas et un bandeau en haut ; puis la vidéo d'origine en plein écran, avec le son et les sous-titres d'origine. Script : `outils/accroche-medaillon.py` (environ 6 minutes de rendu).
- **Accroche « garantie »** : un bandeau « Smoother-looking lip lines in about 60 seconds. Or your money back » sur les 3,6 premières secondes de la vidéo sous-titrée. Gratuit (`outils/accroche-garantie.py`).

**Testé chez unlined le 28-29/10 (ancien compte) :** les 2 UGC Wan à rendu iPhone et voix ElevenLabs, ajoutées le 28/10, font les 3 ventes de la période : « Botox is dead » (salle de bain) 2 ventes et ROAS 1,64, « barcode » v2 (voiture) 1 vente et CTR 8,8 %. L'UGC Seedance non-smoker : ≈ 115 € sans vente depuis le 27/10. Petit échantillon : un premier signal pour la recette Wan et pour les angles Botox et barcode, à confirmer sur le compte US (C9). (NOUS) **Confirmé en partie sur le compte US (02-03/11) :** l'UGC « Botox is dead » (VIDEO 4) prend le plus de budget et fait 5 ventes en 2 jours (02-03/11) ; l'UGC « barcode » v2 (VIDEO 6) fait 1 vente au J1 avec 21 % de CTR ; la vidéo animée B « Before you book Botox » et la statique 1b « Your lipstick isn't the problem » font une vente chacune.

## C7. Les accroches qui marchent chez les concurrents (Eline Paris, blooe)

| Accroche | Portée | Où on en est |
|---|---|---|
| « Non-smoker with smoker's lines? » | 277k, Royaume-Uni | refaite avec Seedance |
| « Botox for lip lines is dead » | 92k | refaite avec Wan |
| « If the skin above your lip looks like a barcode… » | 84k, en forte hausse | refaite avec Wan |
| « Please be careful with Botox… 400 $ » | 64k | faite avec Wan (lot 2, careful-botox) |
| Format animé type Pixar « ended creams » | 75k | proche : nos vidéos animées A (lot 2) |

**Désaccord (04/11) :** Andras (YouTube) estime que reprendre les concepts d'un gros annonceur sur la même audience fait payer un CPM plus cher au copieur ; Adam Griffin, que les mots « Botox », « filler » peuvent nous faire entrer dans des enchères plus chères. À tester : nos propres angles (maquillage, cadeau) face aux angles repris d'Eline, sur le CPM et sur le coût par vente (voir `sources/youtube/`).

**Reprendre un format gagnant, c'est aussi reprendre son montage (NOUS, 06/11, Maison Ouate) :** la première version de nos vidéos d'essayage reprenait l'accroche et l'angle de la pub n°1 de domelyah.com, mais pas son montage. La comparaison image par image a montré 3 écarts : (1) le cadrage : chez lui, chaque couleur a un gros plan tenu à la main où la matière remplit l'écran, puis un plan miroir ; nous n'avions que des plans larges ; (2) le rythme : une coupe toutes les ~1,4 s chez lui, ~2,2 s chez nous ; (3) les légendes : les siennes sont empilées au milieu de l'écran, notre appel à l'action était dans le bas, que Reels recouvre (nom de la page, texte, bouton). Avant de livrer une reprise, on extrait 8 à 15 images de la pub d'origine et on compare cadrage, rythme et place des légendes, pas seulement le texte. Résultat à lire au verdict du 14/11.

Toutes reposent sur la même idée : une ride de la lèvre est un creux, pas un manque d'hydratation. « Comme une fissure dans un mur : la crème repeint, il faut combler. »

**Veille Eline Paris US du 02/11 (TrendTrack, pubs actives triées par hausse de portée sur 7 jours) :**
- **Volume :** 475 pubs actives vers elineparis-us.com, diffusées depuis plusieurs pages : « Women's Wellness Journal » (511 pubs actives), « Scults », « Hairel ». Ciblage US, Canada, Royaume-Uni, Australie, Nouvelle-Zélande, parfois bien plus. Bouton « Learn more » partout. Pages d'arrivée : fiche produit, variantes de fiche (« -listicle », « -lip-lines ») et un advertorial (`/pages/creams-lip-lines`). La portée mesurée vient surtout du Royaume-Uni : les chiffres US sont sous-estimés.
- **Les gagnantes installées (60 à 71 jours, en tête de page) :** « Non-smoker with smoker's lines? Here's the part nobody explains » (n°1, 130k), « Botox for lip lines is dead », « barcode », « Please be careful… Botox », « tensing polymers ended creams ». Leur format : une femme qui parle dans un médaillon, sur un gros plan des rides où l'on dessine au feutre rouge.
- **Les nouvelles qui montent :**

| Accroche | Signal | Pour nous |
|---|---|---|
| « 20 Years of Lip Line GONE in 3 minutes OR MONEY BACK » (gros plan) | +23k de portée en 7 jours, 8 jours d'âge, vers un listicle | **La garantie dans l'accroche** : on peut, la nôtre est réelle (90 jours). « Gone » est trop fort pour un cosmétique : on garde « look smoother ». |
| « This is how $400 filler around my mouth ruined my life » (médaillon + flèche rouge) | n°1 de la page « Scults » | **Nouvel angle : les limites du filler** (gonfle la lèvre, s'en va en quelques mois). À faire en explication, pas en faux témoignage d'une actrice IA. |
| Image « NOT A CREAM. It fills the lines above your lip in about 3 minutes », avec un fer à repasser sur les rides | en hausse, vers l'advertorial | **Une métaphore visuelle forte.** On fait la nôtre (par exemple un enduit qui comble une fissure), sans copier la leur. |
| Image illustrée avant/après « Not a Cream. Lip Lines FILLED In 3 Minutes », avec « Individual results may vary » | en hausse | Un format simple à décliner en statique. |

- **À ne jamais copier (07) :** une voix qui se présente comme praticienne (« patients come to see me for Botox ») ; « tested on 107 women » et « 7,837 women rated 4.8 », invérifiables pour nous ; « 1 SOLD EVERY 10 MINUTES » ; « Buy 1 Get 1 Free Today Only » sur une offre permanente ; des faux témoignages à la première personne ; des pages au nom de « journal », qui font passer une pub pour un média. (NOUS, 02/11)

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
6. **Son workflow de statiques (J59) :** sur TrendTrack, le classement des meilleures statiques des grosses marques DTC ; chaque format retenu est envoyé à Claude Code, qui le réplique pour sa marque avec ses assets. **À reprendre pour unlined** (lot 4), sans jamais copier un logo, un texte ou une fausse preuve sociale. (voir `sources/adam-citron/journal-j45-j63.md`)
   - **Appliqué le 03/11 (lot 4, 13 statiques, 21,5 crédits) :** veille TrendTrack des statiques beauté les plus diffusées aux US auprès des femmes mûres (Frøya Organics, Prime Prometics, Rumi, Cheoni, Dore & Rose, Féline : 90 à 350 jours de diffusion). Formats repris : gros titre condensé + produit + sceau de garantie ; note manuscrite dans un carnet (une astuce, pas un témoignage) ; titre manuscrit sur photo d'ambiance ; lettre texte seule ; titre éditorial + gros plan ; selfie brut sans texte ; promo BOGO franche. **Écartés car interdits chez nous (07) :** « 1 sold every 8 seconds », « Doctor recommended », « Last call, free BOGO ends midnight » sur une offre permanente, logos de presse sans preuve, avant/après en photo. Polices ajoutées : Anton (titres condensés), Caveat (manuscrit). (NOUS)
7. Recrutement des monteurs : test payant de 48 h (une vidéo concurrente à reproduire, une vidéo IA + b-roll). Les tests rendus maîtrisent le b-roll, beaucoup moins la face caméra IA réaliste (J56-J62).
(AC vidéo J30)

## C8. Ce qu'on ne met jamais dans une créa
Les faux chiffres de clientes, les fausses notes, les faux dermatologues, les fausses ruptures de stock, les fausses notifications, et une actrice IA qui dit « ça a marché sur moi ». Voir `07-conformite-us.md`.
