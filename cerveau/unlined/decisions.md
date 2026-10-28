# unlined : journal des décisions

Chaque décision cite la règle du playbook qui la justifie. On note ensuite le résultat.

## Décisions prises

| Date | Décision | Règle | Résultat attendu | Résultat constaté |
|---|---|---|---|---|
| 27/10 | Garder le prix à 29,90 $ pour mesurer la traction | O2, T7 | Juger le produit avant de toucher au prix | – |
| 28/10 | Ne couper aucune pub sur une seule journée de données | T3, T4 | Éviter de juger sur 323 impressions | – |
| 28/10 | Demander un compte publicitaire US (UTC-4, USD), même BM, pixel et page | M11, M9 | Journée calée sur les US, CPM plus bas qu'avec le compte d'agence | – |
| 28/10 | Produire des UGC Wan (barcode v2, Botox) avec une voix ElevenLabs et un rendu iPhone | C1, C6, C7 | Plus de créas face caméra, à 63 crédits au lieu de 210 | – |
| 28/10 | **Lot 2 produit pour la relance US** : 3 UGC (careful Botox, lipstick bleed, gift mom), 4 variantes d'accroche des vidéos animées, 8 statiques en plus. Total : **12 vidéos et 12 statiques**, 187,5 crédits | C1, C6, C9, M5, M16 | Relance avec un adset vidéos et un adset statiques dès J1, environ 24 créas comme Adam | – |

## Plan du 28/10 (proposé à Valentin, tiré du playbook)

### 1. Tout de suite, sur Shopify (Valentin)
| # | Action | Règles | Pourquoi |
|---|---|---|---|
| 1a | **Livraison offerte** (au minimum sur le BOGO, et en pratique tout le monde le prend puisqu'il est au même prix) | O1, O6, T6 | 3 paiements abandonnés pour 12 visiteurs : le port d'environ 4,60 $ apparaît au paiement. Notre produit est léger. Équilibre estimé : ROAS 1,43 → 1,52, CPA max 24 $ → 20 $. C'est rentable dès +23 % de conversion. |
| 1b | **Relance de paiement abandonné** Klaviyo : 3 emails (1 h, 24 h, 48 h), urgence réelle uniquement | R1 | Les paniers sont déjà perdus. Textes rédigés par Claude. |
| 1c | **Upsell après achat** AfterSell : « +1 tube à 14,90 $, dans le même colis » | O4, O10 | Panier moyen en hausse, aucun frein à la conversion. |
| 1d | **Pourboire au paiement** (réglage Shopify) | O7 | 2 minutes, de l'argent en plus. |
| 1e | Vérifier la campagne : **US 18+, broad, sans âge ni genre ni centre d'intérêt**, toutes les « améliorations » décochées, paramètres UTM en place | M13, M14, M18 | |

### 2. L'ancien compte d'agence
- **Ce soir :** Valentin envoie le CSV du 28/10.
- **CPM toujours au-dessus de 200 € :** le problème vient du compte, pas du produit. On met en pause demain matin et le budget passe sur le compte US (T6, M9).
- **CPM nettement en baisse (sous environ 120 €) :** on laisse le 3e jour se faire (T3).

### 3. Dès que le compte US arrive
- **Campagne :** 1 CBO à 100 $/jour, US 18+, broad, démarrage à 00:00 heure du compte (M1, M12, M13).
- **Adset vidéos :** les 5 vidéos actuelles plus les nouvelles, viser 10 à 15 (C1).
- **Adset statiques, dès le premier jour :** 4 formats × 3 déclinaisons = 12 statiques (M5, M16).
- **Pilotage :** on ne touche à rien pendant 3 jours (T3 à T5), puis +20 % après 2 bonnes journées (M4).

### 4. Les créas (Claude, sur accord pour les crédits)
- **8 nouvelles déclinaisons de statiques**, pour arriver à 3 par format : environ 0-10 crédits (M16).
- **3 nouvelles UGC Wan avec rendu iPhone**, chacune un nouvel angle et une nouvelle actrice : environ 190 crédits (C6, C9).
  - « careful with Botox, 400 $ » (Eline, 64k) ;
  - « mon rouge à lèvres file dans les ridules » ;
  - « ma fille m'a offert ça » (angle cadeau).
- **2 variantes d'accroche des vidéos animées A et B** (texte à l'écran et première phrase de la voix) : environ 5 crédits.

### 5. Avant de monter le budget (en parallèle)
- **Échantillon :** commander un échantillon et vérifier la qualité ainsi que les 5 points S6 (T11).
- **Livraison :** demander à l'agent le coût de la ligne « cosmétique liquide » DDP pour 1 et 2 tubes (S7), puis recalculer le ROAS de rentabilité (T1).
- **Compte publicitaire :** un BM perso propre, avec un 2e administrateur et un moyen de paiement de secours. Les comptes d'agence sautent par vagues (M9).
- **Flows Klaviyo :** suivi de livraison (R10) et avis sans tri (R9).

## Règles de pilotage du nouveau compte (tirées du playbook)
- **J1 à J3 :** on ne touche à rien. On coupe seulement si tout est mauvais en même temps : zéro vente, zéro ajout au panier, CPM déraisonnable (T3).
- **Une journée sous 1,45 de ROAS :** variance, on attend. **Deux de suite :** on change l'offre ou le prix avant de couper (T4, O5).
- **Augmenter le budget :** +20 % maximum, après 2 jours de suite au-dessus de 1,75 de ROAS (M4).
- **Vers J4-J5 :** ajout de l'adset de statiques (M5) et lecture de la répartition par âge (M6).
