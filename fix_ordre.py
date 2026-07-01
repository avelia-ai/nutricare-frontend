with open("app.html", "r") as f:
    content = f.read()

# Trouver les positions cles
pos_bouton = content.find('      <button onclick="generateMenu()" id="generateMenuBtn"')
pos_filtre = content.find('      <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px">\n        <div style="width:24px;height:24px;border-radius:50%;background:#f0f0f0;color:#999;font-size:11px;font-weight:700')
pos_loading = content.find('    <div id="menusLoading"')

print(f"pos_bouton={pos_bouton}")
print(f"pos_filtre={pos_filtre}")
print(f"pos_loading={pos_loading}")
print(f"ordre correct: bouton avant filtre = {pos_bouton < pos_filtre}")
