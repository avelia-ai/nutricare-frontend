# -*- coding: utf-8 -*-
with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

old1 = """    var adviceParts = [];
    if (imc >= 25) adviceParts.push('ton IMC indique un ' + (imc >= 30 ? 'exces de poids notable' : 'leger surpoids') + ', privilegie les proteines maigres et les legumes a chaque repas');
    else if (imc < 18.5) adviceParts.push('ton IMC est en dessous de la normale, veille a ne pas sauter de repas et privilegie les apports caloriques de qualite');
    if (profile.stress_actuel && profile.stress_actuel >= 7) adviceParts.push('ton niveau de stress est eleve, essaie une seance de coherence cardiaque de 2 minutes aujourd\\'hui');
    if (profile.energie_actuelle && profile.energie_actuelle <= 4) adviceParts.push('ton energie est basse en ce moment, verifie ton sommeil et ton hydratation avant tout');
    if (profile.sommeil_heures_actuel && profile.sommeil_heures_actuel < 7) adviceParts.push('tu dors moins de 7h, essaie de te coucher 30 minutes plus tot ce soir');
    if (profile.sommeil_reveils_nocturnes === 'souvent') adviceParts.push('tes reveils nocturnes frequents peuvent impacter ta recuperation, evite les ecrans avant le coucher');
    if (profile.sport_pratique) adviceParts.push('continue ta pratique de ' + profile.sport_pratique + ', la regularite est la cle des resultats');
    if (!adviceParts.length && objectifs.indexOf('rester en forme') === -1) adviceParts.push('continue comme ca, tes indicateurs sont dans de bonnes tendances');"""

new1 = """    var _todayLogAdvice = window._pcTodayHealthLog || null;
    var _tlEnergy = (_todayLogAdvice && _todayLogAdvice.energy_level != null) ? _todayLogAdvice.energy_level : null;
    var _tlSleep = (_todayLogAdvice && _todayLogAdvice.sleep_hours != null) ? _todayLogAdvice.sleep_hours : null;
    var _tlStress = (_todayLogAdvice && _todayLogAdvice.stress_level != null) ? _todayLogAdvice.stress_level : null;
    var _tlHydra = (_todayLogAdvice && _todayLogAdvice.hydration_liters != null) ? _todayLogAdvice.hydration_liters : null;
    var _tlActivity = (_todayLogAdvice && _todayLogAdvice.activity_minutes != null) ? _todayLogAdvice.activity_minutes : null;
    var _tlHydraTarget = Math.round(poids * 0.033 * 10) / 10;

    var advicePool = [];
    function pushAdvice(txt, weight) { advicePool.push({ txt: txt, weight: weight || 1 }); }

    // Conseils bases sur les donnees du jour (priorite haute si renseignees)
    if (_tlStress !== null && _tlStress >= 7) pushAdvice('ton stress du jour est eleve (' + _tlStress + '/10), essaie une seance de coherence cardiaque de 2 minutes', 5);
    if (_tlEnergy !== null && _tlEnergy <= 4) pushAdvice('ton energie du jour est basse (' + _tlEnergy + '/10), verifie ton sommeil et ton hydratation avant tout', 5);
    if (_tlSleep !== null && _tlSleep < 7) pushAdvice('tu as dormi ' + _tlSleep + 'h cette nuit, essaie de te coucher 30 minutes plus tot ce soir', 4);
    if (_tlHydra !== null && _tlHydra < _tlHydraTarget) pushAdvice('tu as bu ' + _tlHydra + 'L aujourd\\'hui sur un objectif de ' + _tlHydraTarget + 'L, pense a boire un peu plus', 4);
    if (_tlActivity !== null && _tlActivity < 20) pushAdvice('tu as bouge ' + _tlActivity + ' min aujourd\\'hui, meme une courte marche peut faire la difference', 3);

    // Conseils bases sur l IMC
    if (imc >= 25) pushAdvice('ton IMC indique un ' + (imc >= 30 ? 'exces de poids notable' : 'leger surpoids') + ', privilegie les proteines maigres et les legumes a chaque repas', 2);
    else if (imc < 18.5) pushAdvice('ton IMC est en dessous de la normale, veille a ne pas sauter de repas et privilegie les apports caloriques de qualite', 2);

    // Conseils bases sur le profil statique (onboarding, si pas deja couverts par les donnees du jour)
    if (_tlStress === null && profile.stress_actuel && profile.stress_actuel >= 7) pushAdvice('ton niveau de stress est eleve, essaie une seance de coherence cardiaque de 2 minutes aujourd\\'hui', 2);
    if (_tlEnergy === null && profile.energie_actuelle && profile.energie_actuelle <= 4) pushAdvice('ton energie est basse en ce moment, verifie ton sommeil et ton hydratation avant tout', 2);
    if (_tlSleep === null && profile.sommeil_heures_actuel && profile.sommeil_heures_actuel < 7) pushAdvice('tu dors moins de 7h en general, essaie de te coucher 30 minutes plus tot ce soir', 2);
    if (profile.sommeil_reveils_nocturnes === 'souvent') pushAdvice('tes reveils nocturnes frequents peuvent impacter ta recuperation, evite les ecrans avant le coucher', 2);
    if (profile.sport_pratique) pushAdvice('continue ta pratique de ' + profile.sport_pratique + ', la regularite est la cle des resultats', 1);

    // Conseils personnalises selon les objectifs choisis a l onboarding
    if (objectifs.indexOf('perte_poids') > -1) {
      if (profile.poids_objectif && poids) {
        var _ecartObj = Math.round((poids - profile.poids_objectif) * 10) / 10;
        if (_ecartObj > 0) pushAdvice('il te reste ' + _ecartObj + ' kg pour atteindre ton objectif, mise sur des proteines a chaque repas pour rester rassasie(e)', 3);
      } else {
        pushAdvice('pour ton objectif de perte de poids, privilegie les proteines et les fibres qui rassasient durablement', 2);
      }
      if (_tlActivity !== null && _tlActivity < 30) pushAdvice('pour progresser vers ta perte de poids, vise au moins 30 min d activite aujourd\\'hui', 2);
    }
    if (objectifs.indexOf('masse') > -1) {
      pushAdvice('pour ta prise de masse, assure-toi d avoir un apport calorique suffisant et des proteines a chaque repas', 3);
      if (_tlActivity !== null && _tlActivity < 20) pushAdvice('pense a ta seance de renforcement musculaire aujourd\\'hui pour soutenir ta prise de masse', 2);
    }
    if (objectifs.indexOf('sommeil') > -1) {
      if (_tlSleep !== null && _tlSleep < 7.5) pushAdvice('ton objectif est de mieux dormir : essaie une routine calme sans ecran 30 min avant le coucher ce soir', 3);
      else pushAdvice('continue ta routine de sommeil, elle porte ses fruits sur ton objectif de mieux dormir', 1);
    }
    if (objectifs.indexOf('stress') > -1) {
      if (_tlStress !== null && _tlStress >= 5) pushAdvice('pour reduire ton stress, prends 5 minutes aujourd\\'hui pour un exercice de respiration ou de meditation', 3);
      else pushAdvice('ton niveau de stress semble maitrise, continue tes rituels de detente', 1);
    }
    if (objectifs.indexOf('energie') > -1) {
      if (_tlEnergy !== null && _tlEnergy <= 6) pushAdvice('pour booster ton energie, verifie ton hydratation et privilegie des collations riches en fibres plutot qu en sucre rapide', 3);
      else pushAdvice('ton energie est bonne aujourd\\'hui, continue sur cette lancee', 1);
    }
    if (objectifs.indexOf('performance') > -1) {
      pushAdvice('pour ta performance sportive, veille a bien t hydrater et a manger des glucides complexes avant l effort', 2);
    }
    if (objectifs.indexOf('r\\u00e9\\u00e9quilibrage') > -1) {
      pushAdvice('pour ton reequilibrage alimentaire, vise des repas varies avec legumes, proteines et bonnes graisses a chaque repas', 2);
    }
    if (objectifs.indexOf('maintien') > -1) {
      pushAdvice('pour maintenir ton poids, garde une activite reguliere et une alimentation equilibree comme tu le fais deja', 1);
    }
    if (objectifs.indexOf('forme') > -1 && !advicePool.length) {
      pushAdvice('continue comme ca, tes indicateurs sont dans de bonnes tendances', 1);
    }

    if (!advicePool.length) pushAdvice('continue comme ca, tes indicateurs sont dans de bonnes tendances', 1);

    advicePool.sort(function(a,b) { return b.weight - a.weight; });
    var adviceParts = advicePool.slice(0, 3).map(function(a) { return a.txt; });"""

count1 = content.count(old1)
print("Bloc 1 (conseils personnalises) trouve " + str(count1) + " fois")
assert count1 == 1
content = content.replace(old1, new1)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: conseils de Mirella enrichis et personnalises selon objectifs + donnees du jour")
