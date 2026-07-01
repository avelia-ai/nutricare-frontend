with open("app.html", "r") as f:
    content = f.read()

debut = content.find('    <!-- Mes propres menus -->')
fin = content.find('      <div id="persoMenusContent"')

ancien_header = content[debut:fin]

nouveau_header = '''    <!-- Mes propres menus -->
    <div style="background:#FFFCFA;border-radius:22px;border:1px solid rgba(255,154,108,0.2);box-shadow:0 2px 20px rgba(230,110,70,0.07);margin-top:14px;margin-bottom:16px;overflow:hidden">
      <div style="background:linear-gradient(135deg,#1a1a1a,#2d2d2d);padding:20px;cursor:pointer" onclick="window.togglePersoMenus()">
        <div style="display:flex;align-items:center;justify-content:space-between">
          <div style="display:flex;align-items:center;gap:12px">
            <div style="width:38px;height:38px;border-radius:11px;background:rgba(255,107,107,0.15);border:1px solid rgba(255,107,107,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FF6B6B" stroke-width="2" stroke-linecap="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
            </div>
            <div>
              <div style="font-size:10px;color:rgba(255,154,108,0.7);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:3px">Manuel</div>
              <div style="font-size:16px;font-weight:700;color:white">Mes propres menus</div>
            </div>
          </div>
          <div style="display:flex;align-items:center;gap:10px">
            <div id="persoMenusChevron" style="color:rgba(255,255,255,0.3);transition:transform 0.2s;font-size:18px">▾</div>
            <div onclick="event.stopPropagation();var cb=document.getElementById('persoMenusEnabled');cb.checked=!cb.checked;window.onPersoMenusToggle();" style="position:relative;width:44px;height:24px;cursor:pointer">
              <input type="checkbox" id="persoMenusEnabled" onchange="window.onPersoMenusToggle()" style="opacity:0;width:0;height:0;position:absolute">
              <div id="persoToggleTrack" style="position:absolute;inset:0;background:rgba(255,255,255,0.15);border-radius:12px;transition:.2s"></div>
              <div id="persoToggleThumb" style="position:absolute;top:3px;left:3px;width:18px;height:18px;background:white;border-radius:50%;transition:.2s;opacity:0.5"></div>
            </div>
          </div>
        </div>
        <div style="font-size:12px;color:rgba(255,255,255,0.35);margin-top:10px">Composez vos repas librement, jour par jour</div>
      </div>
      <div style="padding:16px 20px;background:linear-gradient(135deg,#1a1a1a,#2d2d2d);border-top:1px solid rgba(255,255,255,0.05)">
        <select id="persoObjectif" style="width:100%;padding:10px 12px;border-radius:11px;border:none;font-size:0.82rem;background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.7)">
          <option value="">Objectif nutritionnel (optionnel)</option>
          <option value="perte_de_poids">Perte de poids</option>
          <option value="prise_de_masse">Prise de masse</option>
          <option value="seche">Seche</option>
          <option value="maintenance">Maintien du poids</option>
          <option value="performance">Performance sportive</option>
          <option value="sante">Sante generale</option>
        </select>
      </div>
'''

new_content = content[:debut] + nouveau_header + content[fin:]

with open("app.html", "w") as f:
    f.write(new_content)

print(f"OK - header noir applique, taille avant:{len(content)} apres:{len(new_content)}")
