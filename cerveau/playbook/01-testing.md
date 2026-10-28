# Playbook 01 : tester un produit, une offre ou un angle

Sources : AC = Adam Citron (J1 à J10, vidéos J1 et J7), NOUS = nos chiffres unlined.

## T1. Calculer le ROAS de rentabilité avant de lancer
- ROAS de rentabilité = CA par commande ÷ (CA par commande − coût produit − livraison − frais de paiement).
- CPA max = CA par commande − tous ces coûts.
- Le recalculer à chaque changement de prix, d'offre ou de fournisseur.
- Adam : 1,65 pour le produit 1, 1,8 pour le produit 2, qui est plus cher mais laisse plus de marge par vente. (AC J1, J8)
- unlined : voir `unlined/fiche-marque.md`, encore à confirmer avec le vrai coût fournisseur.

## T2. Pendant un test, l'objectif est l'équilibre, pas le bénéfice
Être à l'équilibre, c'est réussir : le pixel apprend sans rien coûter. Adam a fini sa semaine 1 à 5 % de marge et l'appelle « exactement la semaine que je voulais ». (AC J1, J5, vidéo J7)

## T3. Tester au moins 3 jours
Couper avant 24 h seulement si tout est mauvais en même temps : zéro vente, zéro ajout au panier, CPM déraisonnable. Sinon, on attend 3 jours. (AC vidéo J1)
Même conseil de @MurpazECOM le 28/10 : « give it 3 days before touching anything ». Son repère : « 1 sale on day 1 is a good sign » ; unlined a fait 2 ventes au J1 (voir `sources/conseils-x/`).

## T4. Une journée négative, c'est de la variance. Deux de suite, c'est une tendance.
À 100-150 $/jour, deux ou trois ventes de plus ou de moins font basculer la journée. Après une journée rouge, on ne touche à rien. Après deux journées rouges consécutives, on agit : nouvelle offre, nouveau prix, ou on coupe. (AC J4, J5)
Même sur un produit qui marche, le CA peut faire −50 % ou +100 % d'un jour à l'autre sans aucun changement. **On juge la tendance sur 3 jours minimum, 7 dans l'idéal, et à la semaine.** (AC vidéos J14, J30)
J12-J13 : ses deux produits s'inversent chaque jour (P1 à 2,4 et P2 à 1,6, puis l'inverse), et le taux de conversion aussi (J13 : beaucoup de paniers abandonnés, « juste de la variance » ; J14 : record). Lissé sur plusieurs jours, il reste positif. (AC J12-J14)

## T5. On ne touche à rien pendant les premiers jours
Ni le prix, ni le budget, ni les créas. Adam s'est contredit trois fois. La seule erreur nette : monter le budget de 50 % après **une seule** bonne journée (produit 2 : ROAS 3 puis 0,56). (AC J2, J3, J10)

## T6. Grille de diagnostic

| Ce qu'on voit | Ce que ça veut dire | Action |
|---|---|---|
| CPM très élevé, CTR correct, quelques ventes | Pixel ou compte neuf, Meta cherche | Attendre 2-3 jours ; le CPM d'Adam est passé de 100 à 55 $ en 6 jours |
| Bon CTR, CPC bas, beaucoup de visites, peu de ventes | La page, le prix ou l'offre ne convertit pas | Changer l'offre ou le prix, pas les créas (AC J10) |
| CTR faible, CPC élevé | Les créas n'accrochent pas | Nouvelles accroches, nouveaux angles |
| Paiements commencés mais abandonnés | Frein au paiement (frais de port, moyen de paiement, confiance) | Vérifier le paiement, relance par email (R1) |
| Ventes concentrées sur une tranche d'âge | Meta a trouvé l'avatar | Adapter la page et les créas (M6) |

Repères de conversion d'Adam (J13) : P1, 20 % d'ajouts au panier et 7 % de conversion ; P2, 8 % et 2 %. unlined le 28/10 : 29 % d'ajouts au panier et 0 % de conversion, sur 14 visites. (AC J13, NOUS)

## T7. Le prix se décide sur le bénéfice, pas sur le ROAS
Baisser le prix fait monter la conversion et le ROAS, mais peut faire baisser le bénéfice : jour 2 d'Adam, ROAS 1,83 mais 7 % de marge, contre ROAS 1,7 et 11 % la veille. On compare toujours le bénéfice en dollars. (AC J2)

## T8. Le volume de tests fait le résultat
Le KPI hebdomadaire d'Adam : le nombre de produits testés. Pour viser un ROAS de 4-5, il en teste beaucoup. (AC vidéo J1, J9)
**Adapté à unlined (marque mono-produit) :** notre équivalent est le nombre d'angles, d'accroches et d'offres testés chaque semaine. Un deuxième produit beauté viendra plus tard, pour la même cliente.

## T9. Patience quand c'est à l'équilibre
Des amis d'Adam sont restés à l'équilibre un mois avant que le produit « parte en exponentiel ». Tant qu'on est à l'équilibre, on laisse tourner. (AC vidéo J1, J5)

## T10. Objectif de marge : 15 % minimum avant coûts fixes
Adam vise 15 % de marge, 20-25 % dans l'idéal, avant coûts fixes. Au J14 : « tant que je suis au-dessus de 15 % de marge, je peux continuer à scaler » (J11 à J15 : 21 % de marge en moyenne). Il accepte environ 10 % sur une courte période pour nourrir le pixel plus vite. Son premier mois : 15 % avant coûts fixes, environ 10 % net. Repère des coûts fixes : environ 2 450 $ le premier mois (outils IA, apps, Triple Whale, thème). (AC vidéos J14, J30)

## T11. Vérifier la qualité du produit avant de grossir
Son produit 2 a été coupé pour un défaut découvert par les plaintes clientes environ 2 semaines après les premières ventes, à cause du délai de livraison. Scaler trop vite pendant ces 2 semaines, c'est risquer des remboursements, des rétrofacturations et un Shopify Payments qui saute. **Commander et tester un échantillon avant de monter le budget.** (AC vidéo J30)
8lab (28/10) dit pareil avec sa formule « (branding + marketing + pricing) × produit » : si le produit vaut zéro, tout tombe à zéro (voir `sources/conseils-x/8lab-2026-10-28.md`).

## T12. Le budget de départ
Un test, c'est environ 100 $/jour pendant 3 jours, soit 300 $. Adam recommande au moins 3 000 $ « confortables » pour se lancer aux US. (AC vidéo J30)
