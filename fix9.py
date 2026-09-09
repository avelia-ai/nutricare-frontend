# -*- coding: utf-8 -*-
with open('app.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1) Ajouter le HTML de l'etape 3 juste apres l'etape 2 (menuObjectif)
old1 = """      <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px">
        <div style="width:24px;height:24px;border-radius:50%;background:#f0f0f0;color:#999;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0">2</div>
        <select id="menuObjectif" style="flex:1;padding:11px 12px;border-radius:12px;border:1px solid #eee;font-size:0.82rem;background:white;color:#666">
          <option value="">Objectif nutritionnel</option>
          <option value="perte_de_poids">Perte de poids</option>
          <option value="prise_de_masse">Prise de masse</option>
          <option value="seche">Seche</option>
          <option value="maintenance">Maintien du poids</option>
          <option value="performance">Performance sportive</option>
          <option value="sante">Sante generale</option>
        </select>
      </div>"""

new1 = """      <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px">
        <div style="width:24px;height:24px;border-radius:50%;background:#f0f0f0;color:#999;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0">2</div>
        <select id="menuObjectif" style="flex:1;padding:11px 12px;border-radius:12px;border:1px solid #eee;font-size:0.82rem;background:white;color:#666">
          <option value="">Objectif nutritionnel</option>
          <option value="perte_de_poids">Perte de poids</option>
          <option value="prise_de_masse">Prise de masse</option>
          <option value="seche">Seche</option>
          <option value="maintenance">Maintien du poids</option>
          <option value="performance">Performance sportive</option>
          <option value="sante">Sante generale</option>
        </select>
      </div>
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px">
        <div style="width:24px;height:24px;border-radius:50%;background:#f0f0f0;color:#999;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0">3</div>
        <select id="menuRythme" style="flex:1;padding:11px 12px;border-radius:12px;border:1px solid #eee;font-size:0.82rem;background:white;color:#666">
          <option value="">Rythme de repas (optionnel)</option>
          <option value="3_repas_classiques">3 repas par jour (classique)</option>
          <option value="5_6_petits_repas">5-6 petits repas par jour</option>
          <option value="jeune_16_8">Jeune intermittent 16:8</option>
          <option value="jeune_18_6">Jeune intermittent 18:6</option>
          <option value="jeune_20_4">Jeune intermittent 20:4</option>
          <option value="omad">OMAD (1 repas par jour)</option>
          <option value="jeune_5_2">Jeune 5:2 (2 jours restreints/semaine)</option>
        </select>
      </div>"""

count1 = content.count(old1)
print("Bloc 1 (HTML select rythme) trouve " + str(count1) + " fois")
assert count1 == 1
content = content.replace(old1, new1)

# 2) Integrer dans la cle de cache
old2 = "const filtresKey = Array.from(activeMenuFilters || []).sort().join('_') + '_' + (document.getElementById('menuObjectif')?.value || '');"
new2 = "const filtresKey = Array.from(activeMenuFilters || []).sort().join('_') + '_' + (document.getElementById('menuObjectif')?.value || '') + '_' + (document.getElementById('menuRythme')?.value || '');"

count2 = content.count(old2)
print("Bloc 2 (cache key) trouve " + str(count2) + " fois")
assert count2 == 1
content = content.replace(old2, new2)

# 3) Integrer dans le payload envoye au backend
old3 = "body: JSON.stringify({ lang: 'fr', menu_filters: Array.from(activeMenuFilters || []), objectif_nutritionnel: objectifMenuActuel, target_calories: targetCalories, jour: jourAujourdhui }),"
new3 = "body: JSON.stringify({ lang: 'fr', menu_filters: Array.from(activeMenuFilters || []), objectif_nutritionnel: objectifMenuActuel, rythme_repas: document.getElementById('menuRythme')?.value || '', target_calories: targetCalories, jour: jourAujourdhui }),"

count3 = content.count(old3)
print("Bloc 3 (payload backend) trouve " + str(count3) + " fois")
assert count3 == 1
content = content.replace(old3, new3)

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: champ Rythme de repas ajoute (etape 3)")
