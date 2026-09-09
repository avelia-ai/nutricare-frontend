# -*- coding: utf-8 -*-
import sys

path = "app.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

def esc(s):
    """Echappe backslash puis apostrophe pour une chaine JS entre quotes simples."""
    return s.replace("\\", "\\\\").replace("'", "\\'")

def arr(tips):
    """Construit un tableau JS ['a','b','c'] a partir d'une liste de strings python."""
    return "[" + ", ".join("'" + esc(t) + "'" for t in tips) + "]"

replacements = []  # (old, new, expected_count, label)

# ---------------------------------------------------------------
# Ajout du helper pickVariant (rotation par jour) juste apres la
# definition de pushAdvice, UNIQUEMENT dans le bloc renderPersonalSummary
# (ancre unique = ligne suivie du commentaire "donnees du jour")
# ---------------------------------------------------------------
old_anchor = """    var advicePool = [];
    function pushAdvice(txt, weight) { advicePool.push({ txt: txt, weight: weight || 1 }); }

    // Conseils bases sur les donnees du jour (priorite haute si renseignees)"""

new_anchor = """    var advicePool = [];
    function pushAdvice(txt, weight) { advicePool.push({ txt: txt, weight: weight || 1 }); }
    var _dayIdx = Math.floor(Date.now() / 86400000);
    function pickVariant(arr) { return arr[_dayIdx % arr.length]; }

    // Conseils bases sur les donnees du jour (priorite haute si renseignees)"""

replacements.append((old_anchor, new_anchor, 1, "Ajout helper pickVariant (rotation quotidienne)"))

# ---------------------------------------------------------------
# 1. Stress eleve aujourd'hui (weight 5)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlStress !== null && _tlStress >= 7) pushAdvice('ton stress du jour est élevé (' + _tlStress + '/10), essaie une séance de cohérence cardiaque de 2 minutes', 5);",
    "if (_tlStress !== null && _tlStress >= 7) pushAdvice('ton stress du jour est élevé (' + _tlStress + '/10), ' + pickVariant(" + arr([
        "essaie une séance de cohérence cardiaque de 2 minutes (6 respirations par minute)",
        "sors marcher 10 minutes dehors, la lumière naturelle fait baisser le cortisol",
        "pose ton téléphone 15 minutes et accorde-toi une vraie pause sans écran",
        "essaie la technique 4-7-8 : inspire 4s, retiens 7s, expire 8s, répète 4 fois",
        "prends une douche tiède, la baisse de température corporelle calme le système nerveux",
    ]) + "), 5);",
    1, "Variantes: stress eleve aujourd'hui"
))

# ---------------------------------------------------------------
# 2. Energie basse aujourd'hui (weight 5)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlEnergy !== null && _tlEnergy <= 4) pushAdvice('ton énergie du jour est basse (' + _tlEnergy + '/10), vérifie ton sommeil et ton hydratation avant tout', 5);",
    "if (_tlEnergy !== null && _tlEnergy <= 4) pushAdvice('ton énergie du jour est basse (' + _tlEnergy + '/10), ' + pickVariant(" + arr([
        "vérifie ton sommeil et ton hydratation avant tout",
        "bois un grand verre d'eau et prends une collation avec des fruits secs",
        "fais 5 minutes d'étirements ou une courte marche pour relancer la circulation",
        "évite le sucre rapide et privilégie une source de protéines pour stabiliser ton énergie",
        "aère la pièce ou sors 5 minutes, le manque d'air peut accentuer la fatigue",
    ]) + "), 5);",
    1, "Variantes: energie basse aujourd'hui"
))

# ---------------------------------------------------------------
# 3. Sommeil insuffisant aujourd'hui (weight 4)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlSleep !== null && _tlSleep < 7) pushAdvice('tu as dormi ' + _tlSleep + 'h cette nuit, essaie de te coucher 30 minutes plus tôt ce soir', 4);",
    "if (_tlSleep !== null && _tlSleep < 7) pushAdvice('tu as dormi ' + _tlSleep + 'h cette nuit, ' + pickVariant(" + arr([
        "essaie de te coucher 30 minutes plus tôt ce soir",
        "coupe les écrans 30 minutes avant le coucher pour t'endormir plus vite",
        "évite la caféine après 14h pour ne pas perturber ton endormissement",
        "prévois une routine calme (lecture, étirements légers) avant de dormir",
        "évite les repas lourds ce soir, la digestion peut retarder l'endormissement",
    ]) + "), 4);",
    1, "Variantes: sommeil insuffisant aujourd'hui"
))

# ---------------------------------------------------------------
# 4. Hydratation insuffisante (weight 4)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlHydra !== null && _tlHydra < _tlHydraTarget) pushAdvice('tu as bu ' + _tlHydra + 'L aujourd\\'hui sur un objectif de ' + _tlHydraTarget + 'L, pense à boire un peu plus', 4);",
    "if (_tlHydra !== null && _tlHydra < _tlHydraTarget) pushAdvice('tu as bu ' + _tlHydra + 'L aujourd\\'hui sur un objectif de ' + _tlHydraTarget + 'L, ' + pickVariant(" + arr([
        "pense à boire un peu plus",
        "garde une bouteille d'eau visible sur ton bureau, ça aide à y penser",
        "ajoute une tranche de citron ou de concombre pour varier le goût et boire plus facilement",
        "programme une alarme toutes les 2h pour boire un verre d'eau",
        "mange des aliments riches en eau (concombre, pastèque, tomate) pour compléter",
    ]) + "), 4);",
    1, "Variantes: hydratation insuffisante"
))

# ---------------------------------------------------------------
# 5. Activite faible aujourd'hui (weight 3)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlActivity !== null && _tlActivity < 20) pushAdvice('tu as bougé ' + _tlActivity + ' min aujourd\\'hui, même une courte marche peut faire la différence', 3);",
    "if (_tlActivity !== null && _tlActivity < 20) pushAdvice('tu as bougé ' + _tlActivity + ' min aujourd\\'hui, ' + pickVariant(" + arr([
        "même une courte marche peut faire la différence",
        "monte les escaliers plutôt que l'ascenseur aujourd'hui, ça compte",
        "10 minutes de marche après le repas améliorent aussi la digestion",
        "programme un rappel pour te lever et bouger toutes les heures",
        "danse sur 2-3 chansons, c'est une activité cardio qui ne demande aucun materiel",
    ]) + "), 3);",
    1, "Variantes: activite faible aujourd'hui"
))

# ---------------------------------------------------------------
# 6. IMC surpoids (weight 2)
# ---------------------------------------------------------------
replacements.append((
    "if (imc >= 25) pushAdvice('ton IMC indique un ' + (imc >= 30 ? 'excès de poids notable' : 'léger surpoids') + ', privilégie les protéines maigres et les légumes à chaque repas', 2);",
    "if (imc >= 25) pushAdvice('ton IMC indique un ' + (imc >= 30 ? 'excès de poids notable' : 'léger surpoids') + ', ' + pickVariant(" + arr([
        "privilégie les protéines maigres et les légumes à chaque repas",
        "limite les aliments ultra-transformés et privilégie le fait maison",
        "mange lentement et arrête-toi à environ 80% de satiété",
        "ajoute 30 minutes de marche quotidienne à ta routine",
    ]) + "), 2);",
    1, "Variantes: IMC surpoids"
))

# ---------------------------------------------------------------
# 7. IMC sous la normale (weight 2)
# ---------------------------------------------------------------
replacements.append((
    "else if (imc < 18.5) pushAdvice('ton IMC est en dessous de la normale, veille à ne pas sauter de repas et privilégie les apports caloriques de qualité', 2);",
    "else if (imc < 18.5) pushAdvice('ton IMC est en dessous de la normale, ' + pickVariant(" + arr([
        "veille à ne pas sauter de repas et privilégie les apports caloriques de qualité",
        "ajoute des collations riches en bonnes graisses (oléagineux, avocat) entre les repas",
        "privilégie 4 à 5 prises alimentaires dans la journée plutôt que 3 grands repas",
        "ajoute une source de protéines à chaque collation pour soutenir ta masse musculaire",
    ]) + "), 2);",
    1, "Variantes: IMC sous la normale"
))

# ---------------------------------------------------------------
# 8. Reveils nocturnes (weight 2)
# ---------------------------------------------------------------
replacements.append((
    "if (profile.sommeil_reveils_nocturnes === 'souvent') pushAdvice('tes réveils nocturnes fréquents peuvent impacter ta récupération : évite les écrans et les repas lourds avant le coucher, et limite la caféine après 14h', 2);",
    "if (profile.sommeil_reveils_nocturnes === 'souvent') pushAdvice(pickVariant(" + arr([
        "tes réveils nocturnes fréquents peuvent impacter ta récupération : évite les écrans et les repas lourds avant le coucher, et limite la caféine après 14h",
        "pour limiter tes réveils nocturnes, garde ta chambre fraîche (18-19°C) et évite l'alcool en soirée qui fragmente le sommeil",
        "contre les réveils nocturnes, essaie une respiration lente pendant 5 minutes avant de dormir pour calmer ton système nerveux",
        "tes réveils nocturnes peuvent venir d'une chambre trop lumineuse : essaie un masque de sommeil ou des rideaux occultants",
    ]) + "), 2);",
    1, "Variantes: reveils nocturnes"
))

# ---------------------------------------------------------------
# 9. Sport pratique (weight 1)
# ---------------------------------------------------------------
replacements.append((
    "if (profile.sport_pratique) pushAdvice('continue ta pratique de ' + profile.sport_pratique + ', la régularité est la clé des résultats : vise 2 à 3 séances par semaine et laisse au moins un jour de repos entre deux efforts intenses', 1);",
    "if (profile.sport_pratique) pushAdvice('continue ta pratique de ' + profile.sport_pratique + ', ' + pickVariant(" + arr([
        "la régularité est la clé des résultats : vise 2 à 3 séances par semaine et laisse au moins un jour de repos entre deux efforts intenses",
        "pense à varier l'intensité de tes séances pour progresser sans te blesser",
        "n'oublie pas de bien t'échauffer 5 à 10 minutes avant chaque séance",
        "un carnet de suivi de tes performances t'aidera à voir tes progrès sur la durée",
    ]) + "), 1);",
    1, "Variantes: sport pratique"
))

# ---------------------------------------------------------------
# 10. Perte de poids - ecart objectif connu (weight 3)
# ---------------------------------------------------------------
replacements.append((
    "if (_ecartObj > 0) pushAdvice('il te reste ' + _ecartObj + ' kg pour atteindre ton objectif, mise sur des protéines à chaque repas pour rester rassasié(e)', 3);",
    "if (_ecartObj > 0) pushAdvice('il te reste ' + _ecartObj + ' kg pour atteindre ton objectif, ' + pickVariant(" + arr([
        "mise sur des protéines à chaque repas pour rester rassasié(e)",
        "privilégie les fibres (légumes, légumineuses) qui prolongent la sensation de satiété",
        "évite de sauter de repas, ça favorise les grignotages compensatoires",
        "pèse-toi une fois par semaine, à heure fixe, pour suivre ta tendance sans stress",
    ]) + "), 3);",
    1, "Variantes: perte de poids (ecart objectif connu)"
))

# ---------------------------------------------------------------
# 11. Perte de poids - generic sans objectif chiffre (weight 2)
# ---------------------------------------------------------------
replacements.append((
    "pushAdvice('pour ton objectif de perte de poids, privilégie les protéines et les fibres qui rassasient durablement', 2);",
    "pushAdvice(pickVariant(" + arr([
        "pour ton objectif de perte de poids, privilégie les protéines et les fibres qui rassasient durablement",
        "pour ton objectif de perte de poids, mange dans une assiette plus petite : ça aide naturellement à réduire les portions",
        "pour ton objectif de perte de poids, priorise le sommeil : un manque de sommeil dérègle les hormones de la faim",
        "pour ton objectif de perte de poids, bois un verre d'eau avant chaque repas, ça aide à mieux réguler l'appétit",
    ]) + "), 2);",
    1, "Variantes: perte de poids (generique)"
))

# ---------------------------------------------------------------
# 12. Perte de poids - activite < 30 (weight 2)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlActivity !== null && _tlActivity < 30) pushAdvice('pour progresser vers ta perte de poids, vise 30 à 45 min de marche rapide ou de vélo aujourd\\'hui (zone cardio 60-70% de ta FC max) : c\\'est la fourchette la plus efficace pour mobiliser les graisses sans épuiser ta récupération', 2);",
    "if (_tlActivity !== null && _tlActivity < 30) pushAdvice(pickVariant(" + arr([
        "pour progresser vers ta perte de poids, vise 30 à 45 min de marche rapide ou de vélo aujourd'hui (zone cardio 60-70% de ta FC max) : c'est la fourchette la plus efficace pour mobiliser les graisses sans épuiser ta récupération",
        "pour progresser vers ta perte de poids, ajoute 2 séances de renforcement musculaire par semaine : plus de muscle veut dire plus de calories brûlées au repos",
        "pour progresser vers ta perte de poids, essaie 15 minutes de HIIT aujourd'hui : très efficace pour la dépense calorique post-effort",
        "pour progresser vers ta perte de poids, marche systématiquement après chaque repas 10 minutes : ça aide aussi à la digestion",
    ]) + "), 2);",
    1, "Variantes: perte de poids (activite faible)"
))

# ---------------------------------------------------------------
# 13. Masse - apport calorique (weight 3)
# ---------------------------------------------------------------
replacements.append((
    "pushAdvice('pour ta prise de masse, vise un surplus de 250 à 400 kcal par jour et 1,8 à 2,2g de protéines par kg de poids de corps, réparties en 4 prises espacées de 3-4h', 3);",
    "pushAdvice(pickVariant(" + arr([
        "pour ta prise de masse, vise un surplus de 250 à 400 kcal par jour et 1,8 à 2,2g de protéines par kg de poids de corps, réparties en 4 prises espacées de 3-4h",
        "pour ta prise de masse, ajoute une collation riche (flocons d'avoine, beurre de cacahuète, banane) après ta séance pour optimiser la récupération musculaire",
        "pour ta prise de masse, ne néglige pas les glucides : ils sont essentiels pour avoir l'énergie de bien performer à chaque séance",
        "pour ta prise de masse, vise 7 à 9h de sommeil par nuit : c'est pendant le sommeil que le muscle se reconstruit vraiment",
    ]) + "), 3);",
    1, "Variantes: masse (apport calorique)"
))

# ---------------------------------------------------------------
# 14. Masse - seance de renforcement (weight 2)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlActivity !== null && _tlActivity < 20) pushAdvice('pense à ta séance de renforcement musculaire aujourd\\'hui : 3 à 4 séries de 8-12 répétitions par groupe musculaire pour maximiser l\\'hypertrophie', 2);",
    "if (_tlActivity !== null && _tlActivity < 20) pushAdvice(pickVariant(" + arr([
        "pense à ta séance de renforcement musculaire aujourd'hui : 3 à 4 séries de 8-12 répétitions par groupe musculaire pour maximiser l'hypertrophie",
        "pense à augmenter progressivement les charges d'une séance à l'autre pour continuer à progresser",
        "pense à bien travailler chaque groupe musculaire au moins une fois par semaine pour un développement équilibré",
        "pense à laisser 48h de repos avant de retravailler le même groupe musculaire",
    ]) + "), 2);",
    1, "Variantes: masse (seance)"
))

# ---------------------------------------------------------------
# 15. Sommeil - objectif actif (weight 3)
# ---------------------------------------------------------------
# (entree "Sommeil - objectif actif" fusionnee plus bas avec le else correspondant, voir old_sommeil_pair)

# ---------------------------------------------------------------
# 16. Sommeil - objectif ok (weight 1)
# ---------------------------------------------------------------
replacements.append((
    """    if (_tlSleep !== null && _tlSleep < 7.5) pushAdvice(pickVariant([""" + "",
    "PLACEHOLDER_UNUSED",
    0, "IGNORE_THIS_ENTRY"
))
replacements.pop()  # retire l'entree bidon ci-dessus, on la remplace proprement ci-dessous

old_sommeil_pair = """    if (objectifs.indexOf('sommeil') > -1) {
      if (_tlSleep !== null && _tlSleep < 7.5) pushAdvice('ton objectif est de mieux dormir : coupe les écrans 45 min avant le coucher, baisse la température de ta chambre à 18-19 degrés, et vise un coucher à heure fixe pour stabiliser ton rythme circadien', 3);
      else pushAdvice('ta routine de sommeil porte ses fruits : garde ces horaires reguliers, y compris le week-end, pour consolider ton cycle circadien', 1);
    }"""

new_sommeil_pair = """    if (objectifs.indexOf('sommeil') > -1) {
      if (_tlSleep !== null && _tlSleep < 7.5) pushAdvice(pickVariant(""" + arr([
        "ton objectif est de mieux dormir : coupe les écrans 45 min avant le coucher, baisse la température de ta chambre à 18-19 degrés, et vise un coucher à heure fixe pour stabiliser ton rythme circadien",
        "ton objectif est de mieux dormir : essaie une tisane apaisante (camomille, verveine) 30 minutes avant le coucher",
        "ton objectif est de mieux dormir : limite les siestes en journée à 20 minutes maximum pour ne pas perturber ton endormissement le soir",
        "ton objectif est de mieux dormir : expose-toi à la lumière naturelle le matin, ça aide à recaler ton horloge biologique",
    ]) + """), 3);
      else pushAdvice(pickVariant(""" + arr([
        "ta routine de sommeil porte ses fruits : garde ces horaires reguliers, y compris le week-end, pour consolider ton cycle circadien",
        "ton sommeil est sur la bonne voie : continue a eviter les ecrans juste avant de dormir",
        "bravo pour ta regularite de sommeil, c'est l'un des facteurs les plus importants pour ta sante globale",
    ]) + """), 1);
    }"""

replacements.append((old_sommeil_pair, new_sommeil_pair, 1, "Variantes: sommeil (if+else combines, ancre unique bloc3)"))

# ---------------------------------------------------------------
# 17. Stress - objectif actif (weight 3)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlStress !== null && _tlStress >= 5) pushAdvice('pour réduire ton stress, pratique 5 minutes de cohérence cardiaque (6 respirations par minute, inspire 5s / expire 5s) : ça fait baisser le cortisol en moins de 3 minutes', 3);",
    "if (_tlStress !== null && _tlStress >= 5) pushAdvice(pickVariant(" + arr([
        "pour réduire ton stress, pratique 5 minutes de cohérence cardiaque (6 respirations par minute, inspire 5s / expire 5s) : ça fait baisser le cortisol en moins de 3 minutes",
        "pour réduire ton stress, essaie d'identifier une seule tâche prioritaire aujourd'hui plutôt que de tout vouloir gérer en même temps",
        "pour réduire ton stress, accorde-toi une vraie pause déjeuner loin de ton écran",
        "pour réduire ton stress, note 3 choses positives de ta journée avant de dormir, ça aide à relativiser",
    ]) + "), 3);",
    1, "Variantes: stress (objectif actif)"
))

# ---------------------------------------------------------------
# 18. Stress - objectif ok (weight 1)
# ---------------------------------------------------------------
replacements.append((
    "else pushAdvice('ton niveau de stress semble maîtrisé : garde tes rituels de détente en place, ce sont eux qui font la différence sur la durée', 1);",
    "else pushAdvice(pickVariant(" + arr([
        "ton niveau de stress semble maîtrisé : garde tes rituels de détente en place, ce sont eux qui font la différence sur la durée",
        "ton stress est bien géré en ce moment : c'est le bon moment pour ancrer ces bonnes habitudes durablement",
        "ta gestion du stress porte ses fruits : continue à t'accorder ces moments de pause",
    ]) + "), 1);",
    1, "Variantes: stress (objectif ok)"
))

# ---------------------------------------------------------------
# 19. Energie - objectif actif (weight 3)
# ---------------------------------------------------------------
replacements.append((
    "if (_tlEnergy !== null && _tlEnergy <= 6) pushAdvice('pour booster ton énergie, bois 500ml d\\'eau dès le réveil et opte pour une collation à index glycémique bas (amandes, flocons d\\'avoine, fruit entier) plutôt qu\\'un produit sucré qui provoque un coup de barre 1h après', 3);",
    "if (_tlEnergy !== null && _tlEnergy <= 6) pushAdvice(pickVariant(" + arr([
        "pour booster ton énergie, bois 500ml d'eau dès le réveil et opte pour une collation à index glycémique bas (amandes, flocons d'avoine, fruit entier) plutôt qu'un produit sucré qui provoque un coup de barre 1h après",
        "pour booster ton énergie, expose-toi à la lumière naturelle dès le matin, ça aide à réveiller ton organisme",
        "pour booster ton énergie, fractionne tes repas en évitant les portions trop copieuses qui donnent un coup de fatigue digestive",
        "pour booster ton énergie, vérifie ton apport en fer et en vitamine B12, des carences fréquentes en cas de fatigue chronique",
    ]) + "), 3);",
    1, "Variantes: energie (objectif actif)"
))

# ---------------------------------------------------------------
# 20. Energie - objectif ok (weight 1)
# ---------------------------------------------------------------
replacements.append((
    "else pushAdvice('ton énergie est bonne aujourd\\'hui : profites-en pour caler ta séance de sport la plus exigeante de la semaine', 1);",
    "else pushAdvice(pickVariant(" + arr([
        "ton énergie est bonne aujourd'hui : profites-en pour caler ta séance de sport la plus exigeante de la semaine",
        "ton énergie est au rendez-vous : c'est le bon moment pour t'attaquer à une tâche qui demande de la concentration",
        "ton niveau d'énergie est solide aujourd'hui : garde ces bonnes habitudes qui te réussissent",
    ]) + "), 1);",
    1, "Variantes: energie (objectif ok)"
))

# ---------------------------------------------------------------
# 21. Performance sportive (weight 2)
# ---------------------------------------------------------------
replacements.append((
    "pushAdvice('pour ta performance sportive, hydrate-toi avec 500ml d\\'eau dans les 2h avant l\\'effort et prends un repas riche en glucides complexes (riz, patate douce, pâtes) 2-3h avant pour maximiser tes réserves de glycogène', 2);",
    "pushAdvice(pickVariant(" + arr([
        "pour ta performance sportive, hydrate-toi avec 500ml d'eau dans les 2h avant l'effort et prends un repas riche en glucides complexes (riz, patate douce, pâtes) 2-3h avant pour maximiser tes réserves de glycogène",
        "pour ta performance sportive, priorise 7 à 9h de sommeil : c'est un des facteurs les plus sous-estimés de la performance",
        "pour ta performance sportive, prévois une collation glucides+protéines dans les 30 minutes après l'effort pour optimiser la récupération",
        "pour ta performance sportive, n'oublie pas les électrolytes (sodium, potassium) lors des efforts longs ou par forte chaleur",
    ]) + "), 2);",
    1, "Variantes: performance sportive"
))

# ---------------------------------------------------------------
# 22. Reequilibrage alimentaire (weight 2)
# ---------------------------------------------------------------
replacements.append((
    "pushAdvice('pour ton rééquilibrage alimentaire, construis chaque assiette avec la règle moitié-quart-quart : moitié légumes, un quart protéines, un quart féculents complets, plus une source de bonnes graisses (huile d\\'olive, oléagineux)', 2);",
    "pushAdvice(pickVariant(" + arr([
        "pour ton rééquilibrage alimentaire, construis chaque assiette avec la règle moitié-quart-quart : moitié légumes, un quart protéines, un quart féculents complets, plus une source de bonnes graisses (huile d'olive, oléagineux)",
        "pour ton rééquilibrage alimentaire, essaie de cuisiner un nouveau légume de saison cette semaine pour varier tes apports",
        "pour ton rééquilibrage alimentaire, limite les boissons sucrées : elles apportent des calories sans réel effet de satiété",
        "pour ton rééquilibrage alimentaire, prépare tes repas à l'avance sur 2-3 jours pour éviter les choix impulsifs quand tu es pressé(e)",
    ]) + "), 2);",
    1, "Variantes: reequilibrage alimentaire"
))

# ---------------------------------------------------------------
# 23. Maintien du poids (weight 1)
# ---------------------------------------------------------------
replacements.append((
    "pushAdvice('pour maintenir ton poids, garde 150 à 200 min d\\'activité modérée par semaine et pèse-toi une fois par semaine pour repérer toute dérive avant qu\\'elle ne s\\'installe', 1);",
    "pushAdvice(pickVariant(" + arr([
        "pour maintenir ton poids, garde 150 à 200 min d'activité modérée par semaine et pèse-toi une fois par semaine pour repérer toute dérive avant qu'elle ne s'installe",
        "pour maintenir ton poids, continue à privilégier des repas faits maison, plus faciles à équilibrer que la restauration rapide",
        "pour maintenir ton poids, garde une routine d'activité physique stable : c'est la régularité qui fait la différence sur le long terme",
    ]) + "), 1);",
    1, "Variantes: maintien du poids"
))

# ---------------------------------------------------------------
# 24. Forme / fallback (weight 1, x2 occurrences identiques)
# ---------------------------------------------------------------
replacements.append((
    "pushAdvice('continue comme ça, tes indicateurs sont dans de bonnes tendances', 1);",
    "pushAdvice(pickVariant(" + arr([
        "continue comme ça, tes indicateurs sont dans de bonnes tendances",
        "tout est dans le vert aujourd'hui : profites-en pour prendre un moment pour toi",
        "tes indicateurs sont stables : c'est le bon moment pour te fixer un petit défi bonus cette semaine",
        "rien à signaler d'alarmant aujourd'hui : garde le cap sur tes bonnes habitudes",
    ]) + "), 1);",
    2, "Variantes: fallback / forme (2 occurrences)"
))

# ---------------------------------------------------------------
# Verification puis application
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
print("OK: systeme de variantes quotidiennes applique avec succes.")
