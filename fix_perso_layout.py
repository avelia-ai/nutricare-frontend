with open("app.html", "r") as f:
    content = f.read()

# 1. Supprimer le bloc objectif du header noir (de la div padding jusqu'au select ferme)
debut_objectif_zone = content.find('\n      <div style="padding:16px 20px;background:linear-gradient(135deg,#1a1a1a,#2d2d2d);border-top:1px solid rgba(255,255,255,0.05)">')
fin_objectif_zone = content.find('</div>\n', debut_objectif_zone) + len('</div>\n')
objectif_select = content[debut_objectif_zone:fin_objectif_zone]
content = content[:debut_objectif_zone] + content[fin_objectif_zone:]
print(f"OK1 - objectif retire du header noir ({len(objectif_select)} chars)")

# 2. L'inserer dans persoMenusContent (qui est vide, juste un div)
pos_perso = content.find('<div id="persoMenusContent"')
pos_perso_end = content.find('>', pos_perso) + 1
select_html = '\n        <select id="persoObjectif" style="width:100%;padding:10px 12px;border-radius:11px;border:1px solid #eee;font-size:0.82rem;background:white;color:#666;margin-bottom:12px"><option value="">Objectif nutritionnel (optionnel)</option><option value="perte_de_poids">Perte de poids</option><option value="prise_de_masse">Prise de masse</option><option value="seche">Seche</option><option value="maintenance">Maintien du poids</option><option value="performance">Performance sportive</option><option value="sante">Sante generale</option></select>'
content = content[:pos_perso_end] + select_html + content[pos_perso_end:]
print(f"OK2 - objectif ajoute dans persoMenusContent")

# 3. Styler le bouton analyser
pos_btn = content.find('Analyser un repas par photo')
debut_btn = content.rfind('<button', 0, pos_btn)
fin_btn = content.find('</button>', pos_btn) + len('</button>')
ancien_btn = content[debut_btn:fin_btn]
nouveau_btn = '<button onclick="showAnalysisView()" style="width:100%;background:#f0ece8;color:#FF6B6B;border:none;border-radius:12px;padding:12px;font-size:12.5px;font-weight:700;display:flex;align-items:center;justify-content:center;gap:6px;margin-top:12px"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#FF6B6B" stroke-width="2" stroke-linecap="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>Analyser un repas par photo</button>'
content = content[:debut_btn] + nouveau_btn + content[fin_btn:]
print(f"OK3 - bouton analyser restyled")

with open("app.html", "w") as f:
    f.write(content)
print("DONE")
