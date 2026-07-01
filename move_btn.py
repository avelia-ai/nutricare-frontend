with open("app.html", "r") as f:
    content = f.read()

pos_bouton_debut = 347483
pos_bouton_fin = 348084
pos_filtres_fin = 352664

bouton = content[pos_bouton_debut:pos_bouton_fin]

# Supprimer le bouton de sa position actuelle + les 2 sauts de ligne apres
content_sans_bouton = content[:pos_bouton_debut] + content[pos_bouton_fin+2:]

# Recalculer la position des filtres apres suppression
decalage = pos_bouton_fin + 2 - pos_bouton_debut
nouvelle_pos_filtres = pos_filtres_fin - decalage

# Inserer le bouton apres les filtres avec une marge
new_content = content_sans_bouton[:nouvelle_pos_filtres] + '\n      ' + bouton + '\n' + content_sans_bouton[nouvelle_pos_filtres:]

with open("app.html", "w") as f:
    f.write(new_content)

print(f"OK - bouton deplace apres les filtres")
print(f"Taille avant:{len(content)} apres:{len(new_content)}")
