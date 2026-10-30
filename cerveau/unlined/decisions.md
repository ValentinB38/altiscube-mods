# unlined : journal des décisions

Chaque décision cite la règle du playbook qui la justifie. On note ensuite le résultat.

## Décisions prises

| Date | Décision | Règle | Résultat attendu | Résultat constaté |
|---|---|---|---|---|
| 27/10 | Garder le prix à 29,90 $ pour mesurer la traction | O2, T7 | Juger le produit avant de toucher au prix | – |
| 28/10 | Ne couper aucune pub sur une seule journée de données | T3, T4 | Éviter de juger sur 323 impressions | – |
| 28/10 | Demander un compte publicitaire US (UTC-4, USD), même BM, pixel et page | M11, M9 | Journée calée sur les US, CPM plus bas qu'avec le compte d'agence | – |
| 28/10 | Produire des UGC Wan (barcode v2, Botox) avec une voix ElevenLabs et un rendu iPhone | C1, C6, C7 | Plus de créas face caméra, à 63 crédits au lieu de 210 | – |
| 28/10 soir | 2e journée rouge (T4) mais CPM en baisse et 29 % d'ajouts au panier pour 0 achat : **on change l'offre plutôt que de couper**. Livraison offerte et email de panier abandonné Shopify activés ce soir, 3e et dernier jour sur l'ancien compte le 29/10 (T3). Si le 29/10 finit encore à 0 vente, on coupe et on attend le compte US. | T3, T4, T6, O5, O6, R1 | Montrer si les frais de port bloquaient le paiement avant la relance US | – |
| 28/10 soir | Livraison offerte activée par Valentin. Moyens de paiement vérifiés (tous présents). Panier tiroir livré (snippet `cart-drawer`) pour remplacer l'envoi direct au paiement. Emails de relance livrés : notification Shopify en Liquid, plus une séquence de 3 emails. | O6, O12, R1 | Moins d'abandons au paiement. À mesurer : paiements commencés et ventes du 29/10 | 28/10 (Shopify, UTC-4) : 3 commandes à 29,90 $ sans port, 7,3 % de conversion (5,7 % le 27/10). Une seule journée : à confirmer (T4) |
| 28/10 | **Lot 2 produit pour la relance US** : 3 UGC (careful Botox, lipstick bleed, gift mom), 4 variantes d'accroche des vidéos animées, 8 statiques en plus. Total : **12 vidéos et 12 statiques**, 187,5 crédits | C1, C6, C9, M5, M16 | Relance avec un adset vidéos et un adset statiques dès J1, environ 24 créas comme Adam | – |
| 29/10 | **Correction du diagnostic du 28/10** : il n'était pas à 0 vente. L'export Meta datait de 17 h (Paris) ; sur la journée US, Shopify compte 3 commandes pour 41 visites (7,3 %). Le paiement fonctionne ; ce qui coûte cher, c'est la visite. Plan inchangé : 3e journée sans rien toucher (T3, T5), lot 2 sur le compte US dès son arrivée (M11). **Un changement :** si l'ancien compte vend encore le 29/10, il tourne jusqu'au lancement US au lieu d'être coupé. | T3, T4, T5, T6, M11 | ROAS calculé sur des journées complètes dès l'export Meta | Export du 28/10 au 29/10 9 h : ROAS 0,42, CPM ≈ 204 €. La clause « il tourne jusqu'au lancement US » est remplacée le 29/10 (ligne suivante) |
| 29/10 | **Lancement US** dès l'arrivée du compte : lot 2 le 30/10 à 00:00 (New York), campagne publiée avant 22 h (Paris) pour laisser à Meta le temps de valider les pubs. L'ancien compte reçoit une date de fin au 30/10 à 05:00 (Paris), pour s'arrêter quand le compte US démarre sans perdre la soirée américaine. J1 à J3 = vendredi à dimanche : on ne touche à rien, même le week-end (M17 sert au scale, pas au test). Bilan le lundi 2/11 sur des journées complètes. **Mis à jour le 29/10 avec l'export du 28-29/10 (ROAS 0,42, CPA 64 €, CPM stable autour de 200 €) :** la date de fin de l'ancien compte s'applique même si le compte US n'arrive pas ce soir ; on n'attend pas en perdant environ 55 € par jour (nos chiffres passent avant la règle). **Remplacé le même jour, voir la ligne suivante.** | M1, M5, M11, M12, M13, M14, T3, T4, T5, T6 | Un premier test propre sur le bon fuseau. Repères : CPM en baisse, ROAS cumulé J1-J3 au-dessus de 1,52 | – |
| 29/10 | **Valentin : l'ancien compte tourne jusqu'à épuisement de son solde prépayé**, qui ne peut pas être transféré en USD sur le compte US. Cet argent est déjà payé, et chaque vente rapporte environ 18 € une fois le produit et les frais payés : il vaut mieux l'utiliser. Remplace la date de fin du 30/10 à 5 h. On ne touche pas à ses pubs (T5, M15 : 0 vente d'AD 7 sur une trentaine de visites reste dans la variance). Les 2 comptes tournent en parallèle sur le même pixel : **le test US se juge sur les chiffres Meta du compte US et sur ses UTM dans Shopify**, pas sur le total Shopify. | M15, M18, T5 | Utiliser le solde sans fausser la lecture du test US | – |
| 30/10 | Campagne US programmée à 00:00 (New York). Au matin (Paris), 0 $ dépensé : on regarde la colonne « Diffusion » (examen des pubs, facturation, date de début) et on ne touche à rien d'autre (T5). J1 = vendredi 30/10, bilan lundi 2/11. | T3, T5, M12 | Une dépense qui démarre dans la journée du 30/10 (New York) | – |
| 28/10 soir | Livraison offerte, panier tiroir et relance en 3 emails **en place** (Valentin). **Le lot 2 attend le compte US.** Le 29/10, on ne touche à rien sur l'ancien compte : son résultat mesurera seulement les changements du site. Le lot 2 part à 00:00, heure du compte US, la nuit qui suit son arrivée. **À tester (aucune règle ne le couvre) :** si le compte n'est toujours pas là vendredi 30/10 au soir, on décide d'un plan B pour ne pas perdre le week-end. | T5, M11, M12, M15, M9, M17 | Un 29/10 lisible (le site seul) et un lot 2 lancé sur le bon fuseau | – |

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
- **Une journée sous 1,52 de ROAS** (1,45 avant la livraison offerte) **:** variance, on attend. **Deux de suite :** on change l'offre ou le prix avant de couper (T4, O5).
- **Augmenter le budget :** +20 % maximum, après 2 jours de suite au-dessus de 1,8 de ROAS, soit l'équilibre + 0,3 (M4).
- **Vers J4-J5 :** ajout de l'adset de statiques (M5) et lecture de la répartition par âge (M6).
