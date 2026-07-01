with open("app.html", "r") as f:
    content = f.read()

# Trouver les positions exactes
p1 = content.find('        </select>\n      </div>\n    </div>\n      <button')
p2 = content.find('\n    <div id="menusLoading"')
bouton_zone = content[p1:p2]
print(f"p1={p1} p2={p2}")
print(f"Zone bouton ({len(bouton_zone)} chars):")
print(repr(bouton_zone[:100]))
