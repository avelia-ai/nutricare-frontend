with open("app.html", "r") as f:
    content = f.read()

pos = 347483

step3 = '      <div style="display:flex;align-items:center;gap:10px;margin-bottom:18px">\n        <div style="width:24px;height:24px;border-radius:50%;background:#f0f0f0;color:#999;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0">3</div>\n        <select id="menuFiltresUnifie" onchange="window.applyFiltreUnifie(this.value)" style="flex:1;padding:11px 12px;border-radius:12px;border:1px solid #eee;font-size:0.82rem;background:white;color:#666">\n          <option value="">Filtres (optionnel)</option>\n          <optgroup label="Exclusions">\n            <option value="sans_gluten">Sans gluten</option>\n            <option value="sans_lactose">Sans lactose</option>\n            <option value="sans_oeufs">Sans oeufs</option>\n            <option value="sans_porc">Sans porc</option>\n            <option value="sans_poisson">Sans poisson</option>\n            <option value="vegetarien">Vegetarien</option>\n            <option value="vegan">Vegan</option>\n            <option value="halal">Halal</option>\n            <option value="casher">Casher</option>\n          </optgroup>\n          <optgroup label="Cuisine">\n            <option value="cuisine_africaine">Africaine</option>\n            <option value="cuisine_asiatique">Asiatique</option>\n            <option value="cuisine_orientale">Orientale</option>\n            <option value="cuisine_mediterraneenne">Mediterraneenne</option>\n            <option value="cuisine_indienne">Indienne</option>\n            <option value="cuisine_europeenne">Europeenne</option>\n          </optgroup>\n          <optgroup label="Objectif sante">\n            <option value="skincare">Skincare</option>\n            <option value="boost_cognitif">Boost cognitif</option>\n            <option value="sommeil">Sommeil</option>\n            <option value="cardio">Sante cardio</option>\n          </optgroup>\n          <optgroup label="Cycle menstruel">\n            <option value="cycle_menstrues">Menstrues J1-J5</option>\n            <option value="cycle_folliculaire">Folliculaire J6-J13</option>\n            <option value="cycle_ovulation">Ovulation J14-J16</option>\n            <option value="cycle_luteale">Luteale J17-J28</option>\n          </optgroup>\n        </select>\n      </div>\n'

new_content = content[:pos] + step3 + content[pos:]

with open("app.html", "w") as f:
    f.write(new_content)

print(f"OK - etape 3 inseree {len(step3)} chars a position {pos}")
