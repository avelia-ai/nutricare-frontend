# -*- coding: utf-8 -*-
with open('routes/menus.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1) Recuperer le parametre rythme_repas depuis la requete
old1 = """  if (req.body.objectif_nutritionnel) profile.objectif_nutritionnel = req.body.objectif_nutritionnel;
  const targetCaloriesReq = req.body.target_calories ? parseInt(req.body.target_calories) : null;"""

new1 = """  if (req.body.objectif_nutritionnel) profile.objectif_nutritionnel = req.body.objectif_nutritionnel;
  const targetCaloriesReq = req.body.target_calories ? parseInt(req.body.target_calories) : null;
  const rythmeRepas = req.body.rythme_repas || '';"""

count1 = content.count(old1)
print("Bloc 1 (recuperation rythme_repas) trouve " + str(count1) + " fois")
assert count1 == 1
content = content.replace(old1, new1)

# 2) Construire la note d'instructions selon le rythme choisi
old2 = """  const systemPromptDay = 'Tu es un nutritionniste expert. Reponds TOUJOURS et UNIQUEMENT avec du JSON brut valide, sans texte avant ou apres, sans markdown.';"""

new2 = """  const rythmeLabelsDay = {
    '3_repas_classiques': 'RYTHME 3 REPAS CLASSIQUES: garnis normalement petit_dejeuner, dejeuner, diner. Pour collation, propose une collation legere standard (fruit, oleagineux, yaourt).',
    '5_6_petits_repas': 'RYTHME 5-6 PETITS REPAS: repartis les calories en petites portions plus frequentes. Reduis les portions de petit_dejeuner, dejeuner et diner par rapport a une portion classique, et fais de la collation un vrai repas a part entiere (pas juste un snack) pour compenser. Dans le champ conseil_nutritionnel, precise qu il est recommande de fractionner encore ce plan en 1-2 collations supplementaires dans la journee.',
    'jeune_16_8': 'RYTHME JEUNE INTERMITTENT 16:8 (fenetre alimentaire de 8h, ex 12h-20h): NE PAS remplir petit_dejeuner (mets nom="" ingredients=[] calories=0 pour ce champ). Concentre tous les apports caloriques du jour sur dejeuner, collation et diner, dans la fenetre alimentaire. Dans conseil_nutritionnel, rappelle la fenetre horaire recommandee.',
    'jeune_18_6': 'RYTHME JEUNE INTERMITTENT 18:6 (fenetre alimentaire de 6h, ex 13h-19h): NE PAS remplir petit_dejeuner (mets nom="" ingredients=[] calories=0 pour ce champ). Concentre tous les apports caloriques du jour sur dejeuner et diner rapproches, collation optionnelle et legere si besoin dans la fenetre. Dans conseil_nutritionnel, rappelle la fenetre horaire recommandee.',
    'jeune_20_4': 'RYTHME JEUNE INTERMITTENT 20:4 (fenetre alimentaire de 4h, ex 15h-19h): NE PAS remplir petit_dejeuner ni collation (mets nom="" ingredients=[] calories=0 pour ces champs). Concentre la quasi-totalite des calories du jour sur dejeuner et diner rapproches dans la courte fenetre alimentaire. Dans conseil_nutritionnel, rappelle la fenetre horaire recommandee et insiste sur l importance de bien s hydrater hors fenetre.',
    'omad': 'RYTHME OMAD (1 repas par jour): NE PAS remplir petit_dejeuner, collation ni diner (mets nom="" ingredients=[] calories=0 pour ces 3 champs). Concentre l integralite des calories et nutriments du jour dans le champ dejeuner, qui doit etre un repas copieux et complet nutritionnellement equilibre. Dans conseil_nutritionnel, donne des conseils de vigilance pour ce rythme exigeant.',
    'jeune_5_2': 'RYTHME JEUNE 5:2: pour ce jour precis, applique un jour NORMAL avec les 4 repas remplis normalement (le jeune 5:2 s applique a 2 jours non consecutifs par semaine geres separement par l utilisateur, pas ce jour-ci). Dans conseil_nutritionnel, rappelle que ce jour est un jour d alimentation normale dans le cadre du 5:2.',
  };
  const rythmeNoteDay = rythmeRepas && rythmeLabelsDay[rythmeRepas] ? ('\\n\\nRYTHME DE REPAS DEMANDE PAR L UTILISATEUR:\\n' + rythmeLabelsDay[rythmeRepas]) : '';

  const systemPromptDay = 'Tu es un nutritionniste expert. Reponds TOUJOURS et UNIQUEMENT avec du JSON brut valide, sans texte avant ou apres, sans markdown.';"""

count2 = content.count(old2)
print("Bloc 2 (definition rythmeNoteDay) trouve " + str(count2) + " fois")
assert count2 == 1
content = content.replace(old2, new2)

# 3) Injecter la note dans le prompt final envoye a l IA
old3 = """  const promptDay = `Genere le menu d UNE SEULE journee (${jourDemande}) en JSON strictement valide. ${langNoteDay}${objNoteDay}${activeFiltersTextDay}"""

new3 = """  const promptDay = `Genere le menu d UNE SEULE journee (${jourDemande}) en JSON strictement valide. ${langNoteDay}${objNoteDay}${activeFiltersTextDay}${rythmeNoteDay}"""

count3 = content.count(old3)
print("Bloc 3 (injection dans promptDay) trouve " + str(count3) + " fois")
assert count3 == 1
content = content.replace(old3, new3)

with open('routes/menus.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: rythme_repas integre dans le prompt de generation du menu du jour")
