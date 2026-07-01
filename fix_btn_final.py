with open("app.html", "r") as f:
    content = f.read()

old = '    </div>\n\n\n            <button onclick="generateMenu()" id="generateMenuBtn"'
new = '\n            <button onclick="generateMenu()" id="generateMenuBtn"'

if old in content:
    # Trouver la fin du bouton
    pos_old = content.find(old)
    pos_btn_fin = content.find('</button>', pos_old) + len('</button>')
    
    # Reconstruire : retirer les </div> d'avant, les remettre apres le bouton
    bouton_complet = content[pos_old+len('    </div>\n\n\n'):pos_btn_fin]
    new_content = content[:pos_old] + '\n      ' + bouton_complet + '\n    </div>\n' + content[pos_btn_fin:]
    
    with open("app.html", "w") as f:
        f.write(new_content)
    print(f"OK taille avant:{len(content)} apres:{len(new_content)}")
else:
    print("ERREUR pattern non trouve")
