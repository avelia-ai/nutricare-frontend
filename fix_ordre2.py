with open("app.html", "r") as f:
    content = f.read()

pos_bouton = 347483
pos_filtre = 348086
pos_loading = 350585

bloc_bouton = content[pos_bouton:pos_filtre]
bloc_filtre = content[pos_filtre:pos_loading]

nouveau = bloc_filtre + bloc_bouton.replace('margin-bottom:14px">', 'margin-bottom:14px;margin-top:14px">')

new_content = content[:pos_bouton] + nouveau + content[pos_loading:]

with open("app.html", "w") as f:
    f.write(new_content)

print(f"OK - taille avant:{len(content)} apres:{len(new_content)}")
print(f"Verification - generateMenuBtn avant menusLoading: {new_content.find('generateMenuBtn') < new_content.find('menusLoading')}")
