with open("app.html", "r") as f:
    content = f.read()

old = "  window.applySelectFilter = function() {"
new = """  window.applyFiltreUnifie = function(valeur) {
    var categoriesExclusions = ['sans_gluten','sans_lactose','sans_fruits_a_coques','sans_oeufs','sans_porc','sans_poisson','vegetarien','vegan','halal','casher','sans_alcool'];
    var categoriesCuisine = ['cuisine_africaine','cuisine_asiatique','cuisine_orientale','cuisine_mediterraneenne','cuisine_latine','cuisine_indienne','cuisine_europeenne'];
    var categoriesSante = ['skincare','boost_cognitif','sommeil','cardio'];
    var categoriesCycle = ['cycle_menstrues','cycle_folliculaire','cycle_ovulation','cycle_luteale'];
    var toutes = categoriesExclusions.concat(categoriesCuisine).concat(categoriesSante).concat(categoriesCycle);
    if (!valeur) return;
    if (categoriesExclusions.indexOf(valeur) !== -1) categoriesExclusions.forEach(function(v){ activeMenuFilters.delete(v); });
    if (categoriesCuisine.indexOf(valeur) !== -1) categoriesCuisine.forEach(function(v){ activeMenuFilters.delete(v); });
    if (categoriesSante.indexOf(valeur) !== -1) categoriesSante.forEach(function(v){ activeMenuFilters.delete(v); });
    if (categoriesCycle.indexOf(valeur) !== -1) categoriesCycle.forEach(function(v){ activeMenuFilters.delete(v); });
    activeMenuFilters.add(valeur);
  };
  window.applySelectFilter = function() {"""

if old in content and content.count(old) == 1:
    content = content.replace(old, new)
    with open("app.html", "w") as f:
        f.write(content)
    print("OK - applyFiltreUnifie ajoute")
else:
    print("ERREUR - count=" + str(content.count(old)))
