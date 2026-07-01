with open("app.html", "r") as f:
    content = f.read()

debut = content.find('      <!-- Filtres en selects -->')
fin = content.find('    <div id="menusLoading"')

print(f"debut={debut} fin={fin} taille_a_supprimer={fin-debut}")

new_content = content[:debut] + content[fin:]

with open("app.html", "w") as f:
    f.write(new_content)

print(f"OK - anciens filtres supprimes")
