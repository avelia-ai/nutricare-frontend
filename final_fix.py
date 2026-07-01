with open("app.html", "r") as f:
    content = f.read()

debut_filtres = content.find('      <!-- Filtres en selects -->')
fin_filtres = content.find('    <!-- Mes propres menus -->')
pos_bouton_fin = content.find('\n\n    <!-- Mes propres menus -->')

# On remplace tout le bloc filtres par un simple </div> de fermeture
new_content = content[:debut_filtres] + '    </div>\n' + content[fin_filtres:]

with open("app.html", "w") as f:
    f.write(new_content)

print(f"OK - filtres remplaces par fermeture div")
print(f"Chars supprimes: {fin_filtres - debut_filtres}")
