with open("app.html", "r") as f:
    content = f.read()


# Localiser le bloc filtres existant
debut_marker = '      <div style="border-top:1px solid rgba(255,154,108,0.1);padding-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:10px" id="menuFiltersGrid">'
fin_marker = '    <div id="menusLoading"'

debut_idx = content.find(debut_marker)
fin_idx = content.find(fin_marker)

print(f"Debut: {debut_idx}, Fin: {fin_idx}")
if debut_idx == -1:
    print("ERREUR: debut_marker non trouve")
if fin_idx == -1:
    print("ERREUR: fin_marker non trouve")

nouveau_bloc = '''      <div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:14px">
        <div style="width:24px;height:24px;border-radius:50%;background:#f0f0f0;color:#999;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px">3</div>
        <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:8px" id="menuFiltersGrid">
          <div>
            <div style="font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.8px;color:#aaa;margin-bottom:5px">Exclusions</div>
            <select id="filterExclusions" onchange="window.applySelectFilter('filterExclusions')" style="width:100%;padding:9px 10px;border:1px solid #eee;border-radius:10px;font-size:0.78rem;color:#2D2D2D;background:white;cursor:pointer">
              <option value="">Aucune</option>
              <option value="sans_gluten">Sans gluten</option>
              <option value="sans_lactose">Sans lactose</option>
              <option value="sans_fruits_a_coques">Sans fruits a coques</option>
              <option value="sans_oeufs">Sans oeufs</option>
              <option value="sans_porc">Sans porc</option>
              <option value="sans_poisson">Sans poisson</option>
              <option value="vegetarien">Vegetarien</option>
              <option value="vegan">Vegan</option>
              <option value="halal">Halal</option>
              <option value="casher">Casher</option>
              <option value="sans_alcool">Sans alcool</option>
            </select>
          </div>
          <div>
            <div style="font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.8px;color:#aaa;margin-bottom:5px">Cuisine</div>
            <select id="filterCuisine" onchange="window.applySelectFilter('filterCuisine')" style="width:100%;padding:9px 10px;border:1px solid #eee;border-radius:10px;font-size:0.78rem;color:#2D2D2D;background:white;cursor:pointer">
              <option value="">Toutes cuisines</option>
              <option value="cuisine_africaine">Africaine</option>
              <option value="cuisine_asiatique">Asiatique</option>
              <option value="cuisine_orientale">Orientale</option>
              <option value="cuisine_mediterraneenne">Mediterraneenne</option>
              <option value="cuisine_latine">Latino-americaine</option>
              <option value="cuisine_indienne">Indienne</option>
              <option value="cuisine_europeenne">Europeenne</option>
            </select>
          </div>
          <div>
            <div style="font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.8px;color:#aaa;margin-bottom:5px">Objectif sante</div>
            <select id="filterObjectifSante" onchange="window.applySelectFilter('filterObjectifSante')" style="width:100%;padding:9px 10px;border:1px solid #eee;border-radius:10px;font-size:0.78rem;color:#2D2D2D;background:white;cursor:pointer">
              <option value="">Aucun objectif</option>
              <option value="skincare">Skincare</option>
              <option value="prise_de_masse">Prise de masse</option>
              <option value="perte_de_poids">Perte de poids</option>
              <option value="seche">Seche</option>
              <option value="boost_cognitif">Boost cognitif</option>
              <option value="sommeil">Sommeil</option>
              <option value="cardio">Sante cardio</option>
            </select>
          </div>
          <div>
            <div style="font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.8px;color:#aaa;margin-bottom:5px">Cycle menstruel</div>
            <select id="filterCycle" onchange="window.applySelectFilter('filterCycle')" style="width:100%;padding:9px 10px;border:1px solid #eee;border-radius:10px;font-size:0.78rem;color:#2D2D2D;background:white;cursor:pointer">
              <option value="">Non renseigne</option>
              <option value="cycle_menstrues">Menstrues J1-J5</option>
              <option value="cycle_folliculaire">Folliculaire J6-J13</option>
              <option value="cycle_ovulation">Ovulation J14-J16</option>
              <option value="cycle_luteale">Luteale J17-J28</option>
            </select>
          </div>
        </div>
      </div>
    '''

new_content = content[:debut_idx] + nouveau_bloc + content[fin_idx:]
with open("app.html", "w") as f:
    f.write(new_content)

opens = nouveau_bloc.count('<div')
closes = nouveau_bloc.count('</div>')
print(f"OK - div ouverts:{opens} fermes:{closes} - taille avant:{len(content)} apres:{len(new_content)}")
