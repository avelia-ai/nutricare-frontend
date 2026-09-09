# -*- coding: utf-8 -*-
import sys

path = "app.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = []  # (old, new, expected_count, label)

# ---------------------------------------------------------------
# FIX PROGRESS BAR: objectif energie affiche "10/10" comme fin
# alors que la cible reelle est 7/10 (incoherent avec le texte
# "vise 7/10 ou plus")
# ---------------------------------------------------------------
replacements.append((
    '''      objLine = "Objectif : ameliorer ton energie (vise 7/10 ou plus)";
      progressWrap.style.display = 'block';
      document.getElementById('summaryProgressStart').textContent = '0/10';
      document.getElementById('summaryProgressEnd').textContent = '10/10';''',
    '''      objLine = "Objectif : ameliorer ton energie (vise 7/10 ou plus)";
      progressWrap.style.display = 'block';
      document.getElementById('summaryProgressStart').textContent = '0/10';
      document.getElementById('summaryProgressEnd').textContent = '7/10';''',
    1, "FIX barre progression energie (10/10 -> 7/10)"
))

# ---------------------------------------------------------------
# CONSEILS PREMIUM - version avec \u00e9 echappe (blocs 1 et 2, x2 chacun)
# ---------------------------------------------------------------
pairs_escaped = [
    (
        "pour progresser vers ta perte de poids, vise au moins 30 min d\\'activit\\u00e9 aujourd\\'hui",
        "pour progresser vers ta perte de poids, vise 30 a 45 min de marche rapide ou de velo aujourd\\'hui (zone cardio 60-70% de ta FC max) : c\\'est la fourchette la plus efficace pour mobiliser les graisses sans epuiser ta recuperation",
        2, "perte_poids activite (escaped)"
    ),
    (
        "pour ta prise de masse, assure-toi d\\'avoir un apport calorique suffisant et des prot\\u00e9ines \\u00e0 chaque repas",
        "pour ta prise de masse, vise un surplus de 250 a 400 kcal par jour et 1,8 a 2,2g de proteines par kg de poids de corps, reparties en 4 prises espacees de 3-4h",
        2, "masse apport (escaped)"
    ),
    (
        "pense \\u00e0 ta s\\u00e9ance de renforcement musculaire aujourd\\'hui pour soutenir ta prise de masse",
        "pense a ta seance de renforcement musculaire aujourd\\'hui : 3 a 4 series de 8-12 repetitions par groupe musculaire pour maximiser l\\'hypertrophie",
        2, "masse seance (escaped)"
    ),
    (
        "ton objectif est de mieux dormir : essaie une routine calme sans \\u00e9cran 30 min avant le coucher ce soir",
        "ton objectif est de mieux dormir : coupe les ecrans 45 min avant le coucher, baisse la temperature de ta chambre a 18-19 degres, et vise un coucher a heure fixe pour stabiliser ton rythme circadien",
        2, "sommeil actif (escaped)"
    ),
    (
        "continue ta routine de sommeil, elle porte ses fruits sur ton objectif de mieux dormir",
        "ta routine de sommeil porte ses fruits : garde ces horaires reguliers, y compris le week-end, pour consolider ton cycle circadien",
        3, "sommeil ok (toutes occurrences, pas d'accent)"
    ),
    (
        "pour r\\u00e9duire ton stress, prends 5 minutes aujourd\\'hui pour un exercice de respiration ou de m\\u00e9ditation",
        "pour reduire ton stress, pratique 5 minutes de coherence cardiaque (6 respirations par minute, inspire 5s / expire 5s) : ca fait baisser le cortisol en moins de 3 minutes",
        2, "stress actif (escaped)"
    ),
    (
        "ton niveau de stress semble ma\\u00eetris\\u00e9, continue tes rituels de d\\u00e9tente",
        "ton niveau de stress semble maitrise : garde tes rituels de detente en place, ce sont eux qui font la difference sur la duree",
        2, "stress ok (escaped)"
    ),
    (
        "pour booster ton \\u00e9nergie, v\\u00e9rifie ton hydratation et privil\\u00e9gie des collations riches en fibres plut\\u00f4t qu\\'en sucre rapide",
        "pour booster ton energie, bois 500ml d\\'eau des le reveil et opte pour une collation a index glycemique bas (amandes, flocons d\\'avoine, fruit entier) plutot qu\\'un produit sucre qui provoque un coup de barre 1h apres",
        2, "energie basse (escaped)"
    ),
    (
        "ton \\u00e9nergie est bonne aujourd\\'hui, continue sur cette lanc\\u00e9e",
        "ton energie est bonne aujourd\\'hui : profites-en pour caler ta seance de sport la plus exigeante de la semaine",
        2, "energie ok (escaped)"
    ),
    (
        "pour ta performance sportive, veille \\u00e0 bien t\\'hydrater et \\u00e0 manger des glucides complexes avant l\\'effort",
        "pour ta performance sportive, hydrate-toi avec 500ml d\\'eau dans les 2h avant l\\'effort et prends un repas riche en glucides complexes (riz, patate douce, pates) 2-3h avant pour maximiser tes reserves de glycogene",
        2, "performance (escaped)"
    ),
    (
        "pour ton r\\u00e9\\u00e9quilibrage alimentaire, vise des repas vari\\u00e9s avec l\\u00e9gumes, prot\\u00e9ines et bonnes graisses \\u00e0 chaque repas",
        "pour ton reequilibrage alimentaire, construis chaque assiette avec la regle moitie-quart-quart : moitie legumes, un quart proteines, un quart feculents complets, plus une source de bonnes graisses (huile d\\'olive, oleagineux)",
        2, "reequilibrage (escaped)"
    ),
    (
        "pour maintenir ton poids, garde une activit\\u00e9 r\\u00e9guli\\u00e8re et une alimentation \\u00e9quilibr\\u00e9e comme tu le fais d\\u00e9j\\u00e0",
        "pour maintenir ton poids, garde 150 a 200 min d\\'activite moderee par semaine et pese-toi une fois par semaine pour reperer toute derive avant qu\\'elle ne s\\'installe",
        2, "maintien (escaped)"
    ),
]

for old, new, cnt, label in pairs_escaped:
    replacements.append((old, new, cnt, label))

# ---------------------------------------------------------------
# CONSEILS PREMIUM - version accents litteraux utf-8 (bloc 3, x1 chacun)
# ---------------------------------------------------------------
pairs_utf8 = [
    (
        "pour progresser vers ta perte de poids, vise au moins 30 min d\\'activité aujourd\\'hui",
        "pour progresser vers ta perte de poids, vise 30 à 45 min de marche rapide ou de vélo aujourd\\'hui (zone cardio 60-70% de ta FC max) : c\\'est la fourchette la plus efficace pour mobiliser les graisses sans épuiser ta récupération",
        1, "perte_poids activite (utf8)"
    ),
    (
        "pour ta prise de masse, assure-toi d\\'avoir un apport calorique suffisant et des protéines à chaque repas",
        "pour ta prise de masse, vise un surplus de 250 à 400 kcal par jour et 1,8 à 2,2g de protéines par kg de poids de corps, réparties en 4 prises espacées de 3-4h",
        1, "masse apport (utf8)"
    ),
    (
        "pense à ta séance de renforcement musculaire aujourd\\'hui pour soutenir ta prise de masse",
        "pense à ta séance de renforcement musculaire aujourd\\'hui : 3 à 4 séries de 8-12 répétitions par groupe musculaire pour maximiser l\\'hypertrophie",
        1, "masse seance (utf8)"
    ),
    (
        "ton objectif est de mieux dormir : essaie une routine calme sans écran 30 min avant le coucher ce soir",
        "ton objectif est de mieux dormir : coupe les écrans 45 min avant le coucher, baisse la température de ta chambre à 18-19 degrés, et vise un coucher à heure fixe pour stabiliser ton rythme circadien",
        1, "sommeil actif (utf8)"
    ),
    (
        "pour réduire ton stress, prends 5 minutes aujourd\\'hui pour un exercice de respiration ou de méditation",
        "pour réduire ton stress, pratique 5 minutes de cohérence cardiaque (6 respirations par minute, inspire 5s / expire 5s) : ça fait baisser le cortisol en moins de 3 minutes",
        1, "stress actif (utf8)"
    ),
    (
        "ton niveau de stress semble maîtrisé, continue tes rituels de détente",
        "ton niveau de stress semble maîtrisé : garde tes rituels de détente en place, ce sont eux qui font la différence sur la durée",
        1, "stress ok (utf8)"
    ),
    (
        "pour booster ton énergie, vérifie ton hydratation et privilégie des collations riches en fibres plutôt qu\\'en sucre rapide",
        "pour booster ton énergie, bois 500ml d\\'eau dès le réveil et opte pour une collation à index glycémique bas (amandes, flocons d\\'avoine, fruit entier) plutôt qu\\'un produit sucré qui provoque un coup de barre 1h après",
        1, "energie basse (utf8)"
    ),
    (
        "ton énergie est bonne aujourd\\'hui, continue sur cette lancée",
        "ton énergie est bonne aujourd\\'hui : profites-en pour caler ta séance de sport la plus exigeante de la semaine",
        1, "energie ok (utf8)"
    ),
    (
        "pour ta performance sportive, veille à bien t\\'hydrater et à manger des glucides complexes avant l\\'effort",
        "pour ta performance sportive, hydrate-toi avec 500ml d\\'eau dans les 2h avant l\\'effort et prends un repas riche en glucides complexes (riz, patate douce, pâtes) 2-3h avant pour maximiser tes réserves de glycogène",
        1, "performance (utf8)"
    ),
    (
        "pour ton rééquilibrage alimentaire, vise des repas variés avec légumes, protéines et bonnes graisses à chaque repas",
        "pour ton rééquilibrage alimentaire, construis chaque assiette avec la règle moitié-quart-quart : moitié légumes, un quart protéines, un quart féculents complets, plus une source de bonnes graisses (huile d\'olive, oléagineux)",
        1, "reequilibrage (utf8)"
    ),
    (
        "pour maintenir ton poids, garde une activité régulière et une alimentation équilibrée comme tu le fais déjà",
        "pour maintenir ton poids, garde 150 à 200 min d\'activité modérée par semaine et pèse-toi une fois par semaine pour repérer toute dérive avant qu\'elle ne s\'installe",
        1, "maintien (utf8)"
    ),
]

for old, new, cnt, label in pairs_utf8:
    replacements.append((old, new, cnt, label))

# ---------------------------------------------------------------
# Application
# ---------------------------------------------------------------
all_ok = True
for old, new, expected, label in replacements:
    actual = content.count(old)
    status = "OK" if actual == expected else "MISMATCH"
    if actual != expected:
        all_ok = False
    print("[" + status + "] " + label + ": attendu=" + str(expected) + " trouve=" + str(actual))

if not all_ok:
    print("")
    print("ABANDON: au moins un remplacement ne correspond pas au nombre attendu.")
    print("Aucune modification n'a ete ecrite sur disque.")
    sys.exit(1)

for old, new, expected, label in replacements:
    content = content.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("")
print("OK: toutes les corrections ont ete appliquees avec succes.")
