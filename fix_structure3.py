with open("app.html", "r") as f:
    content = f.read()

p1 = 349940
p2 = 350600

zone = content[p1:p2]

# Remplacer    </div>\n    </div>\n      <button  par    </div>\n      <button
nouveau = zone.replace('      </div>\n    </div>\n      <button', '      </div>\n      <button', 1)
# Et ajouter    </div>\n juste avant menusLoading
nouveau = nouveau.rstrip() + '\n    </div>\n'

new_content = content[:p1] + nouveau + content[p2:]

with open("app.html", "w") as f:
    f.write(new_content)

print(f"OK - taille avant:{len(content)} apres:{len(new_content)}")
