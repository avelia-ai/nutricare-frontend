with open("app.html", "r") as f:
    content = f.read()

marker = '  window.applySelectFilter = function() {'
pos = content.find(marker)

js = '''  window.applyFiltreUnifie = function(valeur) {
    if (!valeur) return;
    var excl = ['sans_gluten','sans_lactose','sans_fruits_a_coques','sans_oeufs','sans_porc','sans_poisson','vegetarien','vegan','halal','casher','sans_alcool'];
    var cuis = ['cuisine_africaine','cuisine_asiatique','cuisine_orientale','cuisine_mediterraneenne','cuisine_latine','cuisine_indienne','cuisine_europeenne'];
    var sant = ['skincare','boost_cognitif','sommeil','cardio'];
    var cycl = ['cycle_menstrues','cycle_folliculaire','cycle_ovulation','cycle_luteale'];
    excl.forEach(function(v){if(excl.indexOf(valeur)!==-1)activeMenuFilters.delete(v);});
    cuis.forEach(function(v){if(cuis.indexOf(valeur)!==-1)activeMenuFilters.delete(v);});
    sant.forEach(function(v){if(sant.indexOf(valeur)!==-1)activeMenuFilters.delete(v);});
    cycl.forEach(function(v){if(cycl.indexOf(valeur)!==-1)activeMenuFilters.delete(v);});
    activeMenuFilters.add(valeur);
  };
'''

new_content = content[:pos] + js + content[pos:]
with open("app.html", "w") as f:
    f.write(new_content)
print(f"OK - applyFiltreUnifie ajoute a position {pos}")
