# Cerveau unlined — mode d'emploi pour Claude

Le dossier `cerveau/` est la mémoire de travail de la marque **unlined** (tryunlined.com), un lissant pour les ridules au-dessus des lèvres vendu aux États-Unis.
Le reste du dépôt (fichiers .jar) contient les mods Minecraft du serveur altiscube, sans rapport avec unlined.
Le propriétaire parle français et tutoie : réponds en français, en tutoyant.

## Règle n°1 : toute décision passe par ce cerveau

Avant de recommander une action (pub, budget, prix, offre, page, créa, fournisseur) :

1. Lis `cerveau/unlined/fiche-marque.md` (état actuel) et la fin de `cerveau/unlined/journal.md` (derniers chiffres).
2. Cherche la règle qui s'applique dans `cerveau/playbook/`. Chaque règle cite sa source.
3. Donne ta recommandation **en citant la règle** (ex. « règle T4 : une seule journée négative = variance »).
4. Si aucune règle ne couvre le cas, dis-le, propose une hypothèse et marque-la « à tester ».
5. Une fois la décision prise, ajoute une ligne dans `cerveau/unlined/decisions.md` (date, décision, règle, résultat attendu).

## Ordre de confiance des sources

1. **Nos propres chiffres** (`cerveau/unlined/journal.md`) : ils battent toujours une règle générale.
2. **Formation Evolve** (`cerveau/sources/evolve/`) : à venir.
3. **Adam Citron** (`cerveau/sources/adam-citron/`) : build in public, de 0 à 1 M$/mois aux US, ce qu'il a réellement fait et obtenu.
4. **Conseils ponctuels sur X** (`cerveau/sources/conseils-x/`) : sans chiffres vérifiables, ils confirment une règle mais n'en créent jamais une à eux seuls.
5. Bon sens e-commerce général : à signaler comme tel.

Quand deux sources se contredisent, garde les deux dans le playbook et note le désaccord au lieu de trancher en silence.

## Mise à jour du cerveau

- Nouvelle source (vidéo, thread, module de formation) : un résumé dans `cerveau/sources/<nom>/`, puis les règles nouvelles ou modifiées dans `cerveau/playbook/`, avec renvoi à la source.
- Nouveaux chiffres (export CSV Meta, Shopify) : une ligne par jour dans `cerveau/unlined/journal.md`, avec le ROAS comparé au ROAS de rentabilité.
- Résultat d'un test : on le note sous la règle concernée (« testé chez unlined le JJ/MM : … »).
- **Ce dépôt est public** (choix de Valentin le 28/10/2026) : tout ce qui est écrit ici est lisible par n'importe qui. Aucun secret ici : ni mot de passe, ni accès, ni coordonnées clients.
- **La formation Evolve ne va pas ici** : c'est un contenu payant, et des résumés publiés en public reviendraient à le redistribuer. Il lui faudra un dépôt privé (voir `cerveau/sources/evolve/README.md`). Pour les sources publiques comme Adam Citron, des résumés avec le lien vers la source suffisent.

## Garde-fous permanents (conformité US)

Pas de faux avis, de faux médecins, de faux stocks ou de fausses ruptures, de fausses notifications (règle Meta), de « 200 000 clientes » inventées.
Une offre « free » n'est honnête que si le prix de l'unité est le prix normal (FTC).
Une actrice IA ne dit jamais « ça a marché sur moi » (règle FTC 2024 sur les témoignages).
Détails : `cerveau/playbook/07-conformite-us.md`.

## Plan

- `cerveau/unlined/` : fiche marque, journal des chiffres, journal des décisions
- `cerveau/playbook/` : règles par thème (testing, Meta Ads, créas, offre et page, rétention et outils, sourcing, conformité)
- `cerveau/sources/` : résumés de chaque source, avec chiffres et citations courtes
- `cerveau/outils/` : scripts de production réutilisables (filtre iPhone, sous-titres, voix)
