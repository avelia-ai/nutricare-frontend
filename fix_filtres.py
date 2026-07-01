with open("app.html", "r") as f:
    content = f.read()

ancien = content[content.find('      <!-- Filtres en selects -->'):content.find('    <div id="menusLoading"')]

nouveau = '''      <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px">
        <div style="width:24px;height:24px;border-radius:50%;background:#f0f0f0;color:#999;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0">3</div>
        <select id="menuFiltresUnifie" onchange="window.applyFiltreUnifie(this.value)" style="flex:1;padding:11px 12px;border-radius:12px;border:1px solid #eee;font-size:0.82rem;background:white;color:#666">
          <option value="">Filtres (optionnel)</option>
          <optgroup label="Exclusions alimentaires">
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
          </optgroup>
          <optgroup label="Type de cuisine">
            <option value="cuisine_africaine">Africaine</option>
            <option value="cuisine_asiatique">Asiatique</option>
            <option value="cuisine_orientale">Orientale</option>
            <option value="cuisine_mediterraneenne">Mediterraneenne</option>
            <option value="cuisine_latine">Latino-americaine</option>
            <option value="cuisine_indienne">Indienne</option>
            <option value="cuisine_europeenne">Europeenne</option>
          </optgroup>
          <optgroup label="Objectif sante">
            <option value="skincare">Skincare</option>
            <option value="boost_cognitif">Boost cognitif</option>
            <option value="sommeil">Sommeil</option>
            <option value="cardio">Sante cardio</option>
          </optgroup>
          <optgroup label="Cycle menstruel">
            <option value="cycle_menstrues">Menstrues J1-J5</option>
            <option value="cycle_folliculaire">Folliculaire J6-J13</option>
            <option value="cycle_ovulation">Ovulation J14-J16</option>
            <option value="cycle_luteale">Luteale J17-J28</option>
          </optgroup>
        </select>
      </div>
    </div>
'''

new_content = content.replace(ancien, nouveau)
if new_content == content:
    print("ERREUR: aucun remplacement effectue")
else:
    with open("app.html", "w") as f:
        f.write(new_content)
    print(f"OK - ancien:{len(ancien)} chars -> nouveau:{len(nouveau)} chars")
