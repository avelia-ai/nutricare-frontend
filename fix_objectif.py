with open("app.html", "r") as f:
    content = f.read()

# Inserer le select juste apres la fermeture du header noir, avant persoMenusContent
marker = '      <div id="persoMenusContent"'
pos = content.find(marker)

select_html = '      <div style="padding:12px 20px;background:linear-gradient(135deg,#1a1a1a,#2d2d2d)">\n        <select id="persoObjectif" style="width:100%;padding:10px 12px;border-radius:11px;border:none;font-size:0.82rem;background:white;color:#2D2D2D"><option value="">Objectif nutritionnel (optionnel)</option><option value="perte_de_poids">Perte de poids</option><option value="prise_de_masse">Prise de masse</option><option value="seche">Seche</option><option value="maintenance">Maintien du poids</option><option value="performance">Performance sportive</option><option value="sante">Sante generale</option></select>\n      </div>\n'

new_content = content[:pos] + select_html + content[pos:]
with open("app.html", "w") as f:
    f.write(new_content)
print(f"OK - select reinjecte avant persoMenusContent")
