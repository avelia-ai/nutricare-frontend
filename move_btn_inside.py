with open("app.html", "r") as f:
    content = f.read()

# Extraire le bouton
pos_btn = 352062
pos_btn_fin = content.find('</button>', pos_btn) + len('</button>')
bouton = content[pos_btn:pos_btn_fin]

# Supprimer le bouton + les sauts de ligne avant
content_sans_btn = content[:352053+6] + content[pos_btn_fin:]

# Le reinsérer avant les 2 </div> de fermeture du bloc
pos_insert = content_sans_btn.find('/div>\n    </div>\n\n\n', 347000)
print(f"Point d insertion: {pos_insert}")
print(f"Contexte: {repr(content_sans_btn[pos_insert-5:pos_insert+30])}")

new_content = content_sans_btn[:pos_insert-5] + '\n      ' + bouton + '\n    </div>\n    </div>\n\n' + content_sans_btn[pos_insert+len('/div>\n    </div>\n\n\n'):]

with open("app.html", "w") as f:
    f.write(new_content)
print(f"OK taille avant:{len(content)} apres:{len(new_content)}")
