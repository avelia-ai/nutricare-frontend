with open("app.html", "r") as f:
    content = f.read()

pos = content.find('  window.applySelectFilter = function() {')

js = '  window.applyFiltreUnifie = function(valeur) {\n    if (!valeur) return;\n    var excl = ["sans_gluten","sans_lactose","sans_oeufs","sans_porc","sans_poisson","vegetarien","vegan","halal","casher"];\n    var cuis = ["cuisine_africaine","cuisine_asiatique","cuisine_orientale","cuisine_mediterraneenne","cuisine_indienne","cuisine_europeenne"];\n    var sant = ["skincare","boost_cognitif","sommeil","cardio"];\n    var cycl = ["cycle_menstrues","cycle_folliculaire","cycle_ovulation","cycle_luteale"];\n    [excl,cuis,sant,cycl].forEach(function(cat){ if(cat.indexOf(valeur)!==-1) cat.forEach(function(v){ activeMenuFilters.delete(v); }); });\n    activeMenuFilters.add(valeur);\n  };\n'

new_content = content[:pos] + js + content[pos:]
with open("app.html", "w") as f:
    f.write(new_content)
print(f"OK - JS insere a {pos}")
